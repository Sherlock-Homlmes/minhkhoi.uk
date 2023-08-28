# default
from bson.objectid import ObjectId

# libraries
from fastapi import APIRouter, Depends, HTTPException, status
from models import ClubMembers, Clubs, Users
from other_modules.json_modules import mongodb_to_json

# local
from routes.authentication import auth_handler

router = APIRouter(
    prefix="/clubs",
    tags=["Clubs"],
    responses={404: {"description": "Not found"}},
)


# CLUB
@router.get("/", dependencies=[Depends(auth_handler.auth_wrapper)])
async def get_list_clubs():
    return mongodb_to_json(await Clubs.find().to_list())


@router.get("/{club_id}", dependencies=[Depends(auth_handler.auth_wrapper)])
async def get_club(club_id: str):
    club = await Clubs.get(club_id)
    return club.json()


@router.post("/", dependencies=[Depends(auth_handler.auth_wrapper)])
async def create_club(
    name: str,
    description: str,
    user: Users = Depends(auth_handler.auth_wrapper)
):
    club = await Clubs(
        name=name,
        description=description,
        # avatar = avatar,
        owner=user
    ).insert()
    return {"id": mongodb_to_json(club.id)}


@router.patch(
    "/{club_id}",
    dependencies=[Depends(auth_handler.auth_wrapper)],
    status_code=status.HTTP_204_NO_CONTENT
)
async def update_club(
    club_id: str,
    payload: dict,
    user: Users = Depends(auth_handler.auth_wrapper)
):
    club = await Clubs.find_one(
        Clubs.id == ObjectId(club_id),
        Clubs.owner.id == user["id"]
    )
    if club:
        club.update({"$set": payload})
        await club.save()
        return
    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="Forbidden"
    )


@router.delete(
    "/{club_id}",
    dependencies=[Depends(auth_handler.auth_wrapper)],
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_club(
    club_id: str,
    user: Users = Depends(auth_handler.auth_wrapper)
):
    club = await Clubs.find_one(
        Clubs.id == ObjectId(club_id),
        Clubs.owner.id == ObjectId(user["id"]) 
    )
    if club:
        await club.delete()
        return
    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="Forbidden"
    )


# CLUB MEMBER
@router.get(
    "/{club_id}/members",
    dependencies=[Depends(auth_handler.auth_wrapper)],
    status_code=status.HTTP_200_OK
)
async def list_club_members(
    club_id: str,
    user: Users = Depends(auth_handler.auth_wrapper)
):
    club = await Clubs.get(club_id)
    is_member_of_club = await ClubMembers.find_one(
        ClubMembers.club.id == club.id,
        ClubMembers.member.id == ObjectId(user["id"])
    )
    if is_member_of_club:
        members = await ClubMembers.find(
            ClubMembers.club.id == club.id,
        ).to_list()
        return [member.json() for member in members]
    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="Forbidden"
    )


@router.post(
    "/{club_id}/members",
    dependencies=[Depends(auth_handler.auth_wrapper)],
    status_code=status.HTTP_204_NO_CONTENT
)
async def add_new_member_to_club(
    club_id: str,
    member_id: str,
    user: Users = Depends(auth_handler.auth_wrapper)
):
    club = await Clubs.find_one(
        Clubs.id == ObjectId(club_id),
        Clubs.owner.id == ObjectId(user["id"])
    )
    if club:
        is_member_exist = await ClubMembers.find_one(
            ClubMembers.club.id == club.id,
            ClubMembers.member.id == ObjectId(member_id)
        )
        if is_member_exist:
            raise HTTPException(
                status_code=status.HTTP_406_NOT_ACCEPTABLE,
                detail="Member already exist"
            )
        member = await Users.get(member_id)
        if not member:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Member not exist"
            )
        await ClubMembers(
            club=club,
            member=member
        ).insert()
        return
    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="Forbidden"
    )


@router.delete(
    "/{club_id}/members/{member_id}",
    dependencies=[Depends(auth_handler.auth_wrapper)],
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_club_member(
    club_id: str,
    member_id: str,
    user: Users = Depends(auth_handler.auth_wrapper)
):
    club = await Clubs.find_one(
        Clubs.id == ObjectId(club_id),
        Clubs.owner.id == ObjectId(user["id"])
    )
    if club:
        await ClubMembers.find_one(
            ClubMembers.club.id == club.id,
            ClubMembers.member.id == ObjectId(member_id)
        ).delete()
        return
    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="Forbidden"
    )
