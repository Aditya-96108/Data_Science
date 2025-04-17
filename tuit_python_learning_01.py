import pandas as pd

# 1. List
fruits = ['apple', 'banana', 'mango']
print("List:", fruits)

# 2. Dictionary
fruit_colors = {'apple': 'red', 'banana': 'yellow', 'mango': 'orange'}
print("Dictionary:", fruit_colors)

# 3. Series (like a list with labels)
fruit_prices = pd.Series([30, 10, 50], index=['apple', 'banana', 'mango'])
print("Series:\n", fruit_prices)

# 4. Function
def greet(name):
    return f"Hello, {name}!"

print(greet("Aditya"))

# 5. Class
class Fruit:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def show(self):
        print(f"{self.name} is {self.color}")

# Creating object of class
my_fruit = Fruit('apple', 'red')
my_fruit.show()
