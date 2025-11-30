from fastapi import APIRouter, Depends, Query, Body, Path
from typing import List, Optional, Dict, Any
from sqlalchemy.orm import Session

from app.api.dependencies import get_db
from app.schemas.asset import AssetCreate, AssetUpdate, AssetResponse
from app.services.asset_service import AssetService

router = APIRouter(prefix="/assets", tags=["Assets"])


@router.post("/", response_model=AssetResponse, status_code=201, summary="자산 생성")
def create_asset(
    payload: AssetCreate = Body(...),
    db: Session = Depends(get_db)
):
    service = AssetService(db)
    return service.create_asset(payload)


@router.get("/", response_model=List[AssetResponse], summary="자산 목록 조회")
def list_assets(
    limit: int = Query(100, ge=1, le=1000),
    db: Session = Depends(get_db)
):
    service = AssetService(db)
    return service.list_assets(limit=limit)

@router.get("/search", response_model=List[AssetResponse], summary="자산 검색")
def search_assets(
    campus: Optional[str] = Query(None),
    status: Optional[str] = Query(None),
    department: Optional[str] = Query(None),
    asset_type: Optional[str] = Query(None),
    db: Session = Depends(get_db),
):
    service = AssetService(db)
    filters = {
        "campus": campus,
        "status": status,
        "department": department,
        "asset_type": asset_type,
    }
    active_filters = {k: v for k, v in filters.items() if v is not None}
    return service.search_assets(active_filters)


@router.get("/stats", summary="자산 통계")
def get_stats(db: Session = Depends(get_db)):
    service = AssetService(db)
    return service.get_stats()


@router.get("/{asset_id}", response_model=AssetResponse, summary="특정 자산 조회")
def get_asset(
    asset_id: str = Path(..., description="조회할 자산의 고유 ID"),
    db: Session = Depends(get_db)
):
    service = AssetService(db)
    return service.get_asset(asset_id)


@router.put("/{asset_id}", response_model=AssetResponse, summary="자산 정보 수정")
def update_asset(
    asset_id: str = Path(..., description="수정할 자산의 고유 ID"),
    payload: AssetUpdate = Body(...),
    db: Session = Depends(get_db)
):
    service = AssetService(db)
    return service.update_asset(asset_id, payload)


@router.delete("/{asset_id}", status_code=204, summary="자산 삭제")
def delete_asset(
    asset_id: str = Path(..., description="삭제할 자산의 고유 ID"),
    db: Session = Depends(get_db)
):
    service = AssetService(db)
    service.delete_asset(asset_id)
    return None
