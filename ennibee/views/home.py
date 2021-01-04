from fastapi.responses import RedirectResponse
from fastapi.requests import Request
from ennibee.seetings import template
from fastapi import APIRouter
from ennibee.models.docs import Docs
router = APIRouter()


@router.get("/docs", include_in_schema=False)
def docs():
    return RedirectResponse("/api/v1/docs", status_code=303)

@router.get("/", response_model=Docs, tags=["home"], description="the default route for ennibee")
def home(request:Request):
    return template("index.html", {"request":request})