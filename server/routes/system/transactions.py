# default
# libraries
from all_env import CASSO_SECRET_KEY

# local
from core.conf import app
from fastapi import APIRouter, HTTPException, Request, status
from fastapi_utils.tasks import repeat_every
from models import CassoTransactions

router = APIRouter(
    prefix="/bank",
    tags=["System: Bank API"],
)


@router.post("/casso")
async def wh__receive_transaction(request: Request):
    if request.headers["secure-token"] == CASSO_SECRET_KEY:
        data = await request.json()
        CassoTransactions(

        )
        print(data)
    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="Forbidden"
    )


# Cron job
@app.on_event("startup")
@repeat_every(seconds=3, wait_first=True)
async def confirm_transactions():
    # transaction_history = await get_transaction_history()
    pass
