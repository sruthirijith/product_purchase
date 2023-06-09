from typing import Optional, Text

from pydantic import BaseModel, EmailStr, Field


class UsersBase(BaseModel):
    full_name      : Optional[str]
    email          : Optional[EmailStr]
    password       : Optional[str]
    phone_number   : Optional[str]
    role_id        : int


class login(BaseModel):
   email     : Optional[EmailStr]
   password  : Optional[str]

class add_pin(BaseModel):
    pin         : str
    reenter_pin : str   

class add_wallet(BaseModel):
    pin    : int
    amount : int    

class product_purchase(BaseModel):
    product_name : str
    quantity   : int
    

class add_product(BaseModel):
    product_name   : str
    product_price  : int
    product_stock  : int
    
    
class purchase_details(BaseModel):
    users_id        : int
    email           : str
    product_name    : str 
    quantity        : int 
    total_price     : int

class membership(BaseModel):
    plan       : str
    pin        : int   
   
    
     




