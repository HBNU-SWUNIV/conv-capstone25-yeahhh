from sqlalchemy import Column, Integer, String, Float, Date, Enum
from sqlalchemy.sql import func
from sqlalchemy.types import DateTime
from app.db.session import Base

class Asset(Base):
    __tablename__ = "assets"

    id = Column(Integer, primary_key=True, index=True)
    asset_id = Column(String, unique=True, index=True, nullable=False)
    asset_type = Column(String, nullable=False)
    asset_category = Column(String, nullable=False)
    brand = Column(String, nullable=False)
    model = Column(String, nullable=False)
    serial_number = Column(String, nullable=False)
    purchase_date = Column(Date, nullable=True)
    supplier = Column(String, nullable=True)
    purchase_order_no = Column(String, nullable=True)
    warranty_start_date = Column(Date, nullable=True)
    warranty_end_date = Column(Date, nullable=True)
    location = Column(String, nullable=True)
    campus = Column(String, nullable=True)
    department = Column(String, nullable=True)
    custodian = Column(String, nullable=True)
    status = Column(String, nullable=False, default="available")
    book_value = Column(Float, nullable=True)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
    )
