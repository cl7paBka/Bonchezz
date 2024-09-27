from fastapi import APIRouter

router = APIRouter()


@router.get("/get/{project_id}")
def get_project():
    return ''


@router.post("/create/{project_id}")
async def create_project():
    return ''


@router.put("/update/{project_id}")
async def update_project():
    return ''
