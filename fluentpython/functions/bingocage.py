import random


class BingoCage:

    def __init__(self, items: list) -> None:
        self._items = items
        random.shuffle(self._items)

    def pick(self) -> int:
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('Pick from empty BingoCage.')

    def __call__(self):
        return self.pick()

    @property
    def items(self) -> list:
        return self._items
