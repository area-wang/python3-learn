from fastapi import FastAPI
from pydantic import BaseModel, Field
from decimal import Decimal

app=FastAPI()

class Item(BaseModel):
    name:str
    description:str|None = None
    price:float
    tax: float | None = None



class Product(BaseModel):
    name: str = Field(min_length=5, max_length=15, description="商品名称")
    sku: str = Field(pattern=r"^[A-Z]{3}-\d{4}$", examples=["KBD-0001"])
    price: Decimal = Field(gt=0, max_digits=8, decimal_places=2)
    stock: int = Field(default=0, ge=0)
    discount: float = Field(default=1.0, gt=0, le=1, description="折扣")

@app.post('/items')
async def create_item(item: Item):
    data = item.model_dump()
    print(item)         
    print(item.dict())                     # name='键盘' price=199.0 tags=[]
    print(item.model_dump())                 # {'name': '键盘', 'price': 199.0, 'tags': []}
    print(item.model_dump_json()) 
    if item.tax is not None:
        data["price_with_tax"] = item.price + item.tax
    return data

@app.post('/products')
async def get_prod(products: Product):
    data = products.model_dump()
    return data