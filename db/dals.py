from db.models import Product
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import update, and_, select
class ProductDAL:
    def __init__(self, db_session:AsyncSession):
        self.db_session = db_session

    async def get_products(self):
        query = select(Product)
        res = await self.db_session.execute(query)
        products = res.scalars().all()
        if products is not None:
            return products
