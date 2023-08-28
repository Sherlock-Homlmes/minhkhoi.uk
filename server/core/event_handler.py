# default
import beanie
from models import (
    CassoTransactions,
    ClubMembers,
    Clubs,
    ConfirmPaymentRequests,
    Matches,
    MatchMembers,
    PaymentRequests,
    Transactions,
    Users,
)

# local
from .conf import app
from .mongodb.async_db import client


@app.on_event("startup")
async def startup():
    await beanie.init_beanie(
        database=client.banhda_project,
        document_models=[
            Users,
            Clubs, ClubMembers,
            Matches, MatchMembers,
            PaymentRequests, Transactions, ConfirmPaymentRequests, CassoTransactions
        ],
    )

    print("Start up done")
