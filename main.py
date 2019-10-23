import logging
import time
import functools
from fluentpython.functions.decorators.profile import clock


@clock
def counter_step_by_step(counter_size: int) -> None:
    print("Counter size: {:03d}".format(counter_size))
    for n in range(counter_size):
        print("Current value: {:03d}".format(n))
        time.sleep(1)


@functools.lru_cache()
@clock(writer=logging.getLogger('fibo'))
def fibonacci(value: int):
    if value < 2:
        return value
    return fibonacci(value - 2) + fibonacci(value - 1)


if __name__ == "__main__":
    print(fibonacci.__name__)
    print(fibonacci(6))
