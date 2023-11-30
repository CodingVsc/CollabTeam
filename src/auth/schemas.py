from pydantic import model_validator

from core.share.schemas import Base


class LoginUser(Base):
    email: str
    password: str

    @model_validator(mode="after")
    def email_validator(self):
        if "@" not in self.email:
            raise ValueError("email must contain '@'")
        return self


class Tokens(Base):
    access: str
    refresh: str
