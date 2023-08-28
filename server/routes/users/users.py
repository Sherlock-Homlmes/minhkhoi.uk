# default

# libraries
from fastapi import APIRouter, Depends
from models import Users

# local
from routes.authentication import auth_handler

router = APIRouter(
    prefix="/users",
    tags=["Users"],
    responses={404: {"description": "Not found"}},
)

@router.get("/self", dependencies=[Depends(auth_handler.auth_wrapper)])
def protected(user: Users = Depends(auth_handler.auth_wrapper)):
    return user



# @router.get("/settings/self")
# async def get_user_setting(user: Users = Depends(auth_handler.auth_wrapper)):
#     user_setting = await UserSettings.find_one(
#         UserSettings.user.id == ObjectId(user["id"])
#     )
#     del user_setting.user
#     return user_setting

# @router.patch("/settings/self", status_code=204)
# async def update_user_setting(
#     user_setting: UserSetting, user: Users = Depends(auth_handler.auth_wrapper)
# ):
#     old_user_setting = await UserSettings.find_one(
#         UserSettings.user.id == ObjectId(user["id"])
#     )
#     old_user_setting.update_value(**user_setting)
#     await old_user_setting.save()
#     return

