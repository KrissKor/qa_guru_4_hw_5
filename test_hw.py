import math
import random


def test_greeting():
    name = "Анна"
    age = 25
    output = f"Привет, {name}! Тебе {age} лет."
    print(output)
    assert output == "Привет, Анна! Тебе 25 лет."


def test_rectangle():
    a = 10
    b = 20
    perimeter = 2 * (a + b)
    assert perimeter == 60

    area = a * b
    assert area == 200


def test_circle():
    r = 23
    area = math.pi * (r ** 2)
    print(area)
    assert area == 1661.9025137490005

    length = 2 * math.pi * r
    print(length)
    assert length == 144.51326206513048


def test_random_list():
    l = []
    for i in range (0, 10):
        l.append(random.randint(1, 100))
    l.sort()
    assert len(l) == 10
    assert l[0] < l[-1]


def test_unique_elements():
    l = list([1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 8, 9, 10, 10])
    l = set(l)
    l = list(l)

    assert isinstance(l, list)
    assert len(l) == 10
    assert l == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def test_dicts():
    first = ["a", "b", "c", "d", "e"]
    second = [1, 2, 3, 4, 5, 6]

    d = dict(zip(first, second))
    print(d.values())

    assert isinstance(d, dict)
    assert len(d) == 5

