import json
import keyword
from typing import Any


class AttributeSetter:
    def __init__(self, dict_: dict):
        for key in dict_:
            new_key = key + '_' if keyword.iskeyword(key) else key
            setattr(self, new_key, dict_[key])

    def __setattr__(self, __name: str, __value: Any) -> None:
        if isinstance(__value, dict):
            super().__setattr__( __name, AttributeSetter(__value))
        else:
            super().__setattr__( __name, __value)

    def __getattr__(self, __name: str) -> Any:
        return super().__getattribute__(__name)


class ColorizeMixin:
    def __repr__(self):
        super_repr = super().__repr__()
        try:
            return f'\033[{super().repr_color_code};40m' + \
                   super_repr + '\033[0m'
        except AttributeError:
            return super_repr


class BaseAdvert(AttributeSetter):
    repr_color_code = 33

    def __init__(self, dict_):
        if 'title' not in dict_:
            raise ValueError('title not in json')

        super(BaseAdvert, self).__init__(dict_)

    def __repr__(self):
        return f'{self.title} | {self.price} ₽'

    @property
    def price(self):
        if '_curr_price' in self.__dict__:
            return self._curr_price
        return 0

    @price.setter
    def price(self, price):
        if price < 0:
            raise ValueError('Price must be >= 0')
        self.curr_price = price

class Advert(ColorizeMixin, BaseAdvert):
    pass


if __name__ == '__main__':
    #обращение к вложенным атрибутам через точки
    # lesson_str = """{
    #               "title": "python",
    #               "price": 0,
    #               "location": {
    #                   "address": "город Москва, Лесная, 7",
    #                   "metro_stations": ["Белорусская"]
    #                   }
    # }"""
    # lesson = json.loads(lesson_str)
    # lesson_ad = Advert(lesson)
    # print(lesson_ad.location.address)

    # ошибка при отрицательной цене
    # lesson_str = '{"title": "python", "price": -1}'
    # lesson = json.loads(lesson_str)
    # lesson_ad = Advert(lesson)

    # 0 при отсутствии цены
    # lesson_str = '{"title": "python"}'
    # lesson = json.loads(lesson_str)
    # lesson_ad = Advert(lesson)
    # print(lesson_ad.price)

    # ошибка при отсутствии title
    lesson_str = """{
      "price": 1000,
      "class": "dogs",
      "location": {
        "address": "поселок санатория Тишково, 25"
      }
    }"""
    lesson = json.loads(lesson_str)
    corgi = Advert(lesson)
    print(corgi)
    print(corgi.class_)

    # # ошибка при отсутствии title
    # lesson_str = """{
    #   "title": "Вельш-корги",
    #   "price": 1000,
    #   "class": "dogs",
    #   "location": {
    #     "address": "поселок санатория Тишково, 25"
    #   }
    # }"""
    # lesson = json.loads(lesson_str)
    # corgi = Advert(lesson)
    # print(corgi)
    # print(corgi.class_)
