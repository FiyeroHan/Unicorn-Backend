from pydantic import BaseModel
from sqlalchemy import Column, String, inspect, Integer,ForeignKey, default

from .__conn__ import * 
from .__shop__ import *

class ProductTable(Base): # 상품 테이블
    __tablename__ = 'product' #테이블 이름
    shop_name = Column(String(50),ForeignKey("shop.name"),  primary_key=True, nullable=False)
    product_name = Column(String(50), nullable=False) # 이름
    product_id = Column(String(50), primary_key=True, nullable=False) # 상품 아이디
    price = Column(String(50), nullable=False) # 가격
    product_Description = Column(String(50), nullable=False) # 상세설명
    spicy_level = Column(String(50), default = 0) # 맵기 정도

class Product(BaseModel): # 유저
    shop_name: str
    product_name: str
    product_id: str
    price: str
    product_Description: str
    spicy_level: str


# UserTable 테이블 생성
# 이미 생성되어있는지 확인 후 생성
# <class 'sqlalchemy.engine.base.Connection'>


inspector = inspect(conn.engineData())
if not inspector.has_table('user'):
    UserTable.__table__.create(bind=conn.engineData())
    print("테이블 생성 완료")
else:
    print("이미 테이블이 존재합니다.")