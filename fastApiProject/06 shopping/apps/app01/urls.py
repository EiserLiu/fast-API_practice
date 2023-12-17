from fastapi import APIRouter
import uvicorn

shop = APIRouter()


@shop.get('/food')
async def shop_food():
    return {"shop": "food"}


@shop.get('/bed')
async def shop_bed():
    return {"shop": "bed"}


if __name__ == '__main__':
    uvicorn.run("03 fastAPI quickstart:app", port=8080, debug=True, reload=True)