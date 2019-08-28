from typing import Dict, Any


def remove_empty(dictionary: Dict[Any, Any]):
    """
    removes all entries in the provided dictionary whose value is falsey
    """
    return {k: v for k, v in dictionary.items() if v}
