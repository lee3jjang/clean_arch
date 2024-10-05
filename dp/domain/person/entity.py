from sqlalchemy import Text
from sqlalchemy.orm import Mapped, mapped_column
from dp.base import Base


class PersonEntity(Base):
    __tablename__ = "person"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(Text)
