a: int = 5
b: str = 'строка'

# после создания такой переменной мы не можем присвоить ей значение с другим типом

a = 'quwuwuw'

def indent(s: str, width: int) -> str:
    return " " * (max(0, width - len(s))) + s


print(indent('321', 321))
