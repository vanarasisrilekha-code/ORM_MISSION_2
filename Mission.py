"""Mission = child table. Each mission belongs to one existing user."""
from __future__ import annotations
from sqlalchemy import CheckConstraint, ForeignKey, Index, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from base import Base

class Mission(Base):
    __tablename__ = "missions"
    __table_args__ = (
        CheckConstraint("points >= 0", name="ck_missions_nonnegative_points"),
        CheckConstraint("status IN ('open', 'in_progress', 'done')", name="ck_missions_status"),
        Index("idx_missions_user_status", "user_id", "status"),
    )

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="RESTRICT"), nullable=False)
    title: Mapped[str] = mapped_column(String(150), nullable=False)
    points: Mapped[int] = mapped_column(default=0, nullable=False)
    status: Mapped[str] = mapped_column(String(20), default="open", nullable=False)

    user: Mapped["User"] = relationship(back_populates="missions")

    def __repr__(self) -> str:
        return f"Mission(id={self.id}, title={self.title!r}, status={self.status!r})"
