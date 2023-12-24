from typing import TypeVar

T = TypeVar('T')


def singleton(original_class: T):
    instances = {}

    def get_instance(*args, **kwargs) -> T:
        if original_class not in instances:
            instances[original_class] = original_class(*args, **kwargs)
        return instances[original_class]

    return get_instance
