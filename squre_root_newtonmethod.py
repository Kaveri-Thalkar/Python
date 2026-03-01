def newton_method(number, number_iters=100):
    a = float(number)
    x = a  # initial guess
    
    for i in range(number_iters):
        x = 0.5 * (x + a / x)
    
    return x


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Square root of first number:", newton_method(a))
print("Square root of second number:", newton_method(b))