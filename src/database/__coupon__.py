from pydantic import BaseModel
from sqlalchemy import Column, String, inspect, Integer

from .__conn__ import *

class CouponTable(Base): # 쿠폰 테이블
    __tablename__ = 'coupon' #테이블 이름
    restaurant_name = Column(String(50), primary_key=True,nullable=False) # 식당 이름
    user_id = Column(String(50), primary_key=True, nullable=False) # 유저 아이디
    coupon_num = Column(Integer(10), nullable=False,) # 쿠폰도장 개수

class Coupon(BaseModel): # 쿠폰
    restaurant_name: str
    user_id: int
    coupon_num: str


# CouponTable 테이블 생성
# 이미 생성되어있는지 확인 후 생성
# <class 'sqlalchemy.engine.base.Connection'>


inspector = inspect(conn.engineData())
if not inspector.has_table('user'):
    CouponTable.__table__.create(bind=conn.engineData())
    print("테이블 생성 완료")
else:
    print("이미 테이블이 존재합니다.")