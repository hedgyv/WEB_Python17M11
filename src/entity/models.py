from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, CheckConstraint
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.sql.sqltypes import Date
from datetime import date

class Base(DeclarativeBase):
    pass


class Contact(Base):
    __tablename__ = "contacts"
    id: Mapped[int] = mapped_column(primary_key=True)
    f_name: Mapped[str] = mapped_column(String(50), index=True)
    l_name: Mapped[str] = mapped_column(String(50), index=True)
    email: Mapped[str] = mapped_column(String(100))
    phone: Mapped[str] = mapped_column(String(25))
    birthday: Mapped[date] = mapped_column(Date, nullable=False)
    additional_data: Mapped[str] = mapped_column(default=False)
    
    __table_args__ = (
        CheckConstraint("phone ~ E'^[\\d\\+\\(\\)]+$'"),
    )