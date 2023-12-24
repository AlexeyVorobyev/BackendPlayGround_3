import uvicorn
from fastapi import FastAPI
from src.controllers.routers import all_routers
from src.exceptions.middleware import catch_exceptions_middleware

app = FastAPI(
    title="Сервис для ведения учёта чемпионата мира по выкуриванию сигареты"
)


for router in all_routers:
    app.include_router(router)

app.middleware('http')(catch_exceptions_middleware)

if __name__ == "__main__":
    uvicorn.run(app="main:app", reload=True)