from src.controllers.judge.controller import router as router_judge
from src.controllers.stadium.controller import router as router_stadium
from src.controllers.sport.controller import router as router_sport
from src.controllers.competition.controller import router as router_competition
from src.swagger.swagger import router as router_swagger

all_routers = [
    router_judge,
    router_sport,
    router_stadium,
    router_competition,
    router_swagger
]
