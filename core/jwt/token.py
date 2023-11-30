from datetime import datetime, timedelta

from jwt import ExpiredSignatureError, PyJWTError, decode, encode

from core.config.jwt import config_token
from core.config.settings import settings
from core.jwt.base import AbstractToken
from core.share.controller_base.base import UserModel
from core.share.errors import TokenError
from src.auth.schemas import Tokens
from src.users.services.user_service import user_service


class TokenService(AbstractToken):
    secret_key = settings.secret_key
    algorithm = config_token.ALGORITHM
    access_token_lifetime = config_token.ACCESS_TOKEN_LIFETIME
    refresh_token_lifetime = config_token.REFRESH_TOKEN_LIFETIME
    refresh_token_rotate_min_lifetime = config_token.REFRESH_TOKEN_ROTATE_MIN_LIFETIME

    async def create_tokens(self, user: UserModel) -> Tokens:
        access_token = await self.generate_access_token(user)
        refresh_token = await self.generate_refresh_token(user)
        return {"access": access_token, "refresh": refresh_token}

    async def generate_access_token(self, user: UserModel) -> str:
        expire = datetime.utcnow() + timedelta(seconds=self.access_token_lifetime)
        payload = {
            "token_type": "access",
            "user_id": str(user.id),
            "user_permissions": [permission.codename for permission in user.permissions],
            "exp": expire,
        }
        return await self.encode_token(payload)

    async def generate_refresh_token(self, user: UserModel) -> str:
        expire = datetime.utcnow() + timedelta(seconds=self.refresh_token_lifetime)
        payload = {
            "token_type": "refresh",
            "user_id": str(user.id),
            "user_permissions": [permission.codename for permission in user.permissions],
            "exp": expire,
        }
        return await self.encode_token(payload)

    async def refresh(self, refresh_token: str) -> dict[str, str]:
        decoded_refresh = await self.decode_token(refresh_token)
        if decoded_refresh["token_type"] != "refresh":
            raise TokenError("Not a refresh token")
        return await self.create_tokens(await user_service.retrieve(decoded_refresh["user_id"]))

    async def encode_token(self, payload: dict) -> str:
        return encode(payload, self.secret_key, self.algorithm)

    async def decode_token(self, token: str) -> dict:
        try:
            return decode(token, self.secret_key, self.algorithm)
        except ExpiredSignatureError:
            raise ExpiredSignatureError("Token lifetime is expired")
        except PyJWTError:
            raise TokenError("Token is invalid")


token_service = TokenService()
