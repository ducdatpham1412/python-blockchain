def get_object(object: dict, key: str, default=None):
    try:
        return object[key]
    except KeyError or TypeError:
        return default
