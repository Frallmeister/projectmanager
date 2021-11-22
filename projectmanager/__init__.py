VERSION = (0,1,0)

__version__ = ".".join(map(str, VERSION))

from log import configure_logging
configure_logging()
