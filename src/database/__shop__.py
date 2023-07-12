from pydantic import BaseModel
from sqlalchemy import Column, String, inspect

from .__conn__ import *

class ShopTable(Base): # 가게 테이블
    __tablename__ = 'shop' #테이블 이름
    shop_name = Column(String(50), nullable=False) # 이름
    shop_id = Column(String(50), primary_key=True, nullable=False) # 아이디    


class Shop(BaseModel):
    shop_name: str
    shop_id: str



# UserTable 테이블 생성
# 이미 생성되어있는지 확인 후 생성
# <class 'sqlalchemy.engine.base.Connection'>


inspector = inspect(conn.engineData())
if not inspector.has_table('user'):
    ShopTable.__table__.create(bind=conn.engineData())
    print("테이블 생성 완료")
else:
    print("이미 테이블이 존재합니다.")