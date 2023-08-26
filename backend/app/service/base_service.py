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

from pptx.oxml.ns import nsdecls
from pptx.oxml import parse_xml

class BaseSevice:
    def generate_template(self) -> Presentation:
        prs = Presentation(str(settings.templates_path / "1.pptx"))
        return prs

    def generate_filename(self) -> Path:
        return settings.media_path / "test.pptx"  # f"{time()}.pptx"
    
    def create_table(self, slide, _rows, _cols):
        left_inch = Inches(1.0)
        top_inch = Inches(2.0)
        width_inch = Inches(8.0)
        height_inch = Inches(3)
        table = slide.shapes.add_table(
            rows=_rows, cols=_cols,
            left=left_inch, top=top_inch, width=width_inch, height=height_inch
        ).table
        return table
    
    def create_slide(self,  prs, slide_layout, title):
        title_slide_layout = prs.slide_layouts[slide_layout]
        slide = prs.slides.add_slide(title_slide_layout)
        _title = slide.shapes.title
        _title.text = title
        return slide

    def generate_title_slide(self, prs: Presentation, data: CreatePresentation) -> None:
        """Генерация первого слайда - Титульник"""
        slide = self.create_slide(prs, 0, data.project_name)
        _subtitle = slide.placeholders[1]
        _subtitle.text = data.short_description
        # TODO need fix
        _subtitle_text_frame = _subtitle.text_frame
        _subtitle_text_frame.word_wrap = True
        _subtitle_text_frame.auto_size = MSO_AUTO_SIZE.TEXT_TO_FIT_SHAPE
        _subtitle_text_frame.alignment = PP_ALIGN.JUSTIFY

    def generate_table_slide(self, prs: Presentation, data: CreatePresentation, title: str, content_func):
        slide = self.create_slide(prs, 5, title)

        max_content_length = max(len(content_func(x)) for x in data.problem)
        _rows = max_content_length + 1
        _cols = len(data.problem)

        table = self.create_table(slide, _rows, _cols)

        for i in range(0, _cols):
            cell = table.cell(0, i)
            cell.text = data.problem[i].target_audience
            for j, content in enumerate(content_func(data.problem[i])):
                cell = table.cell(j + 1, i)
                cell.text = content

    def generate_problems_slide(self, prs: Presentation, data: CreatePresentation):
        """Генерация второго слайда - Проблемы"""
        self.generate_table_slide(prs, data, "Проблемы", lambda x: x.issue)

    def generate_solution_slide(self, prs: Presentation, data: CreatePresentation):
        """Генерация четвёртого слайда - Решение"""
        self.generate_table_slide(prs, data, "Решение", lambda x: x.solution)

    def generate_description_slide(self, prs: Presentation, data: CreatePresentation) -> None:
        """Генерация третьего слайда - Описание"""
        slide = self.create_slide(prs, 1, "Описание")
        description = slide.placeholders[1]
        description.text = data.description

    def generate_members_slide(self, prs: Presentation, data: CreatePresentation):
        slide = self.create_slide(prs, 5, "Команда")
        _rows = 2
        _cols = len(data.members)
        table = self.create_table(slide, _rows, _cols)
        for i in range(0, _cols):
            table.cell(0, i).text = data.members[i].full_name
            table.cell(1, i).text = data.members[i].proffesion

    def generate_investors_slide(self, prs: Presentation, data: CreatePresentation):
        raise Exception("Not implemented")
    
    def generate_investing_rounds_slide(self, prs: Presentation, data: CreatePresentation):
        investing_rounds = data.investing_rounds
        if len(investing_rounds) > 1:
            raise Exception("Not implemented")

        stage = investing_rounds[0].stage
        amount = investing_rounds[0].amount
        slide = self.create_slide(prs, 5, f"За {stage.value} будет привлечено {amount} рублей")
        _title = slide.shapes.title
        _title.text = f"За {stage.value} будет привлечено {amount} рублей"
        if investing_rounds[0].fraction:
            _title.text += f" за долю в компании {investing_rounds[0].fraction}"

        _rows = 2
        _cols = len(investing_rounds[0].spending)
        table = self.create_table(slide, _rows, _cols)
        for i in range(0, _cols):
            print(investing_rounds[0].spending[i])
            table.cell(0, i).text = investing_rounds[0].spending[i].name
            table.cell(1, i).text = investing_rounds[0].spending[i].percent
    
    def generate_roadmap_slide(self, prs: Presentation, data: CreatePresentation):
        raise Exception("Not implemented")
    
    def generate_contacts_slide(self, prs: Presentation, data: CreatePresentation):
        raise Exception("Not implemented")
    
    def generate_business_units_slide(self, prs: Presentation, data: CreatePresentation):
        slide = self.create_slide(prs, 5, "Бизнес-модель")

        _rows = 3
        _cols = len(data.business_units)

        table = self.create_table(slide, _rows, _cols)

        for i in range(0, _cols):
            table.cell(0, i).text = data.business_units[i].name
            table.cell(1, i).text = data.business_units[i].income
            table.cell(2, i).text = data.business_units[i].revenue_share

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
        self.generate_description_slide(prs, data)
        self.generate_solution_slide(prs, data)
        self.generate_business_units_slide(prs, data)
        self.generate_investing_rounds_slide(prs, data)
        self.generate_members_slide(prs, data)

        prs.save(str(file))
        return FileResponse(
            file, headers={"Content-Disposition": f'attachment; filename="{file.name}"'}, background=BackgroundTask(self.delete_file, file)
        )  # background=BackgroundTask(self.delete_file, file)

    async def delete_file(self, file):
        await anyio.run_sync_in_worker_thread(file.unlink)


# https://github.com/Soulter/hugging-chat-api
