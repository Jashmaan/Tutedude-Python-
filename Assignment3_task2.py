import math
n = float(input("Enter a number: "))
def calculate_math_functions(n):
    square_root = math.sqrt(n)
    natural_log = math.log(n)
    sine_value = math.sin(n)
    
    return square_root, natural_log, sine_value

result = calculate_math_functions(n)
print("sqaure root: ", result[0]),
print("natural log: ", result[1]),
print("sine value: ", result[2])
