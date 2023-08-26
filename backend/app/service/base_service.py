
import collections # noqa: F401
import collections.abc  # noqa: F401
from pathlib import Path
from pptx import Presentation
from pptx.util import Inches

from ..schemas.base_schema import CreatePresentation
from ..config import settings
from fastapi.responses import FileResponse
import anyio
from starlette.background import BackgroundTask

class BaseSevice():
    async def create_presentation(self, data:CreatePresentation):

        prs = Presentation()
        title_slide_layout = prs.slide_layouts[0]
        slide = prs.slides.add_slide(title_slide_layout)
        title = slide.shapes.title
        subtitle = slide.placeholders[1]

        title.text = data.project_name
        subtitle.text = data.short_description
        file = settings.media_path / 'test.pptx'
        prs.save(str(file))
        return FileResponse(file, background=BackgroundTask(self.delete_file, file), headers= {'Content-Disposition': f'attachment; filename="{file.name}"'})

    async def delete_file(self, file):
        await anyio.run_sync_in_worker_thread(file.unlink)
# https://github.com/Soulter/hugging-chat-api