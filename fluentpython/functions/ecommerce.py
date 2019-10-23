from abc import ABC, abstractmethod
from decimal import Decimal

from typing import List


class Customer:

    def __init__(self, first_name: str, last_name: str, fidelity: int):
        self.first_name = first_name
        self.last_name = last_name
        self.fidelity = fidelity

    @property
    def full_name(self):
        return "{} {}".format(self.first_name, self.last_name)


class OrderItem:

    def __init__(self, product: str, quantity: int, price: Decimal):
        self.product = product
        self.quantity = quantity
        self.price = price

    def total(self):
        return self.price * self.quantity


class Order:

    def __init__(self, customer: Customer, cart: List[OrderItem], promotion: 'Promotion' = None):
        self.customer = customer
        self.cart = cart
        self.promotion = promotion
        self._total = 0.00

    def total(self) -> Decimal:
        self._total = sum(item.total() for item in self.cart)
        return self._total

    def due(self):
        if not self.promotion:
            discount = 0.00
        else:
            discount = self.promotion.discount(order=self)
        return self.total() - discount

    def __repr__(self):
        return "Order:\nCustomer: {}\nNumber of items: {}\nTotal: {:.2f}\nDue: {:.2f}".format(self.customer.full_name,
                                                                                              len(self.cart),
                                                                                              self.total(),
                                                                                              self.due())


class Promotion(ABC):

    @abstractmethod
    def discount(self, order: Order) -> Decimal:
        pass


class FidelityPromo(Promotion):  # first Concrete Strategy
    """5% discount for customers with 1000 or more fidelity points"""

    def discount(self, order):
        return order.total() * .05 if order.customer.fidelity >= 1000 else 0


class BulkItemPromo(Promotion):  # second Concrete Strategy
    """10% discount for each LineItem with 20 or more units"""

    def discount(self, order):
        discount = 0
        for item in order.cart:
            if item.quantity >= 20:
                discount += item.total() * .1
        return discount


class LargeOrderPromo(Promotion):  # third Concrete Strategy
    """7% discount for orders with 10 or more distinct items"""

    def discount(self, order):
        distinct_items = {item.product for item in order.cart}
        if len(distinct_items) >= 10:
            return order.total() * .07
        return 0
