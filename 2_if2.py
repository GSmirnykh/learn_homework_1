"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""
def compare_strings(s1, s2):
    if type(s1) is str and type(s2) is str:
        if len(s1) == len(s2):
            return 1
        elif len(s1) != len(s2) and s2 == 'learn':
            return 2
        elif len(s1) > len(s2):
            return 3
    else:
        return 0




def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    print(compare_strings('Hello', 2023))
    print(compare_strings('Hello', 'world'))
    print(compare_strings('Hello', '2023'))
    print(compare_strings('python', 'learn'))

if __name__ == "__main__":
    main()
