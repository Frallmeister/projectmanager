import logging

logger = logging.getLogger(__name__)

def handle(args):
    logger.debug("In subpackage.handle(args) with args = %s", args)