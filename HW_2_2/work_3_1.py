def memoize_func(f):
    memo = dict()

    def func(number):
        if number not in memo:
            memo[number] = f(number)
        return memo[number]

    return func


@memoize_func
def multiplier(number: int):
    return number * 2

