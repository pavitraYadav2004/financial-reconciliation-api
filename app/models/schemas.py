from pydantic import BaseModel
from typing import List


class Invoice(BaseModel):
    invoice_id: str
    vendor_name: str
    amount: float
    currency: str
    invoice_date: str
    payment_status: str


class MatchRequest(BaseModel):
    source_a: List[Invoice]
    source_b: List[Invoice]