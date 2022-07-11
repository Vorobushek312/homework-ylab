import time
def decorator_arg(func):
    def wrapper(call_count, start_sleep_time, factor, border_sleep_time):
        count = 1
        print(f"Кол-во запусков = call_count ({call_count})\nНачало работы")
        while count <= call_count:
            status = func
            if status == True:
                break
            print(f"Запуск номер {count}. Ожидание: {start_sleep_time} секунд. Результат декорируемой функций = {status()}")
            time.sleep(start_sleep_time)
            count += 1
            if start_sleep_time < border_sleep_time:
                start_sleep_time *= start_sleep_time*2**factor
            if start_sleep_time >= border_sleep_time:
                start_sleep_time = border_sleep_time
        print("Конец работы")
    return wrapper


@decorator_arg
def func(call_count = 3, start_sleep_time = 1, factor = 3, border_sleep_time = 15):
    return False

if __name__ == '__main__':
    func(call_count = 3, start_sleep_time = 1, factor = 2, border_sleep_time = 20)