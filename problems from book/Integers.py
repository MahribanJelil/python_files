# 2
# L = int(input("Enter: ")) 
# a = L//1000
# print(L, "kg", " = ", a, "ton")

# 3
# L = int(input("Enter: ")) 
# a = L//1024
# print(L, "b", " = ", a, "kb")

# 7
# L = int(input("Enter two digit number: "))
# a = L//10
# b = L%10
# x = a + b
# y = a * b
# print("Sum of two digit: ", x)
# print("Product of two digit: ", y)

# 8
# L = int(input("Enter two digit number: "))
# a = L//10
# b = L%10
# c = 10*b + a
# print(c)

# 10
# L = int(input("Enter three digit number: ")) 
# a = L%10
# b = (L//10)%10
# c = 10*a + b
# print(c)

# 11
# L = int(input("Enter three digit number: ")) 
# a = L//100
# b = (L//10)%10
# c = L%10
# x = a + b + c
# y = a * b * c
# print("Sum of digits: ", x)
# print("Product of digits: ", y)

# 12
# L = int(input("Enter three digit number: ")) 
# a = L//100
# b = (L//10)%10
# c = L%10
# x = 100*c + 10*b + a
# print("Result: ", x)

# 13
# L = int(input("Enter three digit number: ")) 
# a = L//10
# b = L%10
# x = 100*b + a
# print("Result: ", x)

# 15
# L = int(input("Enter three digit number: ")) 
# a = L//100
# b = (L//10)%10
# c = L%10
# x = 100*b + 10*a + c
# print("Result: ", x)

# 17
# L = int(input("Enter three digit number: "))
# x = (L%1000)//100
# print("Result: ", x)

# 18
# L = int(input("Enter three digit number: "))
# x = L//1000
# print("Result: ", x)

# 19
# N = int(input("Please enter amount of seconds: "))
# x = N//60
# print("Amount of minutes: ", int(x), "min.")

# 20
# N = int(input("Please enter amount of seconds: "))
# x = N//3600
# print("Amount of hours: ", int(x), "hours")

# 22
# N = int(input("Please enter amount of seconds: "))
# x = N%3600
# print("Amount of seconds passed from the last hour: ", int(x), "sec.")

# 23
# N = int(input("Please enter amount of seconds: "))
# x = (N%3600)//60
# print("Amount of minutes passed from the last hour: ", int(x), "min.")

# 25
# week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
# x = int(input("Enter your day: "))
# a = (x + 3)%7
# result = week[a]
# print("Today is ", result)

# 26
# week = [" ", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
# x = int(input("Enter your day: "))
# a = (x % 7) + 1
# result = week[a]
# print("Today is ", result)

# 27
# week = [" ", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
# x = int(input("Enter your day: "))
# a = (x + 5) % 7
# result = week[a]
# print("Today is ", result)

# 29
# a = int(input("Enter A: "))
# b = int(input("Enter B: "))
# c = int(input("Enter C: "))
# x = (a * b)//(c*c)
# y = (a * b)%(c*c)
# print("Amount of squares placed on the rectangle is ", x)
# print("Area of unused part of the rectangle is ", y)

# 30
a = int(input("Enter number of year: "))
x = (a // 100) + 1
print("Number of century is ", x, "th")
