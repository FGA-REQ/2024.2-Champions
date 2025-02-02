from fastapi import APIRouter, status

router = APIRouter(
  prefix='/users',
  tags=['User Routes']
)

@router.get("/", status_code=status.HTTP_200_OK)
def get():
  return {'msg' : "Hello from Users Router!"}