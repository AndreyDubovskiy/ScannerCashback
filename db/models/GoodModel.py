from db.models.BaseModel import BaseModel
from db.models.imports import *
from datetime import datetime

class GoodModel(BaseModel):
    __tablename__ = 'goods'

    id: Mapped[int] = mapped_column(primary_key=True)
    code: Mapped[str] = mapped_column(String(255))
    brend: Mapped[str] = mapped_column(String(255))
    name: Mapped[str] = mapped_column(String(255))
    name_short: Mapped[str] = mapped_column(String(255))
    yurid_name: Mapped[str] = mapped_column(String(255))
    edrpoy: Mapped[str] = mapped_column(String(255), nullable=True)
    rnokpp: Mapped[str] = mapped_column(String(255), nullable=True)
    updated_at = Column(DateTime(timezone=True))
    created_at = Column(DateTime(timezone=True))

    def __init__(self, code: str, brend: str, name: str, name_short: str, yurid_name: str, edrpoy: str, rnokpp: str, updated_at: datetime, created_at: datetime):
        self.code = code
        self.brend = brend
        self.name = name
        self.name_short = name_short
        self.yurid_name = yurid_name
        self.edrpoy = edrpoy
        self.rnokpp = rnokpp
        self.updated_at = updated_at
        self.created_at = created_at
