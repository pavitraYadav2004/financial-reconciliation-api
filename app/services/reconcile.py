import asyncio

from app.services.matcher import calculate_confidence


async def compare_record(record_a, source_b):

    best_match = None
    best_score = 0

    for record_b in source_b:

        score = calculate_confidence(
            record_a,
            record_b
        )

        if score > best_score:
            best_score = score
            best_match = record_b

    if best_score >= 0.95:
        match_type = "Exact Match"
    elif best_score >= 0.80:
        match_type = "Fuzzy Match"
    else:
        match_type = "No Match"

    return {
        "source_a": record_a,
        "best_match": best_match,
        "confidence": best_score,
        "match_type": match_type
    }


async def reconcile_data(source_a, source_b):

    tasks = [
        compare_record(record, source_b)
        for record in source_a
    ]

    results = await asyncio.gather(*tasks)

    matched = []
    unmatched = []

    for result in results:

        if result["confidence"] >= 0.80:
            matched.append(result)
        else:
            unmatched.append(result)

    return {
        "matched": matched,
        "unmatched": unmatched
    }
# import asyncio

# from app.services.matcher import calculate_confidence


# async def compare_record(record_a, source_b):

#     best_match = None
#     best_score = 0

#     for record_b in source_b:

#         score = calculate_confidence(
#             record_a,
#             record_b
#         )

#         if score > best_score:
#             best_score = score
#             best_match = record_b

#     if best_score >= 0.95:
#         match_type = "Exact Match"
#     elif best_score >= 0.80:
#         match_type = "Fuzzy Match"
#     else:
#         match_type = "No Match"

#     return {
#         "source_a": record_a,
#         "best_match": best_match,
#         "confidence": best_score,
#         "match_type": match_type
#     }


# async def reconcile_data(source_a, source_b):

#     tasks = [
#         compare_record(record, source_b)
#         for record in source_a
#     ]

#     results = await asyncio.gather(*tasks)

#     matched = []
#     unmatched = []

#     for result in results:

#         if result["confidence"] >= 0.80:
#             matched.append(result)
#         else:
#             unmatched.append(result)

#     return {
#         "matched": matched,
#         "unmatched": unmatched
#     }