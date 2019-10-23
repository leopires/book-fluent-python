def deco(func):
    def inner():
        print("Running 'inner'.")

    return inner


@deco
def target():
    print("Running 'target'.")
