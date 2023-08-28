# default
from typing import Optional, List
from enum import Enum

# libraries
from beanie import Document
from pydantic import BaseModel, EmailStr


class NotiReceiveEnum(Enum):
    EMAIL = "email"
    ZALO = "zalo"


class UserSettings(BaseModel):
    noti_receives: List[NotiReceiveEnum]


class Users(Document):
    name: str
    nick: Optional[str] = None
    email: EmailStr = None
    phone_number: Optional[str] = None
    avatar: Optional[str] = None
    settings: UserSettings = UserSettings(
        noti_receives=[NotiReceiveEnum.EMAIL, NotiReceiveEnum.ZALO]
    )

    # function
    def get_info(self):
        return {
            "id": self.id,
            "name": self.name,
            "nick": self.nick,
            "email": self.email,
            "avatar": self.avatar,
            "settings": self.settings,
        }
