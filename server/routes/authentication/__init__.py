from fastapi import APIRouter

router = APIRouter(
    prefix="/auth",
    tags=["Auth"],
    responses={404: {"description": "Not found"}},
)

from .google_oauth import *
from .auth import *
