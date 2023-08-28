from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# base setting
app = FastAPI(
    title="Kpay Wallet API",
    version="0.1.0",
    openapi_url="/openapi.json",
    redoc_url=None,
)
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
