import sys
from getpass import getpass

import argon2

from core.cmds import func_registry
from src.users.errors import ValidationError
from src.users.repositories.user_repository import user_repository
from src.users.utils.password_hash import PasswordHash
from src.users.utils.password_validator import validate_password


@func_registry(description="Create new superuser in DB")
async def createsuperuser():
    user_data = {
        "username": await get_username(),
        **get_full_name(),
        "password": get_password(),
    }
    await user_repository.create_superuser(user_data)
    sys.stdout.write("Superuser successfully created.")


async def get_username() -> str:
    while True:
        username = input("Please provide your username: ")
        if not username:
            sys.stdout.write("Your username could not be blank line\n")
        elif await user_repository.exists(username=username):
            sys.stdout.write("Username already exists\n")
        else:
            break
    return username


def get_full_name() -> dict[str, str]:
    full_name = {}
    for name in ["first_name", "last_name"]:
        while True:
            input_name = input(f"Please provide your {name}: ")
            if not input_name:
                sys.stdout.write(f"Your {name} could not be blank line\n")
            else:
                full_name[name] = input_name
                break
    return full_name


def get_password() -> str | PasswordHash:
    while True:
        password = getpass()
        if not password:
            sys.stdout.write("Password can't be blank line\n")
            continue

        password_again = getpass(prompt="Password again: ")

        if password != password_again:
            sys.stdout.write("Password doesn't match\n")
            continue

        try:
            validate_password(password)
        except ValidationError as error:
            sys.stdout.write(f"\033[91m\n{str(error)}\n\033[0m")
            is_it_ok = input(
                "Are you sure you want to use this password? Press 'Y/y' for confirmation: "
            )
            if is_it_ok.lower() == "y":
                return PasswordHash(argon2.PasswordHasher().hash(password))
        else:
            break
    return password
