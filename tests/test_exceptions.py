# Проверка на ожидаемые исключения

import pytest

def test_add_raises():
    with pytest.raises(ZeroDivisionError):
     1/0

