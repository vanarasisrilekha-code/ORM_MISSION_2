"""One shared SQLAlchemy declarative base for ALL ORM models."""
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    """Collects ORM models and their SQLAlchemy table metadata."""
    pass
