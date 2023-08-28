import datetime
from typing import Optional

# libraries
from beanie import Delete, Document, Insert, Link, after_event, before_event

from .clubs import Clubs

# local
from .users import Users
from .transactions import PaymentRequests


class Matches(Document):
    created_by: Link[Users]
    club: Link[Clubs]
    title: Optional[str] = None
    description: Optional[str] = None
    price: int
    place: str
    time: datetime.datetime

    @before_event(Insert)
    async def fix_title(self):
        if not self.title:
            self.title = f"Match in {self.place}"

    @after_event(Insert)
    async def create_first_match_member(self):
        await MatchMembers(match=self, member=self.created_by).insert()

    @after_event(Delete)
    async def delete_match_members_when_delete_club(self):
        await MatchMembers.find(
            MatchMembers.match.id == self.id,
        ).delete()
    
    async def create_payment_requests(
        self,
        intermediary: Optional[bool] = None
    ):
        match_members = await MatchMembers.find(
            MatchMembers.match.id == self.id,
        ).to_list()
        member_match_count = await MatchMembers.find(
            MatchMembers.match == self
        ).count()
        if intermediary is None:
            self = self.club.settings.intermediary
            
        await PaymentRequests.insert_many(
            [
                PaymentRequests(
                    created_by=self.created_by,
                    to=match_member,
                    title=f"Request payment for {self.title}",
                    price=self.price / member_match_count,
                    intermediary=intermediary,
                )
                for match_member in match_members
            ]
        )


class MatchMembers(Document):
    match: Link[Matches]
    member: Link[Users]
