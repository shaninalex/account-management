from dataclasses import dataclass
from .descriptors import EmailField


@dataclass
class Employee:
    id: int
    email: EmailField
    username: str
