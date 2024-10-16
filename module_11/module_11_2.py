import inspect


def introspection_info(obj):
    if isinstance(obj, (int, float, str, bool, list, tuple, dict, set, frozenset)):
        module = "__main__"
    else:
        module = inspect.getmodule(obj).__name__
    return {
        "Тип объекта": type(obj),
        "Модуль объекта": module,
        "Атрибуты и методы объекта": dir(obj),
        "Можно ли вызвать объект?": callable(obj),
        "Свойства и значения объекта": obj.__class__.__dict__
    }

class callable_object:
    One = "Первый атрибут"
    Two = "Второй атрибут"

    def __init__(self, *args):
        self.attr_of_obj = args
    def first_method(self):
        pass

    def __call__(self, *args, **kwargs):
        return "Вы меня вызвали!"

number_info = introspection_info(42)
print(number_info)

number_info_2 = introspection_info(callable_object(1, 2, 3, 4, 5))
print(number_info_2)