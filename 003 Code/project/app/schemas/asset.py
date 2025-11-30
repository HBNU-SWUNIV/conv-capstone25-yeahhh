from pydantic import BaseModel
from typing import Optional
from datetime import date

class AssetBase(BaseModel):
    asset_type: str
    asset_category: str
    brand: str
    model: str
    serial_number: str
    purchase_date: Optional[date] = None
    supplier: Optional[str] = None
    purchase_order_no: Optional[str] = None
    warranty_start_date: Optional[date] = None
    warranty_end_date: Optional[date] = None
    location: Optional[str] = None
    campus: Optional[str] = None
    department: Optional[str] = None
    custodian: Optional[str] = None
    status: Optional[str] = "available"
    book_value: Optional[float] = None


class AssetCreate(AssetBase):
    asset_id: str


class AssetUpdate(BaseModel):
    asset_type: Optional[str] = None
    asset_category: Optional[str] = None
    brand: Optional[str] = None
    model: Optional[str] = None
    serial_number: Optional[str] = None
    purchase_date: Optional[date] = None
    supplier: Optional[str] = None
    purchase_order_no: Optional[str] = None
    warranty_start_date: Optional[date] = None
    warranty_end_date: Optional[date] = None
    location: Optional[str] = None
    campus: Optional[str] = None
    department: Optional[str] = None
    custodian: Optional[str] = None
    status: Optional[str] = None
    book_value: Optional[float] = None


class AssetResponse(AssetBase):
    id: int
    asset_id: str

    class Config:
        orm_mode = True
