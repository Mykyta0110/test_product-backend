from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, String, Boolean,Integer,Float

Base = declarative_base()



class Product(Base):
    __tablename__= "products"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    discount = Column(Float, nullable=True)
