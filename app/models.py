

class CrewMember:
    id: int
    name: str
    contract_days: int
    availability: int
    role: str

    def __init__(self, id: int, name: str, contract_days: int, availability: int, role: str):
        self.id = id
        self.name = name
        self.contract_days = contract_days
        self.availability = availability
        self.role = role

    def __repr__(self):
        return f"{self.name} is a {self.role} with {self.availability} days available"
