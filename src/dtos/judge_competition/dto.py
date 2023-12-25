
from pydantic import BaseModel


class JudgeCompetitionAddDTO(BaseModel):
    competition_id: str
    judge_id: str
