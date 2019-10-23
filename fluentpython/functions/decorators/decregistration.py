registry = []


def register(func):
    print('Running register: {0!r}'.format(func))
    registry.append(func)
    return func


@register
def func1():
    print('Running func1()...')


@register
def func2():
    print('Running func2()...')


def func3():
    print('Running func3()...')
