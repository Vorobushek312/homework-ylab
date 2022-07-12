import time
def decorator_maker_with_arguments(call_count, start_sleep_time, factor, border_sleep_time ):
    def decorator_arg(func):
        def wrapper():
            t = start_sleep_time
            count = 1
            print(f"Кол-во запусков = call_count ({call_count})\nНачало работы")
            while count <= call_count:
                status = func
                if status == True:
                    break
                print(f"Запуск номер {count}. Ожидание: {t} секунд. Результат декорируемой функций = {status()}")
                time.sleep(t)
                count += 1
                if t < border_sleep_time:
                    t *= t*2**factor
                if t >= border_sleep_time:
                    t = border_sleep_time
            print("Конец работы")
        return wrapper
    return decorator_arg


@decorator_maker_with_arguments(3, 1, 3, 15)
def func():
    return False

if __name__ == '__main__':
    func()