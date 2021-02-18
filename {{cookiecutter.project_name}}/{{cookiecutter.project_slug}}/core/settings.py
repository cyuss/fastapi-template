# -*- coding: utf-8 -*-

from starlette.config import Config


# app settings
APP_VERSION = "{{cookiecutter.version}}"
APP_NAME = """{{cookiecutter.app_name}}"""
APP_DESCRIPTION = """{{cookiecutter.project_description}}"""
API_PREFIX = ""

# no autoload .env file by poetry
config = Config(".env")
