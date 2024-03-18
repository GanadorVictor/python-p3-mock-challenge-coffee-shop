class Coffee:
    def __init__(self, name):
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        if len(name) < 3:
            raise ValueError("Name length must be at least 3 characters")
        self._name = name
        self._orders = []

    @property
    def name(self):
        return self._name

    def orders(self):
        return self._orders

    def customers(self):
        return list(set(order.customer for order in self._orders))

    def num_orders(self):
        return len(self._orders)

    def average_price(self):
        if not self._orders:
            return 0
        total_price = sum(order.price for order in self._orders)
        return total_price / len(self._orders)


class Customer:
    def __init__(self, name):
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        if not 1 <= len(name) <= 15:
            raise ValueError("Name must be between 1 and 15 characters")
        self._name = name
        self._orders = []

    @property
    def name(self):
        return self._name

    def orders(self):
        return self._orders

    def coffees(self):
        return list(set(order.coffee for order in self._orders))

    def create_order(self, coffee, price):
        if not isinstance(coffee, Coffee):
            raise TypeError("Coffee must be an instance of Coffee class")
        if not isinstance(price, float):
            raise TypeError("Price must be a float")
        if not 1.0 <= price <= 10.0:
            raise ValueError("Price must be between 1.0 and 10.0")
        order = Order(self, coffee, price)
        self._orders.append(order)
        coffee._orders.append(order)
        return order


class Order:
    def __init__(self, customer, coffee, price):
        if not isinstance(customer, Customer):
            raise TypeError("Customer must be an instance of Customer class")
        if not isinstance(coffee, Coffee):
            raise TypeError("Coffee must be an instance of Coffee class")
        if not isinstance(price, float):
            raise TypeError("Price must be a float")
        if not 1.0 <= price <= 10.0:
            raise ValueError("Price must be between 1.0 and 10.0")
        self.customer = customer
        self.coffee = coffee
        self.price = price


# Testing
if __name__ == "__main__":
    # Creating customers
    customer1 = Customer("Alice")
    customer2 = Customer("Bob")

    # Creating coffees
    coffee1 = Coffee("Espresso")
    coffee2 = Coffee("Latte")

    # Creating orders
    order1 = customer1.create_order(coffee1, 5.0)
    order2 = customer2.create_order(coffee1, 4.0)
    order3 = customer2.create_order(coffee2, 6.0)

    # Testing properties and methods
    print("Customer:", customer1.name)
    print("Coffee:", coffee1.name)
    print("Order price:", order1.price)
    print("Customer orders:", [order.price for order in customer1.orders()])
    print("Customer coffees:", [coffee.name for coffee in customer1.coffees()])
    print("Coffee orders:", [order.price for order in coffee1.orders()])
    print("Coffee customers:", [customer.name for customer in coffee1.customers()])
    print("Number of orders for coffee1:", coffee1.num_orders())
    print("Average price for coffee1:", coffee1.average_price())
