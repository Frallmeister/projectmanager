"""
DOCSTRING
"""

import sys
import os
from argparse import ArgumentParser
from pathlib import Path
from importlib import import_module
import projectmanager.commands


def check_subcommands(args):
    """
    DOCSTRING
    """
    commands_dir = Path(projectmanager.commands.__path__[0])
    commands_files = commands_dir.glob("*.py")
    allowed_commands = [file.stem for file in commands_files]
    
    if not args.subcommand in allowed_commands:
        raise Exception(
            "Unexpected subcommand. "
            "Use one of the following:\n\t"+"\n\t".join(allowed_commands)
            )

def check_name(args):
    """
    DOCSTRING
    """
    try:
        print("In the try")
        import_module(args.name)
    except:
        print("In the except")
        pass
    else:
        print("In the else")
        raise Exception(
            f"Can not create '{args.name}' since a module with that name already exists. "
            "Please, choose another name."
        )

def parse_command_line():
    """
    DOCSTRING
    """
    parser = ArgumentParser()
    parser.add_argument("subcommand")
    parser.add_argument("name")
    args = parser.parse_args(sys.argv[1:])

    check_subcommands(args)
    check_name(args)



def entry_point():
    parse_command_line()
