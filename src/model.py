from dataclasses import dataclass

@dataclass
class Customer:
    id: int
    name: str
    last_name: str
    email: str
