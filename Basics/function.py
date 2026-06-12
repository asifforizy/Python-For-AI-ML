def greet():
    print("Hello, world!")
    print("Welcome to Python!")

# Call the function
greet()



def say_goodbye():
    print("Goodbye!")
    print("See you later!")

# Call it multiple times
say_goodbye()
say_goodbye()
say_goodbye()




def check_weather():
    temperature = 25
    if temperature > 30:
        print("It's hot!")
    else:
        print("Nice weather!")

# Use the function
check_weather()




# Without parameters (inflexible)
def greet_alice():
    print("Hello, Alice!")

# With parameters (flexible)
def greet(name):
    print(f"Hello, {name}!")

# Now it works for anyone
greet("Alice")
greet("Bob")
greet("Charlie")



def introduce(name, age):
    print(f"My name is {name}")
    print(f"I am {age} years old")

# Call with values
introduce("Alice", 25)
introduce("Bob", 30)


# This function only prints
def add_print(a, b):
    print(a + b)

# This function returns a value
def add_return(a, b):
    return a + b

# Now you can use the result
result = add_return(5, 3)
print(f"The result is {result}")  # The result is 8



def calculate_area(width, height):
    area = width * height
    return area

# Store the returned value
room_area = calculate_area(10, 12)
print(f"Room size: {room_area} sq ft")  # Room size: 120 sq ft