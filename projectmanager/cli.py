"""
DOCSTRING
"""

import sys
import logging
from argparse import ArgumentParser
from pathlib import Path
from importlib import import_module
import projectmanager.commands


logger = logging.getLogger(__name__)

def check_subcommand(args):
    """
    Check that the provided subcommand exists.
    """

    logger.debug("Entering validate_subcommand(args) with args = %s", args)
    commands_dir = Path(projectmanager.commands.__path__[0])
    commands_files = commands_dir.glob("*.py")
    allowed_commands = [file.stem for file in commands_files]
    
    if not args.subcommand in allowed_commands:
        raise Exception(
            "Unexpected subcommand. "
            "Use one of the following:\n\t"+"\n\t".join(allowed_commands)
            )


def validate_name(args):
    """
    Check that no module exists with the name in args
    """

    logger.debug("Entering validate_name(args) with args = %s", args)
    if args.subcommand not in ['newproject', 'subpackage']:
        return
    try:
        import_module(args.name)
    except:
        pass
    else:
        raise Exception(
            f"Can not create '{args.name}' since a module with that name already exists. "
            "Please, choose another name."
        )
    
    if not args.name.isidentifier():
        raise Exception(
            f"'{args.name}' is not a valid name. Choose a name that:\n"
            "   - Only contains alphanumeric characters i.e. [a-z] and [0-9] or underscores\n"
            "   - Not starts with a number\n"
            "   - Not contains any spaces\n"
        )


def parse_command_line(argv=None):
    """
    Expects the two positional arguments 'subcommand' and 'name'
    """

    logger.debug("Entering parse_command_line(argv) with argv = %s", argv)
    try:
        argv = argv or sys.argv[1:]
    except IndexError:
        argv = "help"

    parser = ArgumentParser()
    parser.add_argument("subcommand", help="Enter a subcommand")
    parser.add_argument("name", help="Enter a name")

    # Add the calling program to args before returning it in case subcommands
    # later need to know if entry_point() was invoked by projectmanager.exe or manage.py
    prog = parser.prog
    args = parser.parse_args(argv)
    args.__dict__['prog'] = prog
    return args


def call_command(args):
    """
    Call the command provided on the cli
    """

    logger.debug("Entering call_command(args) with args = %s", args)
    module_path = f"projectmanager.commands.{args.subcommand}"
    cmd_module = import_module(module_path)
    cmd_module.handle(args)

def entry_point(argv=None):
    """
    This is where it all starts!
    """

    logger.debug("Entering entry_point()")
    args = parse_command_line()
    check_subcommand(args)
    validate_name(args)
    call_command(args)
