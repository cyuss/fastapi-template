# -*- coding: utf-8 -*-

import argparse
import re
import sys

import fire
from loguru import logger


quality_color_map = {
    "A": "51C62B",
    "B": "82E0AA",
    "C": "F7DC6F",
    "D": "F39C12",
    "E": "D35400",
    "F": "C0392B"
}


def _read_file(file_name: str) -> str:
    """Read a file content.

    Parameters
    ----------
    file_name : str
        File name to read

    Returns
    -------
    str
        File content string

    """
    with open(file_name, "r") as f:
        return f.read()


def update_readme(version: str, code_quality: str=None) -> None:
    """Update the README file version and quality code badges.

    Parameters
    ----------
    version : str
        The new version value
    code_quality : str
        The new quality code rank

    """
    file_name = "README.md"
    readme_content = _read_file(file_name)
    pattern = re.sub('img.shields.io/badge/version-\d+\.\d+\.\d+',
                     'img.shields.io/badge/version-{}'.format(version),
                     readme_content)
    logger.info("README file version updated to {}".format(version))
    if code_quality:
        code_quality = code_quality.capitalize()
        quality_color = quality_color_map[code_quality]
        pattern = re.sub('img.shields.io/badge/code_quality-[A-Z]-[0-9A-Z]{6}\?',
                         'img.shields.io/badge/code_quality-{}-{}?'.format(
                             code_quality, quality_color),
                         pattern)
        logger.info("Quality Code Rank updated to rank: {}".format(code_quality))
    with open(file_name, "w") as updated_file:
        updated_file.write(pattern)


def update_pyproject(version: str) -> None:
    """Update the pyproject.toml file's version variable.

    Parameters
    ----------
    version : str
        The new version value

    """
    file_name = "pyproject.toml"
    pyproject_content = _read_file(file_name)
    pattern = re.sub('version = \"\d+\.\d+\.\d+\"',
                     'version = "{}"'.format(version),
                     pyproject_content)
    logger.info("pyproject file version updated to {}".format(version))
    with open(file_name, "w") as updated_file:
        updated_file.write(pattern)


def update_makefile(version: str) -> None:
    """Update the Makefile version variable.

    Parameters
    ----------
    version : str
        The new version value

    """
    file_name = "Makefile"
    makefile_content = _read_file(file_name)
    pattern = re.sub('version = \d+\.\d+.\d+',
                     'version = {}'.format(version),
                     makefile_content)
    logger.info("Makefile file version updated to {}".format(version))
    with open(file_name, "w") as updated_file:
        updated_file.write(pattern)


def main(version: str, code_quality: str=None) -> None:
    if len(version) < 1:
        logger.info("No version passed.")
        return None
    update_pyproject(version)
    update_readme(version, code_quality)
    update_makefile(version)


if __name__ == "__main__":
    fire.Fire(main)
