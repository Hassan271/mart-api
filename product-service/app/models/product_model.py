from sqlmodel import SQLModel, Field, Relationship


# 1--------copy todo app Table and past here   --------------
class Product(SQLModel, table=True):
    
    # 2- id, name ... each product features  ---------------------
    # 3-create CRUD of this table   ------------------------  product-service\app\crud
    id: int | None = Field(default=None, primary_key=True)
    name: str
    description: str
    price: float
    expiry: str | None = None
    brand: str | None = None
    weight: float | None = None
    category: str # It shall be pre defined by Platform
    sku: str | None = None
    rating: list["ProductRating"] = Relationship(back_populates="product")
    # image: str # Multiple | URL Not Media | One to Manu Relationship
    # quantity: int | None = None # Shall it be managed by Inventory Microservice
    # color: str | None = None # One to Manu Relationship
    # rating: float | None = None # One to Manu Relationship
    
    
class ProductRating(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    product_id: int = Field(foreign_key="product.id")
    rating: int
    review: str | None = None
    product = Relationship(back_populates="rating")
    
    # user_id: int # One to Manu Relationship
    

#  for update product from   product-service\app\crud\product_crud.py   
class ProductUpdate(SQLModel):
    name: str | None = None
    description: str | None = None
    price: float | None = None
    expiry: str | None = None
    brand: str | None = None
    weight: float | None = None
    category: str | None = None
    sku: str | None = None
