from sqlalchemy import select
from typing import List, Optional
from db.controllers.TemplateController import Controller  # Используем асинхронный контроллер
from db.models.GoodModel import GoodModel
from sqlalchemy.ext.asyncio import AsyncSession

class GoodsController(Controller):
    async def get_all(self) -> List[GoodModel]:
        async with self.async_session() as session:
            query = select(GoodModel)
            result = await session.scalars(query)
            res: List[GoodModel] = result.all()
        return res

    async def get_by(
        self,
        id: Optional[int] = None,
        code: Optional[str] = None,
        brend: Optional[str] = None,
        name: Optional[str] = None,
        name_short: Optional[str] = None,
        yurid_name: Optional[str] = None,
        edrpoy: Optional[str] = None,
        rnokpp: Optional[str] = None,
        updated_at_start = None,
        updated_at_end = None,
        created_at_start = None,
        created_at_end = None
    ) -> List[GoodModel]:
        async with self.async_session() as session:
            query = select(GoodModel)
            if id is not None:
                query = query.where(GoodModel.id == id)
            if code is not None:
                query = query.where(GoodModel.code == code)
            if brend is not None:
                query = query.where(GoodModel.brend.contains(brend))
            if name is not None:
                query = query.where(GoodModel.name.contains(name))
            if name_short is not None:
                query = query.where(GoodModel.name_short == name_short)
            if yurid_name is not None:
                query = query.where(GoodModel.yurid_name == yurid_name)
            if edrpoy is not None:
                query = query.where(GoodModel.edrpoy == edrpoy)
            if rnokpp is not None:
                query = query.where(GoodModel.rnokpp == rnokpp)
            if updated_at_start is not None:
                query = query.where(GoodModel.updated_at >= updated_at_start)
            if updated_at_end is not None:
                query = query.where(GoodModel.updated_at <= updated_at_end)
            if created_at_start is not None:
                query = query.where(GoodModel.created_at >= created_at_start)
            if created_at_end is not None:
                query = query.where(GoodModel.created_at <= created_at_end)

            result = await session.scalars(query)
            res: List[GoodModel] = result.all()
        return res

    async def create(
        self, code: str, brend: str, name: str, name_short: str,
        yurid_name: str, edrpoy: str, rnokpp: str, updated_at, created_at
    ) -> GoodModel:
        async with self.async_session() as session:
            async with session.begin():
                tmp = GoodModel(
                    code=code, brend=brend, name=name, name_short=name_short,
                    yurid_name=yurid_name, edrpoy=edrpoy, rnokpp=rnokpp,
                    updated_at=updated_at, created_at=created_at
                )
                session.add(tmp)
                await session.commit()
                await session.refresh(tmp)
        return tmp

    async def delete(self, id: int) -> Optional[GoodModel]:
        async with self.async_session() as session:
            async with session.begin():
                query = select(GoodModel).where(GoodModel.id == id)
                result = await session.scalars(query)
                tmp: Optional[GoodModel] = result.first()
                if tmp:
                    await session.delete(tmp)
                    await session.commit()
        return tmp
