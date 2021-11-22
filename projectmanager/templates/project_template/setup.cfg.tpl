[metadata]
name = {{project_name}}
version = attr: {{project_name}}.__version__
author = ADD NAME
author_email = ADD MAIL
description = ADD DESCRIPTION
long_description = file: README.md
long_description_content_type = text/markdown
url = ADD URL
project_urls =
    Bug Tracker = ADD ISSUE URL
classifiers =
    Programming Language :: Python :: 3
    License :: OSI Approved :: MIT License
    Operating System :: OS Independent

[options]
packages = find:
python_requires = >=3.6

[options.entry_points]
console_scripts =
    {{project_name}} = {{project_name}}.{{project_name}}:main
