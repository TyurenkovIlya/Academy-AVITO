import json
import keyword


class AttributeSetter:
    def __init__(self, dict_: dict):
        self._set_attributes(dict_)

    def _set_attributes(self, dict_: dict):
        for k, v in dict_.items():
            if keyword.iskeyword(k):
                k = k + '_'
            if isinstance(v, dict):
                self.__dict__[k] = AttributeSetter(v)
            else:
                self.__dict__[k] = v


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

    def __init__(self, _dict):
        super().__init__(_dict)
        _ = self.price

    def __getattribute__(self, item):
        if item == 'price':
            return self._get_price()

        return super().__getattribute__(item)

    def __repr__(self):
        return f'{self.title} | {self.price} ₽'

    def _get_price(self):
        price = 0
        try:
            price = super().__getattribute__('price')
        except AttributeError:
            pass

        if price < 0:
            raise ValueError('price must be >= 0')
        return price


class Advert(ColorizeMixin, BaseAdvert):
    pass


if __name__ == '__main__':
    #обращение к вложенным атрибутам через точки
    lesson_str = """{
                  "title": "python",
                  "price": 0,
                  "location": {
                      "address": "город Москва, Лесная, 7",
                      "metro_stations": ["Белорусская"]
                      }
    }"""
    lesson = json.loads(lesson_str)
    lesson_ad = Advert(lesson)
    print(lesson_ad.location.address)

    # ошибка при отрицательной цене
    # lesson_str = '{"title": "python", "price": -1}'
    # lesson = json.loads(lesson_str)
    # lesson_ad = Advert(lesson)

    # 0 при отсутствии цены
    # lesson_str = '{"title": "python"}'
    # lesson = json.loads(lesson_str)
    # lesson_ad = Advert(lesson)
    # print(lesson_ad.price)

    # желтый цвет текста при выводе
    # lesson_str = """{
    #   "title": "Вельш-корги",
    #   "price": 1000,
    #   "class": "dogs",
    #   "location": {
    #     "address": "поселок санатория Тишково, 25"
    #   }
    #  }"""
    # lesson = json.loads(lesson_str)
    # corgi = Advert(lesson)
    # print(corgi)
    # print(corgi.class_)
