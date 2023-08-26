import collections  # noqa: F401
import collections.abc  # noqa: F401
from pathlib import Path
from pptx import Presentation
from pptx.util import Inches
from pptx.enum.text import MSO_ANCHOR, MSO_AUTO_SIZE, PP_ALIGN

from ..schemas.base_schema import CreatePresentation
from ..config import settings
from fastapi.responses import FileResponse
import anyio
from starlette.background import BackgroundTask
from time import time
from pptx.shapes.placeholder import TablePlaceholder

class BaseSevice:
    def generate_template(self) -> Presentation:
        prs = Presentation(str(settings.templates_path / "1.pptx"))
        return prs

    def generate_filename(self) -> Path:
        return settings.media_path / "test.pptx"  # f"{time()}.pptx"

    def generate_title_slide(self, prs: Presentation, data: CreatePresentation) -> None:
        """Генерация первого слайда - Титульник"""
        title_slide_layout = prs.slide_layouts[0]
        slide = prs.slides.add_slide(title_slide_layout)
        # print(slide.placeholders[0], slide.placeholders[1].name)
        _title = slide.shapes.title
        _subtitle = slide.placeholders[1]
        _title.text = data.project_name
        _subtitle.text = data.short_description
        # TODO need fix
        _subtitle_text_frame = _subtitle.text_frame
        _subtitle_text_frame.word_wrap = True
        _subtitle_text_frame.auto_size = MSO_AUTO_SIZE.TEXT_TO_FIT_SHAPE
        _subtitle_text_frame.alignment = PP_ALIGN.JUSTIFY

    def generate_problems_slide(
        self, prs: Presentation, data: CreatePresentation
    ) -> None:
        """Генерация второго слайда - Проблемы"""
        title_and_content_layout = prs.slide_layouts[5]
        slide = prs.slides.add_slide(title_and_content_layout)
        _title = slide.shapes.title
        _title.text = "Проблемы"

        left_inch = Inches(1.0)
        top_inch = Inches(2.0)
        width_inch = Inches(8.0)
        height_inch = Inches(3)

        _rows = (max(len(x.issue) for x in data.problem)) + 1
        _cols = len(data.problem)
        # print(_cols, _cols)

        table = slide.shapes.add_table(
            rows=_rows, cols=_cols,
            left=left_inch, top=top_inch, width=width_inch, height=height_inch
        ).table

        for i in range(0, _cols):
            cell = table.cell(0, i)
            cell.text = data.problem[i].target_audience
            for j in range(1, _rows):
                cell = table.cell(j, i)
                cell.text = data.problem[i].issue[j-1]


    def generate_solution_slide(
        self, prs: Presentation, data: CreatePresentation
    ) -> None:
        """Генерация четвёртого слайда - Решение"""
        title_and_content_layout = prs.slide_layouts[5]
        slide = prs.slides.add_slide(title_and_content_layout)
        _title = slide.shapes.title
        _title.text = "Решение"

        left_inch = Inches(1.0)
        top_inch = Inches(2.0)
        width_inch = Inches(8.0)
        height_inch = Inches(3)

        _rows = (max(len(x.solution) for x in data.problem)) + 1
        _cols = len(data.problem)

        table = slide.shapes.add_table(
            rows=_rows, cols=_cols,
            left=left_inch, top=top_inch, width=width_inch, height=height_inch
        ).table

        for i in range(0, _cols):
            cell = table.cell(0, i)
            cell.text = data.problem[i].target_audience
            for j in range(1, _rows):
                cell = table.cell(j, i)
                cell.text = data.problem[i].solution[j-1]

    async def create_presentation(self, data: CreatePresentation):
        prs = self.generate_template()
        # TODO: цвета + шрифты
        file = self.generate_filename()

        # debug
        # for i,slide in enumerate(prs.slide_layouts):
        #      print(i,slide.name)
        #     for shape in slide.placeholders:
        #         print(slide.name,";", shape.placeholder_format.idx, shape.name)

        self.generate_title_slide(prs, data)
        self.generate_problems_slide(prs, data)
        self.generate_solution_slide(prs, data)

        prs.save(str(file))
        return FileResponse(
            file, headers={"Content-Disposition": f'attachment; filename="{file.name}"'}, background=BackgroundTask(self.delete_file, file)
        )  # background=BackgroundTask(self.delete_file, file)

    async def delete_file(self, file):
        await anyio.run_sync_in_worker_thread(file.unlink)


# https://github.com/Soulter/hugging-chat-api
