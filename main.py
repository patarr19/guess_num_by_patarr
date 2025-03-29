import random

def main():
    try:
        print("Добро пожаловать в угадайку числа!\nВведите начало диапазона: ")
        start = int(input())
        print("Введите конец диапазона: ")
        end = int(input())
        num = random.randint(start, end)
        # print(num) - проверка
    except ValueError:
        print("Введите натуральное ЧИСЛО!")
        return

    print("Я загадал число, попробуйте угадать, но у вас будет всего 10 попыток!")
    attempts = 10

    while attempts > 0:
        try:
            user_num = int(input())
            if user_num == num:
                print("Поздравляю, вы угадали число! Оно и правда было " + str(num) + ". Сколько попыток осталось: " + str(attempts))
                break
            elif user_num < num:
                print("Увы, но ваше число меньше загаданного, попробуйте еще раз")
                attempts -=1
                print("Кол-во попыток:" + str(attempts))
            elif user_num > num:
                print("Увы, но ваше число больше загаданного, попробуйте еще раз")
                attempts -= 1
                print("Кол-во попыток: " + str(attempts))
        except ValueError:
            print("Введите натуральное ЧИСЛО")
        except TypeError:
            print("Произошла ошибка. Попробуйте позже. код 2")

    print("У вас закончились попытки. Приходите сново")

if __name__ == "__main__":
    main()
#первая версия на русском. скоро вторая версия с кнопкой "показать правильный ответ".
#возможно, будет версия в тг боте(aiogram)
#there are some bugs. i will fix this in near time
