import sys

def main():
    try:
        from projectmanager.cli import entry_point
    except ImportError:
        raise ImportError(
            "Could not import projectmanager. Make sure it is installed,\n"
            "preferably in a virtual environment and that the virtual environment\n"
            "is activated."
        )
    entry_point(sys.argv)