
import collections 
import collections.abc
from pathlib import Path
from pptx import Presentation
from pptx.util import Inches
from ..config import settings
from fastapi.responses import FileResponse
import anyio
from starlette.background import BackgroundTask

class BaseSevice():
    async def create_presentation(self):

        prs = Presentation()
        title_slide_layout = prs.slide_layouts[0]
        slide = prs.slides.add_slide(title_slide_layout)
        title = slide.shapes.title
        subtitle = slide.placeholders[1]

        title.text = "Hello, World!"
        subtitle.text = "python-pptx was here!"

        file = settings.media_path / 'test.pptx'
        prs.save(str(file))
        return FileResponse(file, background=BackgroundTask(self.delete_file, file), headers= {'Content-Disposition': f'attachment; filename="{file.name}"'})

    async def delete_file(self, file):
        await anyio.run_sync_in_worker_thread(file.unlink)
