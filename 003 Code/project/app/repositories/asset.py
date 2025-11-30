from sqlalchemy.orm import Session
from typing import List, Optional, Dict, Any
from app.models.asset import Asset
from app.schemas.asset import AssetCreate, AssetUpdate

class AssetRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self, limit: int = 100) -> List[Asset]:
        return self.db.query(Asset).limit(limit).all()

    def get_by_asset_id(self, asset_id: str) -> Optional[Asset]:
        return self.db.query(Asset).filter(Asset.asset_id == asset_id).first()

    def create(self, data: AssetCreate) -> Asset:
        asset = Asset(**data.dict())
        self.db.add(asset)
        self.db.commit()
        self.db.refresh(asset)
        return asset

    def update(self, asset: Asset, data: AssetUpdate) -> Asset:
        for field, value in data.dict(exclude_unset=True).items():
            setattr(asset, field, value)
        self.db.commit()
        self.db.refresh(asset)
        return asset

    def delete(self, asset: Asset) -> None:
        self.db.delete(asset)
        self.db.commit()

    def search(self, filters: Dict[str, Any]) -> List[Asset]:
        query = self.db.query(Asset)
        if campus := filters.get("campus"):
            query = query.filter(Asset.campus == campus)
        if status := filters.get("status"):
            query = query.filter(Asset.status == status)
        if department := filters.get("department"):
            query = query.filter(Asset.department == department)
        if asset_type := filters.get("asset_type"):
            query = query.filter(Asset.asset_type == asset_type)
        return query.all()
