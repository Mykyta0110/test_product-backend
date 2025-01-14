from sqlalchemy.ext.asyncio import AsyncSession
from ..shemas import ShowProduct
from db.dals import ProductDAL
from typing import List

async def _get_products(session) -> ShowProduct:
    async with session.begin():
        product_dal = ProductDAL(session)
        products = await product_dal.get_products()
        if products is not None:
            return products

async def _calculate_discount(products: list[ShowProduct]) -> List[ShowProduct]:
    for product in products:
        print(product)
        if product.price > 50:
            product.discount = round(product.price * 0.8, 2)
        else:
            product.discount = 0
    return products