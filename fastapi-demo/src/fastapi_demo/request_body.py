from fastapi import FastAPI
from pydantic import BaseModel, Field, HttpUrl,SecretStr, field_validator, model_validator, ConfigDict
from decimal import Decimal
from datetime import date

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
    category: list[str]=Field(default_factory=lambda:['general'], min_length=1, title="分类", description="属于什么分类")


class Image(BaseModel):
    url: HttpUrl
    name: str
class Row(BaseModel):
    name: str
    price: float
    tags: set[str]=set()
    images: list[Image] | None = None
    attributes: dict[str, str]={}

class Order(BaseModel):
    order_no: str
    items: list[Row]
    remark: str | None = None
    key: SecretStr

class UserCreate(BaseModel):
    username: str
    password: str
    tags: list[str] = []

    @field_validator("username")
    @classmethod
    def username_validate(cls, v:str) -> str:
        if len(v) < 5 and len(v) > 10:
            raise ValueError("姓名必须是5个字及以上，10个字以下")
        return v
    @field_validator("password")
    @classmethod
    def password_rule(cls, v:str) -> str:
        if len(v)<10:
            raise ValueError("不能低于10位数")
        return v
    @field_validator("tags", mode="before")
    @classmethod
    def tags_rule(cls, v) -> list[str]:
        if isinstance(v, str):
            return [t.strip() for t in v.split(",") if t.strip()]
        return v


class Register(BaseModel):
    username: str
    password: str
    password2: str

    @model_validator(mode="after")
    def passwords_match(self):
        if self.password != self.password2:
            raise ValueError("两次密码输入不一致")
        return self

class DateRange(BaseModel):
    start: date
    end: date

    @model_validator(mode="after")
    def check_range(self):
        if self.start > self.end:
            raise ValueError("终止日期不能小于起始日期")
        return self


class Profile(BaseModel):
    model_config = ConfigDict(
        str_strip_whitespace=True,
        extra="forbid",
        validate_by_name=True,
        json_schema_extra={
            "examples":[{"nick_name": "张三", "bio": "fs"}] 
        }
    )
    nick_name: str = Field(alias="nickName", min_length=2)
    bio: str=""

class Item2(BaseModel):
    name: str
    description: str | None = None
    price: float
    tags: list[str] = []


class ItemUpdate(BaseModel):
    # 所有字段都可选，用于 PATCH
    name: str | None = None
    description: str | None = None
    price: float | None = None
    tags: list[str] | None = None


items: dict[int, Item] = {
    1: Item(name="键盘", description=None, price=399, tags=["外设"]),
}


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

@app.post('/orders')
async def get_order_list(
    order: Order
):
    total = sum(item.price for item in order.items)
    return {"order_no": order.order_no, "count": len(order.items), "total": total, "key": order.key }

@app.post("/user")
async def get_user(user: UserCreate):
    return user

@app.post('/register')
async def register(user: Register):
    return {"username": user.username}

@app.post("/pick_date")
async def select_date(date: DateRange):
    return date

@app.post('/profile')
async def profile(user: Profile):
    return user.model_dump()

@app.patch("/items/{item_id}")
async def patch_item(item_id: int, item_update: ItemUpdate) -> Item:
    stored = items[item_id]
    update_data = item_update.model_dump(exclude_none=True)  # 只包含客户端显式传入的字段
    updated = stored.model_copy(update=update_data)
    items[item_id] = updated
    return updated