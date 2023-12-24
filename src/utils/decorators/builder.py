import inspect
from typing import TypeVar


# аттрибуты с префиксом _attr участвуют в логике билдера

def is_correct_attribute(attribute: str) -> bool:
    if attribute.startswith('_attr'):
        return True
    return False


def generate_func_setter(attr: str):
    def fun(self, arg):
        setattr(self, attr, arg)
        return self

    fun.__name__ = attr.replace('_attr_', '', 1)

    return fun


def generate_func_getter(attr: str):
    def fun(self):
        return getattr(self, attr)

    fun.__name__ = attr.replace('_', '', 1)
    return fun


T = TypeVar('T')


def builder(cls: T) -> T:
    attributes = list(inspect.getmembers(cls)[0][1].keys())
    cleaned_attributes: list[str] = [attribute for attribute in attributes if is_correct_attribute(attribute)]

    mapping = {}
    model_attr_mapping = {}

    for attr in cleaned_attributes:
        setter = generate_func_setter(attr)
        getter = generate_func_getter(attr)
        setattr(cls, setter.__name__, setter)
        setattr(cls, getter.__name__, getter)
        mapping[setter.__name__] = setter
        mapping[getter.__name__] = getter
        model_attr_mapping[attr.replace('_attr_', '', 1)] = None

    def dir_func(self):
        return mapping.keys

    def getattr_func(self, item):
        for item in mapping:
            return mapping[item]

    def build(self):

        for key in model_attr_mapping:
            model_attr_mapping[key] = getattr(self, f"attr_{key}")()

        print(model_attr_mapping)

        return self._model(**model_attr_mapping)

    cls.__dir__ = dir_func
    cls.__getattr__ = getattr_func
    cls.build = build

    return cls
