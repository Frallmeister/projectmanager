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

    logger.debug("In subpackage.handle(args) with args = %s", args)
    # Check if subpackage is called with manage.py to ensure the
    # subpackage will end up in the correct directory
    
    folder = 'subpackage_template'
    fields = {
        'subpackage_name': args.name,
    }

    tpl_handler = TemplateHandler(folder, fields)
    tpl_handler.generate()