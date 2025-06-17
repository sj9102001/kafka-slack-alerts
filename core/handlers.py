from fastapi import Request
from fastapi.responses import JSONResponse
import asyncio
from .exceptions import AppException
from .kafka_producer import send_error_to_kafka

async def app_error_handler(request: Request, exception: AppException):
    asyncio.create_task(send_error_to_kafka(exception, request))
    return JSONResponse(
        status_code=500,
        content={"Error": "Application Error", "detail": exception.message}
    )
