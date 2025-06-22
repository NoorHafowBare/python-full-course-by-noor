# Object-Oriented Programming (OOP)
# 1. What is Object-Oriented Programming (OOP)?
# OOP is a programming paradigm that organizes code around objects—self-contained units that combine data (attributes) and behaviors (methods). By modeling real-world entities as classes (blueprints) and creating objects (instances) from those classes, your code becomes more modular, reusable, and easier to maintain.

# 2. Why Use OOP?
# Modularity:
# Code is divided into classes, each handling specific responsibilities. This makes projects easier to manage and debug.

# Reusability:
# With inheritance and modular design, you can reuse code without rewriting it for similar tasks.

# Maintainability:
# Changes to one part of your code (inside a class) are less likely to affect other parts, thanks to encapsulation and abstraction.

# Real-World Modeling:
# You can directly model real-world systems—like cars or bank accounts—making your code intuitive and realistic.

# 3. Key Concepts of OOP
# A. Abstraction
# What It Means:
# Abstraction hides complex details while exposing only what is necessary.
# Real-World Example:
# A TV remote control only shows you buttons to change channels and adjust volume—you don’t see the underlying electronics.

# Code Example:
class TVRemote:
    def change_channel(self, channel):
        return f"Changing to channel {channel}"
    def adjust_volume(self, level):
        return f"Adjusting volume to {level}"


if __name__ == "__main__":
    remote = TVRemote()
    print(remote.change_channel("Al- jazeera"))  # Output: Changing to channel Al- jazeera
    print(remote.adjust_volume(40))  # Output: Adjusting volume to 10

# B. Encapsulation
# What It Means:
# Encapsulation bundles data and methods into one class, restricting direct access to some data.
# Real-World Example:
# A bank account where you deposit or withdraw money only through official methods, protecting the account balance from accidental changes.
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return f"Deposited: ${amount}, New Balance: ${self.__balance}"
        return "Deposit amount must be positive."

    def withdraw(self, amount):
        if (amount > self.__balance):
            return "Insufficient funds."
        self.__balance -= amount
        return f"Withdrew: ${amount}, New Balance: ${self.__balance}"
    
    

if __name__ == "__main__":
    account = BankAccount("Noor", 100)
    print(account.deposit(50))  # Output: Deposited: $50, New Balance: $150
    print(account.withdraw(10))  # Output: Withdrew: $30, New Balance: $120
    # print(account.__balance)  # Raises an AttributeError because __balance is private      

# C. Inheritance
# What It Means:
# Inheritance allows one class (child) to take on properties and methods from another class (parent), promoting code reuse.
# Real-World Example:
# A vehicle hierarchy: A basic Car has common features (like starting the engine), while an ElectricCar inherits these features and adds its own (like charging).

class Car:
    """
    A general car with basic features.
    """

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start_engine(self):
        return f"self.make {self.model} engine has started."
    
    def stop_engine(self):
        return f"self.make {self.model} engine has stopped."
    
class ElectricCar(Car):
    def __init__(self, make, model, year, battery_capacity):
        super().__init__(make, model, year)
        self.battery_capacity = battery_capacity
    def charge(self):
        return f"Charging {self.make} {self.model} with {self.battery_capacity} kWh battery."
    
if __name__ == "__main__":
    my_car = Car("Toyota", "Corolla", 2020)
    print(my_car.start_engine())  # Output: Toyota Corolla engine has started.
    print(my_car.stop_engine())  # Output: Toyota Corolla engine has stopped.

    my_electric_car = ElectricCar("Tesla", "Model S", 2021, 100)
    print(my_electric_car.start_engine())  # Output: Tesla Model S engine has started.
    print(my_electric_car.charge())  # Output: Charging Tesla Model S with 100 kWh battery.


# D. Polymorphism

# What It Means:
# Polymorphism lets you use a single interface to work with different data types or classes. Methods with the same name can behave differently for different classes.
# Real-World Example:
# Different payment methods (credit card, debit card, PayPal) all process payments but in their own way. You can call process_payment() on any payment method without worrying about the underlying details.


class Payment:
    """
    A base class for payment methods.
    """
    def process_payment(self, amount):
        raise NotImplementedError("Subclasses must implement this method.")


class CreditCard(Payment):
    def process_payment(self, amount):
        return f"Processing credit card payment of ${amount}."


class DebitCard(Payment):
    def process_payment(self, amount):
        return f"Processing debit card payment of ${amount}."


class PayPal(Payment):
    def process_payment(self, amount):
        return f"Processing PayPal payment of ${amount}."


def make_payment(payment_method, amount):
    """
    Uses the process_payment method regardless of the payment type.
    """
    print(payment_method.process_payment(amount))


if __name__ == "__main__":
    # Creating different payment method objects.
    credit = CreditCard()
    debit = DebitCard()
    paypal = PayPal()

    # All use the same method name, but each works differently.
    make_payment(credit, 100)
    make_payment(debit, 150)
    make_payment(paypal, 200)