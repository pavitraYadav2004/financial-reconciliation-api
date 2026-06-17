import re
from rapidfuzz import fuzz


vendor_aliases = {
    "aws": "amazon web services",
    "oracle corp": "oracle corporation",
    "google cloud": "google cloud platform",
    "ibm": "ibm corporation",
    "microsoft azure llc": "microsoft azure"
}


def normalize(text: str) -> str:
    text = text.lower().strip()

    if text in vendor_aliases:
        text = vendor_aliases[text]

    return re.sub(r"[^a-z0-9]", "", text)


def calculate_confidence(a, b):

    invoice_score = (
        1
        if normalize(a["invoice_id"]) ==
        normalize(b["invoice_id"])
        else 0
    )

    vendor_score = (
        fuzz.ratio(
            normalize(a["vendor_name"]),
            normalize(b["vendor_name"])
        ) / 100
    )

    amount_score = (
        1
        if abs(
            float(a["amount"]) -
            float(b["amount"])
        ) <= 5
        else 0
    )

    date_score = (
        1
        if a["invoice_date"] ==
        b["invoice_date"]
        else 0
    )

    confidence = (
        invoice_score * 0.40 +
        vendor_score * 0.30 +
        amount_score * 0.20 +
        date_score * 0.10
    )

    return round(confidence, 2)