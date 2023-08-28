# default
from enum import Enum
from typing import Optional

# libraries
from beanie import Document, Link

# local
from .users import Users


class TransactionStatusEnum(Enum):
    PAID = "paid"
    UNPAID = "unpaid"
    REJECT = "reject"


class PaymentRequests(Document):
    created_by: Link[Users]
    to: Link[Users]
    title: str
    description: Optional[str] = None
    price: int
    intermediary: bool = False


class Transactions(Document):
    payment_request: Link[PaymentRequests]
    user: Link[Users]
    status: TransactionStatusEnum


class ConfirmPaymentRequests(Document):
    payment_request: Link[PaymentRequests]
    created_by: Link[Users]
    to: Link[Users]


class CassoTransactions(Transactions):
    casso_transaction_id: str
