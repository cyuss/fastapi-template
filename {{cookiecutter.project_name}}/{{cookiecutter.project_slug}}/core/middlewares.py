# -*- coding: utf-8 -*-

import time
from contextvars import ContextVar
from uuid import uuid4

from loguru import logger
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.requests import Request


CORRELATION_ID_CTX_KEY: str = "correlation_id"
REQUEST_ID_CTX_KEY: str = "request_id"

_correlation_id_ctx_var: ContextVar[str] = ContextVar(CORRELATION_ID_CTX_KEY, default=None)
_request_id_ctx_var: ContextVar[str] = ContextVar(REQUEST_ID_CTX_KEY, default=None)


def get_correlation_id() -> str:
    """Return the correlation ID."""
    return _correlation_id_ctx_var.get()


def get_request_id() -> str:
    """Return the request ID to identify conflicting requests' logs."""
    return _request_id_ctx_var.get()


class RequestContextLogMiddleware(BaseHTTPMiddleware):
    """Custom middleware class to customize request's ID and processing time.

    Parameters
    ----------
    BaseHTTPMiddleware : BaseHTTPMiddleware
        Base class for HTTP Middleware.
    """

    # FIXME: Reuse the new format to define custom middleware t.ly/Regh
    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint) -> RequestResponseEndpoint:        
        correlation_id = _correlation_id_ctx_var.set(request.headers.get("X-Correlation-ID", str(uuid4())))
        request_id = _request_id_ctx_var.set(str(uuid4()))
        # update the request ID into the logger
        logger.configure(extra={"request_id": get_request_id()})
        # time the main request's function
        start_time = time.time()
        response = await call_next(request)
        process_time = time.time() - start_time
        # create response headers
        response.headers["X-Process-Time"] = str(process_time)
        response.headers["X-Correlation-ID"] = get_correlation_id()
        response.headers["X-Request-ID"] = get_request_id()
        logger.info("Process time: {:.5f}s".format(process_time))
        # reset the starlette context
        _correlation_id_ctx_var.reset(correlation_id)
        _request_id_ctx_var.reset(request_id)

        return response
