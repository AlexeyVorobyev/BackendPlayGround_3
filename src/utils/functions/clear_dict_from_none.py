from typing import Any


def clear_dict_from_none(dct: dict) -> dict:
    def validation_rule(item: Any):
        if item[1] is None:
            return False
        if type(item[1]) == dict and len(item[1].keys()) == 0:
            return False
        return True

    return dict(filter(validation_rule, dct.items()))


def clear_nested_dict_from_none(dct: dict) -> dict:
    def dfs(dct_internal: dict) -> dict:
        result = dct_internal
        for key in result:
            if type(result[key]) == dict:
                result[key] = dfs(result[key])
        result = clear_dict_from_none(result)
        return result

    return dfs(dct)

