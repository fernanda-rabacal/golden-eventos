from fastapi import Request, Response
from http import HTTPStatus
from api.core.models.responses import BasicResponse, ErrorResponse
from api.core.models.exceptions import *


def core_exception_handler(request: Request, exception: CoreException):
    return Response (
        content = BasicResponse(status = exception.status, message = exception.message).json(),
        status_code = HTTPStatus.BAD_REQUEST
    )

def database_exception_handler(request: Request, exception: DatabaseException):
    return Response (
        content = ErrorResponse (
            status = exception.status, 
            message= exception.message, 
            error=exception.error
        ).json(),
        status_code = HTTPStatus.INTERNAL_SERVER_ERROR
    )

def not_found_exception_handler(request: Request, exception: NotFoundException):
    return Response(
        content = BasicResponse(status = exception.status, message = exception.message).json(),
        status_code = HTTPStatus.NOT_FOUND
    )

def no_content_exception_handler(request: Request, exception: NotFoundException):
    return Response (
        status_code = HTTPStatus.NO_CONTENT
    )