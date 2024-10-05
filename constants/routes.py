from enum import Enum
from config import BASE_URL


class Routes(str, Enum):
    USERS = 'users'

    def __str__(self) -> str:
        return f"{BASE_URL}/api/{self.value}"
