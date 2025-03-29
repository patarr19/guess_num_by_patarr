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

    while True:
        try:
            attemps = 10
            user_num = int(input())
            if user_num == num:
                print("Поздравляю, вы угадали число! Оно и правда было " + str(num) + ". Сколько попыток осталось: " + str(attemps))
                break
            elif user_num < num:
                print("Увы, но ваше число меньше загаданного, попробуйте еще раз")
                attemps -=1
                print("Кол-во попыток:" + str(attemps))
            elif user_num > num:
                print("Увы, но ваше число больше загаданного, попробуйте еще раз")
                attemps -= 1
                print("Кол-во попыток: " + str(attemps))
        except ValueError:
            print("Введите натуральное ЧИСЛО")
        except TypeError:
            print("Произошла ошибка. Попробуйте позже. код 2")


if __name__ == "__main__":
    main()

#доделать!!!!!!!!!!!!!!!!!!!!!