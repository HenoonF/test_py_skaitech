
from app.models import CrewMember


availability_rate = {"PILOT":1,"GROUND_STAFF":0.5,"CABIN_CREW":1.5} #nombre de jour(s) de disponibilité perdu par jour de travail

class CrewService:

    @staticmethod
    def update_availability(crew_member: CrewMember): #changement du type de la variable crew_members étant donné son nom
        if crew_member.availability >= 5:
            new_availability = crew_member.availability - availability_rate.get(crew_member.role, 0)
            crew_member.availability = new_availability
        crew_member.contract_days -=1
        crew_member.availability = min(crew_member.contract_days,crew_member.availability)
        return {"message": "Availability updated", "new_availability": crew_member.availability}
