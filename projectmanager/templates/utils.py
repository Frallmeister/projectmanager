"""
DOCSTRING
"""

import logging
from pathlib import Path

logger = logging.getLogger(__name__)


class TemplateHandler:
    """
    DOCSTRING
    """

    def __init__(self, folder, fields):
        """
        DOCSTRING
        """
        self.folder = folder
        self.fields = fields
        self.templates_dir = Path(__file__).parent / folder
        self.work_dir = Path().cwd().resolve()


    def generate(self):
        """
        DOCSTRING
        """

        for item in self.templates_dir.glob("**/*"):
            self.create_file(item)
            # if item.is_dir():
            #     self.create_dir(item)
            # elif item.is_file():
            #     self.create_file(item)


    def create_file(self, file_path):
        """
        DOCSTRING
        """
        rel_path = file_path.relative_to(self.templates_dir)
        full_path = self.work_dir / rel_path

        print(full_path)
        if full_path.is_file():
            if not full_path.parent.exists():
                logger.debug("Dir doesn't exist, %s", full_path)
        # file = str(rel_path).format(**self.fields).rstrip('.tpl')
        # logger.debug("Relative file path is %s", file)


    def create_dir(self, dir_path):
        """
        DOCSTRING
        """
        rel_path = dir_path.relative_to(self.templates_dir)
        directory = str(rel_path).format(**self.fields).rstrip('.tpl')
        # logger.debug("Relative directory is %s", directory)