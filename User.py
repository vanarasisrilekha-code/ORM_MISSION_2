"""User = parent table. One user can own many missions."""
from __future__ import annotations
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from base import Base

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(120), nullable=False)
    email: Mapped[str] = mapped_column(String(254), unique=True, index=True, nullable=False)

    # back_populates wires User.missions <-> Mission.user
    missions: Mapped[list["Mission"]] = relationship(back_populates="user")

    def __repr__(self) -> str:
        return f"User(id={self.id}, name={self.name!r})"
