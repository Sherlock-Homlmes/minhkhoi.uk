# default
from enum import Enum
from typing import Optional

# libraries
from beanie import Delete, Document, Insert, Link, after_event
from pydantic import BaseModel

# local
from .users import Users


class NotiReceiveEnum(Enum):
    EMAIL = "email"
    ZALO = "zalo"


class ClubSettings(BaseModel):
    intermediary_transactions: bool = False


class Clubs(Document):
    name: str
    description: Optional[str] = None
    avatar: Optional[str] = None
    owner: Link[Users]
    settings: ClubSettings = ClubSettings(
        intermediary_transactions=True
    )

    @after_event(Insert)
    async def create_first_club_member(self):
        await ClubMembers(club=self, member=self.owner).insert()

    @after_event(Delete)
    async def delete_club_members_when_delte_club(self):
        await ClubMembers.find(
            ClubMembers.id == self.id,
            ClubMembers.member == self.owner
        ).delete()


class ClubMembers(Document):
    club: Link[Clubs]
    member: Link[Users]
