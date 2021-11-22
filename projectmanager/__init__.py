VERSION = (0,1,0)

__version__ = ".".join(map(str, VERSION))

from projectmanager.log import configure_logging
configure_logging()
