import sys

from core.cmds import func_registry
from core.share.errors import AlreadyExistError
from core.share.service import GenericService
from tests.fixtures.db_data import FIXTURES


@func_registry(description="Load data in DB")
async def loaddata():
    loaded_models = await add_models()

    if loaded_models == len(FIXTURES.keys()):
        message = "All data successfully loaded."
    elif loaded_models != 0:
        message = f"{loaded_models} models successfully loaded."
    else:
        message = "No data loaded."
    sys.stdout.write(message)


async def add_models() -> int:
    loaded_models = 0
    for model, values in FIXTURES.items():
        try:
            await GenericService(model).repository.bulk_create(values)
        except AlreadyExistError as e:
            sys.stdout.write(f"{e}\n")
            continue
        loaded_models += 1
    return loaded_models
