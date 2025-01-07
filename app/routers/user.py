from fastapi import APIRouter

router =APIRouter(prefix="/user", tags=["user"])
@router.get("/all_users")
async def get_all_users():
    pass

@router.get("/user_id")
async def get_user_by_id():
    pass

@router.post("create")
async def creaty_user():
    pass

@router.put("/update_task")
async def update_user():
    pass

@router.delete("/delete")
async def delete_user():
    pass