from fastapi import FastAPI
from enum import Enum

app=FastAPI()


class AvailableFoodItems(str,Enum):
    indian='indian'
    american='american'
    italian='italian'


food_items={
    'indian':['Samosa','Dosa','biryani'],
    'american':['pizza','burger','fries'],
    'italian':['Ravioli','pizza','pasta'],
}

valid_cuisine=food_items.keys()

# @app.get('/get_items/{cuisine}')
# async def get_items(cuisine):
#     # return food_items[cuisine] 
#     if cuisine not in food_items:
#         return f'{cuisine} not found. Valid Cuisines are {valid_cuisine}'
    
#     return food_items.get(cuisine)


@app.get('/get_items/{cuisine}')
async def get_items(cuisine: AvailableFoodItems):
    return food_items.get(cuisine)


coupon_code={
    1: '10%',
    2: '20%',
    3: '30%',
}
    

@app.get('/get_items/{code}')
async def get_items(code: int):
    return {'coupon_code': coupon_code.get(code)}