from fastapi import APIRouter

from src.auth.controllers import AuthController, authorize

auth_router = APIRouter(prefix="/auth", tags=["Auth"])
auth_router.add_api_route("/login", AuthController().login, methods=["post"])

# For development
auth_router.include_router(authorize)
