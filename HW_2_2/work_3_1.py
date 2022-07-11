def memoize_func(f):
    memo = dict()

    def func(number):
        print(f"Данные в памяти: {memo}")
        if number not in memo:
            memo[number] = f(number)
        return memo[number]

    return func


@memoize_func
def multiplier(number: int):
    return number * 2

if __name__ == '__main__':
    while True:
        x = int(input("Введите число:"))
        print(multiplier(x))
        if x == 11:
            break
        print("Для выхода ввелите число 11")