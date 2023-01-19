class Button:

# атрибуты класса
    type = "Кнопка"

# атрибуты экземпляра
    def __init__(self, text, link, loc):
        self.text = text
        self.link = link
        self.loc = loc

    def click(self):
        return "Клик по локатору - {}".format(self.loc)

    # создаем экземпляры класса
home = Button("Домой", '/home', 'html>div>button#home')

    # вызывем метод экземпляра

print(home.click())


