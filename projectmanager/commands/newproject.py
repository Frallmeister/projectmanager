"""
DOCSTRING
"""

import logging
from projectmanager.templates.utils import TemplateHandler

logger = logging.getLogger(__name__)

def handle(args):
    """
    DOCSTRING
    """
    
    logger.debug("In newproject.handle(args) with args = %s", args)

    folder = 'project_template'
    fields = {
        'project_name': args.name,
    }

    tpl_handler = TemplateHandler(folder, fields)
    tpl_handler.generate()

