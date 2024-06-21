from fastapi import APIRouter

router = APIRouter()

@router.get("/items")
async def read_items():
    return [{"item_id": 1, "name": "item1"}, {"item_id": 2, "name": "item2"}]

@router.get("/users")
async def read_users():
    return [{"user_id": 1, "name": "user1"}, {"user_id": 2, "name": "user2"}]