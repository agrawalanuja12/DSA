x = int(input("Enter the value of x :  "))
y = int(input("Enter the value of y :  "))
print(f"Before swapping The value of x is {x}")
print(f"Before swapping The value of y is {y}")
print('\n')

x = x + y
y = x - y
x = x - y

print(f"After swapping The value of x is {x}")
print(f"After swapping The value of y is {y}")