class input:
    def __init__(self, text, loc):
        self.loc = loc
        self.text = text
class Button:
    def __init__(self, text, loc):
        self.loc = loc
        self.text = text

class Title:
    def __init__(self, text, loc):
        self.loc = loc
        self.text = text

class Link:
    def __init__(self, text, loc):
        self.loc = loc
        self.text = text

search = input("Ввод", 222)
search1 = Button("Кнопка", 333)
search2 = Title("Заглавие", 444)
search3 = Link("Связь", 555)

print(search.loc, search.text)
print(search1.loc, search1.text)
print(search2.loc, search2.text)
print(search3.loc, search3.text)