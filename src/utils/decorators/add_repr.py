import inspect
from typing import TypeVar

T = TypeVar('T')


def add_repr(original_class: T) -> T:
    def __repr__(self: object):
        attributes = inspect.getmembers(original_class, lambda a: not (inspect.isroutine(a)))
        cleaned_attributes = [attribute for attribute in attributes
                              if not (attribute[0].startswith('__')
                                      and attribute[0].endswith('__'))]
        res_string = ''
        for cleaned_attribute in cleaned_attributes:
            res_string += f'{cleaned_attribute[0]}={getattr(self, cleaned_attribute[0])!r}\n'
        return f'{self.__class__}\n(\n{res_string})'

    original_class.__repr__ = __repr__

    return original_class
