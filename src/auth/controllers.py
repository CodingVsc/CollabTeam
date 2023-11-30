from collections import defaultdict
from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from starlette.status import HTTP_400_BAD_REQUEST

from core.jwt.token import token_service
from core.share.controller_base.base import SlugField
from core.share.controller_base.controller import Controller
from core.share.errors import NoRowsFoundError
from src.auth.schemas import LoginUser, Tokens
from src.auth.services import auth_service
from src.users.errors import ValidationError
from src.users.permissions import allow_any
from src.users.services.user_service import user_service


class AuthController(Controller):
    pydantic_models = defaultdict(lambda: LoginUser)
    response_models = {"login": Tokens}
    permissions = defaultdict(lambda: allow_any)
    slug_field_type: SlugField = UUID
    service = auth_service

    async def login(self, model: LoginUser) -> Tokens:
        try:
            return await self.service.login_user(model)
        except (NoRowsFoundError, ValidationError) as e:
            raise HTTPException(HTTP_400_BAD_REQUEST, str(e))


authorize = APIRouter()


@authorize.post("/oauth-authorize")
async def oauth_authorize(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    """
    Only in development for OAuth2PasswordBearer authorization
    Require use OAuth2PasswordRequestForm here because without controller
    Delete this later
    """
    try:
        user = await user_service.get_user_by_credentials(form_data.username)
    except (NoRowsFoundError, ValidationError) as e:
        raise HTTPException(HTTP_400_BAD_REQUEST, str(e))
    if user.password != form_data.password:
        raise ValidationError("Invalid password")
    access_token = await token_service.generate_access_token(user)
    return {"access_token": access_token}
