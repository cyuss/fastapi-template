# -*- coding: utf-8 -*-

import pytest

from starlette.config import environ
from starlette.testclient import TestClient

from {{cookiecutter.project_slug}}.main import get_app


@pytest.fixture(scope="session")
def test_client() -> TestClient:
    app = get_app()
    with TestClient(app) as test_client:
        yield test_client
