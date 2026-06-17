from fastapi import APIRouter

from app.models.schemas import MatchRequest
from app.services.reconcile import reconcile_data

router = APIRouter()


@router.post("/match")
async def match_records(data: MatchRequest):

    result = await reconcile_data(
        [x.dict() for x in data.source_a],
        [x.dict() for x in data.source_b]
    )

    return result


@router.post("/reconcile")
async def reconciliation_summary(data: MatchRequest):

    result = await reconcile_data(
        [x.dict() for x in data.source_a],
        [x.dict() for x in data.source_b]
    )

    matched = len(result["matched"])
    unmatched = len(result["unmatched"])

    return {
        "total_source_a": len(data.source_a),
        "total_source_b": len(data.source_b),
        "matched": matched,
        "unmatched": unmatched,
        "match_rate": (
            round(
                (matched / len(data.source_a)) * 100,
                2
            )
            if len(data.source_a)
            else 0
        )
    }