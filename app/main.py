from typing import List
from fastapi import FastAPI, HTTPException, status

from app.models import CrewMember
from app.service import CrewService
from app.schema import CrewMemberCreate, CrewMemberResponse

app = FastAPI()

crew_members = [
    CrewMember(id=1, name = "John Doe", role = "PILOT",contract_days = 10,availability=8),
    CrewMember(id=2, name = "Jane Doe", role = "PILOT",contract_days = 5,availability=5),
    CrewMember(id=3, name = "Alice", role = "GROUND_STAFF",contract_days = 6,availability=3),
    CrewMember(id=4, name = "Bob", role = "CABIN_CREW",contract_days = 8,availability=7),
    CrewMember(id=5, name = "Charlie", role = "INSTRUCTOR",contract_days = 6,availability=6)]

def get_next_id():
    return max([m.id for m in crew_members], default=0) + 1
 #donne le prochain identifiant à donner


@app.get("/")
def read_root():
    return {"message": "Bienvenue sur l'API AirCrew"}


@app.get("/crew/", response_model=List[CrewMemberResponse])
async def get_all_crew():
    return crew_members


@app.get("/crew/{crew_id}", response_model=CrewMemberResponse)
async def get_crew_member(crew_id: int):
    for c in crew_members :
        if c.id == crew_id :
            return c
    raise HTTPException(status.HTTP_404_NOT_FOUND)


@app.post("/crew/", response_model=CrewMemberResponse)
async def create_crew_member(crew_member: CrewMemberCreate):
    crew = CrewMember(
        id= get_next_id(), #ligne modifiée pour éviter des conflits dans les id : même id donné deux fois si un member précédent a été supprimé 
        name=crew_member.name,
        contract_days=crew_member.contract_days,
        availability=crew_member.availability,
        role=crew_member.role
    )
    crew_members.append(crew)
    return crew


@app.delete("/crew/{crew_id}")
async def delete_crew_member(crew_id: int):
    for c in crew_members:
        if c.id == crew_id:
            crew_members.remove(c)
            return {"message":"Crew member deleted"}
    raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Crew member not found")


@app.put("/crew/{crew_id}/update-availability")
async def update_availability(crew_id: int):
    for c in crew_members :
        if c.id == crew_id :
            return CrewService.update_availability(c)
    raise HTTPException(status.HTTP_404_NOT_FOUND)


@app.get("/crew_stats")
async def get_stats():
    stats = {}
    for c in crew_members:
        if c.role not in stats:
            stats[c.role] = {"total": 0, "available": 0}
        stats[c.role]["total"] += 1
        if c.availability >= 5:
            stats[c.role]["available"] += 1
    return stats

    