from fastapi import HTTPException, Security
from fastapi.security import OAuth2PasswordBearer
from starlette.status import HTTP_401_UNAUTHORIZED

from core.jwt.token import token_service
from core.share.service import BaseService
from src.auth.schemas import LoginUser
from src.users.errors import ValidationError
from src.users.services.user_service import user_service as us

oauth2 = OAuth2PasswordBearer(tokenUrl="/auth/oauth-authorize")


class AuthService:
    def __init__(self, user_service: BaseService):
        self.user_service = user_service

    async def login_user(self, model: LoginUser):
        user = await self.user_service.get_user_by_credentials(model.email)
        if user.password != model.password:
            raise ValidationError("Invalid password")
        return await token_service.create_tokens(user)

    async def get_current_user(self, token: str = Security(oauth2)):
        if data := await token_service.decode_token_or_none(token):
            return await self.user_service.retrieve(pk=data["user_id"])
        raise HTTPException(HTTP_401_UNAUTHORIZED, "Unauthorized")


auth_service = AuthService(us)
