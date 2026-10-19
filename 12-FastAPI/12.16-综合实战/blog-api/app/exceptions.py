import logging
from http import HTTPStatus
from typing import Any

from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException

logger = logging.getLogger("blog.errors")


# ---------- 业务异常 ----------
# 路由和依赖里只抛这些异常，不直接构造 JSONResponse；格式统一由下面的 handler 负责


class AppError(Exception):
    status_code: int = 400
    code: str = "BAD_REQUEST"
    message: str = "请求有误"

    def __init__(self, message: str | None = None, *, headers: dict[str, str] | None = None):
        self.message = message or self.message
        self.headers = headers
        super().__init__(self.message)


class NotFoundError(AppError):
    status_code = 404
    code = "NOT_FOUND"
    message = "资源不存在"


class ConflictError(AppError):
    status_code = 409
    code = "CONFLICT"
    message = "资源冲突"


class PermissionDeniedError(AppError):
    status_code = 403
    code = "FORBIDDEN"
    message = "没有权限执行此操作"


class AuthenticationError(AppError):
    status_code = 401
    code = "UNAUTHORIZED"
    message = "认证失败"

    def __init__(self, message: str | None = None):
        # OAuth2 规范要求 401 响应带上 WWW-Authenticate 头
        super().__init__(message, headers={"WWW-Authenticate": "Bearer"})


# ---------- 统一错误响应 ----------


def error_response(
    request: Request,
    status_code: int,
    code: str,
    message: str,
    details: list[dict[str, Any]] | None = None,
    headers: dict[str, str] | None = None,
) -> JSONResponse:
    body = {
        "error": {"code": code, "message": message, "details": details},
        "request_id": getattr(request.state, "request_id", None),
    }
    return JSONResponse(status_code=status_code, content=body, headers=headers)


async def app_error_handler(request: Request, exc: AppError) -> JSONResponse:
    return error_response(request, exc.status_code, exc.code, exc.message, headers=exc.headers)


async def http_exception_handler(request: Request, exc: StarletteHTTPException) -> JSONResponse:
    # 接管框架自己抛的 HTTPException：404 路由不存在、405 方法不允许、
    # OAuth2PasswordBearer 没拿到 token 时的 401 等
    code = HTTPStatus(exc.status_code).name
    return error_response(
        request, exc.status_code, code, str(exc.detail), headers=getattr(exc, "headers", None)
    )


async def validation_exception_handler(
    request: Request, exc: RequestValidationError
) -> JSONResponse:
    details = [
        {
            "field": ".".join(str(part) for part in err["loc"]),
            "message": err["msg"],
            "type": err["type"],
        }
        for err in exc.errors()
    ]
    return error_response(request, 422, "VALIDATION_ERROR", "请求参数校验失败", details)


async def unhandled_exception_handler(request: Request, exc: Exception) -> JSONResponse:
    logger.exception("未处理的异常: %s", exc)
    return error_response(request, 500, "INTERNAL_ERROR", "服务器内部错误")


def register_exception_handlers(app: FastAPI) -> None:
    app.add_exception_handler(AppError, app_error_handler)
    app.add_exception_handler(StarletteHTTPException, http_exception_handler)
    app.add_exception_handler(RequestValidationError, validation_exception_handler)
    app.add_exception_handler(Exception, unhandled_exception_handler)
