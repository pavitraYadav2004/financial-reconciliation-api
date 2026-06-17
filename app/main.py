from fastapi import FastAPI
from app.routes.reconciliation import router
import logging

# Financial Reconciliation API v1.0
# Features: fuzzy matching, async processing, confidence scoring

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

app = FastAPI(
    title="Financial Reconciliation API",
    version="1.0.0"
)

app.include_router(router)


@app.on_event("startup")
async def startup_event():
    logging.info("Financial Reconciliation API Started")


@app.get("/")
def home():
    return {
        "message": "Financial Reconciliation API Running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.get("/dashboard")
def dashboard():

    return {
        "application": "Financial Reconciliation API",
        "version": "1.0.0",
        "status": "running",
        "features": [
            "Invoice Matching",
            "Fuzzy Vendor Matching",
            "Confidence Scoring",
            "Async Processing",
            "Reconciliation Summary"
        ]
    }




# from fastapi import FastAPI
# from app.routes.reconciliation import router
# import logging

# logging.basicConfig(
#     level=logging.INFO,
#     format="%(asctime)s - %(levelname)s - %(message)s"
# )

# app = FastAPI(
#     title="Financial Reconciliation API",
#     version="1.0.0"
# )

# app.include_router(router)


# @app.on_event("startup")
# async def startup_event():
#     logging.info("Financial Reconciliation API Started")


# @app.get("/")
# def home():
#     return {
#         "message": "Financial Reconciliation API Running"
#     }


# @app.get("/health")
# def health():
#     return {
#         "status": "healthy"
#     }


# @app.get("/dashboard")
# def dashboard():

#     return {
#         "application": "Financial Reconciliation API",
#         "version": "1.0.0",
#         "status": "running",
#         "features": [
#             "Invoice Matching",
#             "Fuzzy Vendor Matching",
#             "Confidence Scoring",
#             "Async Processing",
#             "Reconciliation Summary"
#         ]
#     }