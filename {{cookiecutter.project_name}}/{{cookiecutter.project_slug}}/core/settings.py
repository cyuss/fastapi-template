# -*- coding: utf-8 -*-

from functools import lru_cache

from pydantic import BaseSettings


# app class settings
class Settings(BaseSettings):
    """Store settings variables and load env variables from .env file."""

    app_version: str = "{{cookiecutter.version}}"
    app_name: str = """{{cookiecutter.app_name}}"""
    app_description: str = """{{cookiecutter.project_description}}"""
    api_prefix: str = ""
    author: str = "{{cookiecutter.author}}"
    host: str = "{{cookiecutter.host}}"
    port: str = "{{cookiecutter.port}}"

    class Config:
        """Load .env file for env variables."""

        env_file = ".env"
        env_file_encoding = "utf-8"


@lru_cache()
def get_settings() -> Settings:
    """Create and cache settings object.

    Returns
    -------
    Settings
        Settings object
    """
    return Settings()
