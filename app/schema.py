

from pydantic import BaseModel


class CrewMemberBase(BaseModel):
    name: str
    contract_days: int
    availability: int
    role: str


class CrewMemberCreate(CrewMemberBase):
    pass


class CrewMemberResponse(CrewMemberBase):
    id: int
    class Config:
        from_attributes = True
