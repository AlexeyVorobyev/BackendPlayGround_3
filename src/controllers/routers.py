from src.controllers.judge.controller import router as router_judge
from src.swagger.swagger import router as router_swagger

all_routers = [
    router_judge,
    router_swagger
]
