from fastapi import APIRouter


router = APIRouter()


@router.post("/register")
async def register_user():
    return {"register": "user"}


@router.post("/login")
async def login():
    return {"login": "user"}

