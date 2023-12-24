from fastapi import APIRouter
from fastapi.openapi.docs import get_swagger_ui_html

router = APIRouter(
    prefix="/swagger",
    tags=["swagger"],
)


@router.get("")
def read_docs():
    return get_swagger_ui_html(openapi_url="/openapi.json", title="Сервис для ведения учёта чемпионата мира по выкуриванию сигареты")
