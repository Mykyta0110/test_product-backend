from fastapi import APIRouter, Depends, HTTPException, logger
from db.session import async_session
from db.models import Product
from .shemas import ShowProduct
from sqlalchemy.ext.asyncio import AsyncSession
from .actions.products import _get_products, _calculate_discount
from db.session import get_db
from typing import List



product_router = APIRouter()






@product_router.get("/", response_model=list[ShowProduct])
async def get_products(db: AsyncSession = Depends(get_db)) -> list[ShowProduct]:
    # Отримуємо список SQLAlchemy об'єктів
    products = await _get_products(session=db)
    
    # Перетворюємо SQLAlchemy об'єкти у Pydantic моделі
    pydantic_products = [
        ShowProduct.from_orm(product) for product in products
    ]
    
    # Обчислюємо знижки (оновлюємо Pydantic моделі)
    updated_products = await _calculate_discount(products=pydantic_products)
    
    # Повертаємо список Pydantic моделей із оновленими даними
    return updated_products
    


