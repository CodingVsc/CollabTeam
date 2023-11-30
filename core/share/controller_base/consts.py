from enum import Enum


class Method(Enum):
    all = "all"
    create = "create"
    retrieve = "retrieve"
    delete = "delete"
    update = "update"
    partial_update = "partial_update"


METHOD_WRAPPER = {
    Method.all: "get",
    Method.create: "post",
    Method.retrieve: "get",
    Method.delete: "delete",
    Method.update: "put",
    Method.partial_update: "patch",
}

DEFAULT_METHODS = {Method.all, Method.create, Method.retrieve, Method.delete, Method.partial_update}
SINGLE_METHODS = [Method.retrieve, Method.update, Method.delete, Method.partial_update]
