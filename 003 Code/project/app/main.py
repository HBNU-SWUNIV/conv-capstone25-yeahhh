from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.db.session import engine, Base
from app.api.api import api_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Asset Management API",
    description="A scalable API with CORS and Health Check, built with FastAPI.",
    version="6.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix="/api")

@app.get("/", tags=["Root"], summary="API 환영 메시지")
def read_root():
    return {"message": "Welcome to the Asset Management API. Visit /docs for documentation."}

@app.get("/health", tags=["Health Check"], summary="서버 상태 확인")
def health_check():
    return {"status": "ok"}
