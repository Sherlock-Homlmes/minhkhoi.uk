# fastapi
from fastapi.responses import JSONResponse

# default
from typing import Optional

# local
from . import router
from .google_oauth import GoogleOauth2


@router.get("/oauth-link")
async def get_oauth_link(
    google_link: Optional[bool] = False,
):
    response = {}
    if google_link:
        response["google_link"] = GoogleOauth2().get_oauth_url()

    return JSONResponse(response, status_code=200)
