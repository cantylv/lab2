from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square
import requests


def main():
    r = Rectangle(9,9,"синего")
    c = Circle(9,"зеленого")
    s = Square(9,"красного")
    print(r)
    print(c)
    print(s)
    print(end='\n\n')
    print("__Пакет requests__")
    url = "https://github.com/ugapanyuk/BKIT_2022/wiki/lab_python_oop"
    response = requests.get(url)
    print(type(response))
    print(dir(response))



if __name__ == "__main__":
    main()