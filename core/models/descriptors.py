class EmailField:
    def __init__(self):
        pass

    def __set_name__(self, owner, name):
        self._name = f"_{name}"

    def __get__(self, obj, type):
        if obj is None:
            return self._default
        return getattr(obj, self._name, self._default)

    def __set__(self, obj, value):
        setattr(obj, self._name, int(value))
