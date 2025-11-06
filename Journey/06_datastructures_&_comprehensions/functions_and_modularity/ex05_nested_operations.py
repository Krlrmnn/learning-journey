def operation_factory(operation_type: str, modifier: float):
    if operation_type == "add":
        def add_function(value):
            return value + modifier
        return add_function
    elif operation_type == "multiply":
        def multiplier_function(value):
            return value * modifier
        return multiplier_function
    elif operation_type == "discount":
        def discount_function(value):
            return round(value * (1 - modifier), 2)
        return discount_function
    else:
        raise TypeError("Invalid parameters")

# The correct way to use this function is like this:
## U need to preset the parameters what you are going to work saving them inside a variable and after call the variable with the value inside ""
add_20 = operation_factory("add", 20)
print(add_20(50))        # 70

multiply_5 = operation_factory("multiply", 5)
print(multiply_5(20))    # 100

discount_20 = operation_factory("discount", 0.2)
print(discount_20(100))  # 80.0