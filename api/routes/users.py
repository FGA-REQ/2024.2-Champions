from fastapi import APIRouter

router = APIRouter(
  prefix='/users',
  tags=['User Routes']
)

@router.get("/")
def get():
  return {'msg' : "Hello from Users Router!"}