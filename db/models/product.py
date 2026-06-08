from db.base import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy import String

class Product(Base):
    __tablename__ = "products"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    price: Mapped[int] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=True)
    images: Mapped[list[str]] = mapped_column(ARRAY(String), default=list, nullable=True)
    color: Mapped[str] = mapped_column(nullable=True)
    size: Mapped[str] = mapped_column(nullable=True)