from app.services.matcher import calculate_confidence


def test_exact_match():

    a = {
        "invoice_id": "INV001",
        "vendor_name": "Amazon Web Services",
        "amount": 1000,
        "invoice_date": "2026-06-01"
    }

    b = {
        "invoice_id": "INV001",
        "vendor_name": "Amazon Web Services",
        "amount": 1000,
        "invoice_date": "2026-06-01"
    }

    score = calculate_confidence(a, b)

    assert score > 0.9