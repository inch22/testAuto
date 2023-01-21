# импортируем класс Check из файла check.py
from check import Check
#  создаем 4 класса по выбранным элементам страницы
class Search(Check): #каждый класс наследуйте от класса Check (добавляем в скобках класс)
    def __init__(self, loc):
        self.loc = loc
        super(Search, self).__init__(self.loc) #добавляем в инициализацию
        # каждого класса надпись super(Search,Button и тд.., self).__init__(self.loc),
        # т.е. задаем атрибуты класса Сheck

class Button(Check):
    def __init__(self, loc):
        self.loc = loc
        super(Button, self).__init__(self.loc)

class Pic(Check):
    def __init__(self, loc):
        self.loc = loc
        super(Pic, self).__init__(self.loc)

class Text(Check):
    def __init__(self, loc):
        self.loc = loc
        super(Text, self).__init__(self.loc)
