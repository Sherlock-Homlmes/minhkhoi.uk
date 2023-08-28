
# default
from typing import Optional

from bson.objectid import ObjectId

# libraries
from fastapi import APIRouter, Depends, status

# local
from models import Users, PaymentRequests, ConfirmPaymentRequests, CassoTransactions
from other_modules.json_modules import mongodb_to_json
from other_modules.time_modules import str_to_time
from pydantic import BaseModel
from routes.authentication import auth_handler

router = APIRouter(
    prefix="/matches",
    tags=["Matches"],
    responses={404: {"description": "Not found"}},
)


class PostMatchPayload(BaseModel):
    club: str
    price: int
    place: str
    time: str
    created_by: Users = None


# MATCHES
@router.get("/", dependencies=[Depends(auth_handler.auth_wrapper)])
async def get_list_matches(
    match_club_id: Optional[str] = None,
    user: Users = Depends(auth_handler.auth_wrapper)
):
    member_matches = await MatchMembers.find(
        MatchMembers.member.id == ObjectId(user["id"]),
        fetch_links=True
    ).to_list()
    member_matches = [x.match for x in member_matches]
    if match_club_id:
        for member_match in member_matches:
            if member_match.id == match_club_id:
                return member_match
        return {}
    return mongodb_to_json(member_matches)


@router.post("/", dependencies=[Depends(auth_handler.auth_wrapper)])
async def create_match(
    payload: PostMatchPayload,
    user: Users = Depends(auth_handler.auth_wrapper)
):
    payload.time = str_to_time(payload.time)
    payload.club = ObjectId(payload.club)
    payload.created_by = await Users.get(user["id"])
    payload = payload.dict()

    match = await Matches(**payload).insert()
    return {"id": mongodb_to_json(match.id)}


@router.delete(
    "/{match_id}",
    dependencies=[Depends(auth_handler.auth_wrapper)],
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_match(
    match_id: str,
    user: Users = Depends(auth_handler.auth_wrapper)
):
    match = await Matches.find_one(
        Matches.id == ObjectId(match_id),
        Matches.created_by.id == ObjectId(user["id"])
    )
    if match:
        await match.delete()
        return
    return status.HTTP_403_FORBIDDEN
