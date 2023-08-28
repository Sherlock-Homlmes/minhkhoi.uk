# default
import datetime
import json
from enum import Enum

from beanie import Document
from beanie.odm.fields import PydanticObjectId
from bson import json_util

# libraries
from pydantic import BaseModel

# local
from .time_modules import time_to_str


def serialization(obj: dict) -> dict:
    return json.dumps(obj, default=json_util.default)


def deserialization(obj: dict) -> dict:
    return json.loads(obj, object_hook=json_util.object_hook)


def convert_type_to_json(value) -> dict:
    value_type = type(value)
    if value_type == datetime.datetime:
        return time_to_str(value)
    elif value_type == PydanticObjectId:
        return str(value)
    elif isinstance(value, Enum):
        return value.value

    # convert if value is multi value
    elif value_type == list:
        for index, list_value in enumerate(value):
            value[index] = convert_type_to_json(list_value)

    return value


def mongodb_to_json(obj: dict | list) -> dict:
    if isinstance(obj, Document):
        obj = obj.json()
    if type(obj) == list:
        return [mongodb_to_json(x) for x in obj]
    elif type(obj) == dict:
        for key, value in obj.items():
            obj[key] = convert_type_to_json(value)
            if isinstance(value, BaseModel):
                obj[key] = value.dict()
                for model_key, model_value in obj[key].items():
                    print(model_key, model_value)
                    obj[key][model_key] = convert_type_to_json(model_value)
    else:
        obj = convert_type_to_json(obj)

    return obj
