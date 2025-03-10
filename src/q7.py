class Car:
    """
    Task 1
    - Define a class named Car with attributes: make, model, year
    - Initialize these attributes in the __init__ method
    - Add a method named describe_car() that prints information about the car as "Year Make Model"
    """

    # Define the __init__ method
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    # Define the describe_car method
    def describe_car(self):
        print("")

# Task 2
# Create an instance of the Car class with the following attributes and call describe_car method:
# - Make: Toyota, Model: Corolla, Year: 2020
print("(1) q7_Task 2:")
car1 = Car("Toyota", "Corolla", 2020)

# Do a call describe_car method
car1.describe_car()  # Expected output: 2020 Toyota Corolla

# Print car1 expected output
print(car1.make, car1.model, car1.year)
