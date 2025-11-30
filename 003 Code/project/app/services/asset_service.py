from sqlalchemy.orm import Session
from typing import List, Dict, Any
from fastapi import HTTPException
from app.repositories.asset import AssetRepository
from app.schemas.asset import AssetCreate, AssetUpdate, AssetResponse

class AssetService:
    def __init__(self, db: Session):
        self.repo = AssetRepository(db)

    def list_assets(self, limit: int = 100) -> List[AssetResponse]:
        return self.repo.get_all(limit=limit)

    def get_asset(self, asset_id: str) -> AssetResponse:
        asset = self.repo.get_by_asset_id(asset_id)
        if not asset:
            raise HTTPException(status_code=404, detail="Asset not found")
        return asset

    def create_asset(self, data: AssetCreate) -> AssetResponse:
        existing = self.repo.get_by_asset_id(data.asset_id)
        if existing:
            raise HTTPException(status_code=400, detail="Asset ID already exists")
        return self.repo.create(data)

    def update_asset(self, asset_id: str, data: AssetUpdate) -> AssetResponse:
        asset = self.repo.get_by_asset_id(asset_id)
        if not asset:
            raise HTTPException(status_code=404, detail="Asset not found")
        return self.repo.update(asset, data)

    def delete_asset(self, asset_id: str) -> None:
        asset = self.repo.get_by_asset_id(asset_id)
        if not asset:
            raise HTTPException(status_code=404, detail="Asset not found")
        self.repo.delete(asset)

    def search_assets(self, filters: Dict[str, Any]) -> List[AssetResponse]:
        return self.repo.search(filters)

    def get_stats(self):
        assets = self.repo.get_all(limit=10_000)  # 임시
        total = len(assets)
        by_status = {}
        by_campus = {}
        by_type = {}

        for a in assets:
            by_status[a.status] = by_status.get(a.status, 0) + 1
            by_campus[a.campus or "Unknown"] = by_campus.get(a.campus or "Unknown", 0) + 1
            by_type[a.asset_type] = by_type.get(a.asset_type, 0) + 1

        return {
            "total_assets": total,
            "by_status": by_status,
            "by_campus": by_campus,
            "by_type": by_type,
        }
