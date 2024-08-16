# def xyz():
#     print("hello everyone")
# xyz()
# xyz()
# xyz()
# xyz()

# x=int(input("Enter any first number "))
# x2=int(input("Enter any second number "))


# def add(num1, num2):
#     """Add two numbers"""
#     num3 = num1 + num2
#     print(f"The addition of {num1} and {num2} results {num3}.")
#     # return num3

# add(x,x2)
# num1, num2 = 5, 15
# ans = add(x, x2)
# print(f"The addition of {x} and {x2} results {ans}.")


# some more functions
# def is_prime(n):
#     if n in [2, 3]:
        
#         return True
#     if (n == 1) or (n % 2 == 0):
#         return False
#     r = 3
#     while r * r <= n:
#         if n % r == 0:
#             return False
#         r += 2
#     return True
# print(is_prime(9), is_prime(79))

# A simple Python function to check
# whether x is even or odd
# def evenOdd(x):
#     if (x % 2 == 0):
#         print("even")
#     else:
#         print("odd")


# # Driver code to call the function
# evenOdd(2)
# evenOdd(3)
# evenOdd(30)

# def add(a,b):
#     c = a + b
#     return c

# a, b = 1, 2
# ans = add(a, b)
# print("the addition of {a} and {b} is ")

# def add(num1: int, num2: int) -> int:
#     """Add two numbers"""
#     num3 = num1 + num2

#     return num3

# # Driver code
# num1, num2 = 5, 15
# ans = add(num1, num2)
# print(f"The addition of {num1} and {num2} results {ans}.")


# def add(a1,b1):
#     c=a1+b1

#     return c

# a1=100
# b1=50
# ans =add(a1,b1)
# print("the answer is",ans)

# def multiplication(a1,a2):
#     c=a1*a2
#     return c

# a1,a2=45,1
# ans=multiplication(a1,a2)
# print(f"the multiplication of a1 and a2 is :",ans)


# def trry():
#         print("gaurav negi eggs degi  ")
# trry()
# trry()


# def xyz():
#         print("hello everyone")
# xyz()
# xyz()
# xyz()
# xyz()

# def add(num1, num2):

#         num3 = num1 - num2

#         return num3

# num1, num2 = 12, 12
# ans = add(num1, num2)
# print("the addition of num1 and num2 is :",ans)



# some more functions
# def is_prime(n):
#     if n in [2, 3]:
#         return True
#     if (n == 1) or (n % 2 == 0):
#         return False
#     r = 3
#     while r * r <= n:
#         if n % r == 0:
#             return False
#         r += 2
#     return True
# print(is_prime(78), is_prime(79))

# def evenOdd(x):
#     if (x % 2 == 0):
#         print("even")
#     else:
#         print("odd")


# # Driver code to call the function
# evenOdd(20)
# evenOdd(3)


# Python program to demonstrate
# default arguments
# def myFun(x=100, y=50):
#     print("x: ", x) 
#     print("y: ", y)


# # Driver code (We call myFun() with only
# # argument)
# myFun(10,500)

# Python program to demonstrate Keyword Arguments
# def student(firstname='gaurav', lastname='hello'):
#     print(firstname, lastname)


# # Keyword arguments
# # student(firstname='Geeks', lastname='Practice')
# student(lastname='Practice', firstname='Geeks')
# student()


# def nameAge(name, age):
#     print("Hi, I am", name)
#     print("My age is ", age)


# # You will get correct output because 
# # argument is given in order
# # print("Case-1:")
# # nameAge("Suraj", 27)
# # You will get incorrect output because
# # argument is not in order
# print("\nCase-2:")
# nameAge(age=27, name="Suraj")


# Python program to illustrate
# *args for variable number of arguments
# def myFun(*kuchhbhi):
#     for arg in kuchhbhi:
#         print(arg)


# myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks','Hello', 'Welcome', 'to', 'GeeksforGeeks')
# def myFun(**kwargs):
#     for key, value in kwargs.items():
#         print("%s == %s" % (key, value))


# # Driver code
# myFun(first='Geeks', mid='for', last='Geeks')

# """Function to check if the number is even or odd"""
# def evenOdd(x):
#     """Function to check if the number is even or odd"""
    
#     if (x % 2 == 0):
#         print("even")
#     else:
#         print("odd")


# # Driver code to call the function
# print(evenOdd.__doc__)

# def f1():
#     s = 'I love GeeksforGeeks'
  
#     def f2():
#         print(s)
        
#     f2()

# # Driver's code
# f1()

# def cube(x): return x*x*x

# cube_v2 = lambda x : x*x*x

# # print(cube(7))
# print(cube_v2(7))


# def factorial(n):
#     if n == 0:  
#         return 1
#     else:
#         return n * factorial(n - 1)
# print(factorial(4))

# print(factorial(5))
# print(factorial(3))




# oops in python lang




















# Python program to demonstrate
# default arguments
# def myFun(x, y=50):
#     print("x: ", x)
#     print("y: ", y)


# # Driver code (We call myFun() with only
# # argument)
# myFun(100)



# Python program to demonstrate Keyword Arguments
# def student(firstname, lastname):
#     print(firstname, lastname)


# # Keyword arguments
# student(firstname='Geeks', lastname='Practice')
# student(lastname='Practice', firstname='Geeks')

# def myFun(*argv):
#     for arg in argv:
#         print(arg)


# myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')

# def myFun(**kwargs):
#     for key, value in kwargs.items():
#         print("%s == %s" % (key, value))


# # Driver code
# myFun(first='Geeks', mid='for', last='Geeks')



# def f1():
#     s = 'I love GeeksforGeeks'
#     print("hello everyone")
#     def f2():
#         print('hello ravi')
#         print(s)
        
#     f2()

# # Driver's code
# f1()

# Python code to illustrate the cube of a number
# using lambda function
# def cube(x): return x*x*x

# cube_v2 = lambda x : x*x*x

# # print(cube(7))
# print(cube_v2(7))

# def square_value(num):
#     """This function returns the square
#     value of the entered number"""
#     return num**2


# print(square_value(12))
# print(square_value(-4))

# Here x is a new reference to same list lst
# def myFun(x):
#     x[0] = 20


# # Driver Code (Note that lst is modified
# # after function call.
# lst = [10, 11, 12, 13, 14, 15]
# myFun(lst)
# print(lst)

# def myFun(x):
    
#     # After below line link of x with previous
#     # object gets broken. A new object is assigned
#     # to x.
#     x[0] = 200
#     x[1]=100
#     x[2]=300


# # Driver Code (Note that lst is not modified
# # after function call.
# lst = [10, 11, 12, 13, 14, 15]
# myFun(lst)
# print(lst)


# def myFun(x):
    
#     # After below line link of x with previous
#     # object gets broken. A new object is assigned
#     # to x.
#     x = 20


# # Driver Code (Note that x is not modified
# # after function call.
# x = 10
# myFun(x)
# print(x)


# def swap(x, y):
#     temp = x
#     x = y
#     y = temp

# # Driver code
# x = 2
# y = 3

# swap(x, y)
# print(x)
# print(y)


























































































































































