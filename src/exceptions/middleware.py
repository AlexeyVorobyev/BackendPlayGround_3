from traceback import print_exception
from fastapi.exceptions import ResponseValidationError
from starlette.requests import Request
from starlette.responses import JSONResponse


async def catch_exceptions_middleware(request: Request, call_next):
    try:
        return await call_next(request)
    except Exception as exception:
        print_exception(exception)
        if type(exception) == ResponseValidationError:
            exception: ResponseValidationError
            return JSONResponse(exception.errors(), status_code=422)
        return JSONResponse(str(exception), status_code=400)
