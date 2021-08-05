# 2.10  Exercises
# Date 8/4/2021
"""
Exercise 1
Repeating my advice from the previous chapter, whenever you learn a new feature,
you should try it out in interactive mode and make errors on purpose to see what
goes wrong.
"""

# We’ve seen that n = 42 is legal. What about 42 = n?
# 42 = n
"""
  File "<input>", line 1
    42 = n
    ^
SyntaxError: cannot assign to literal
# Obviously, we can't assign numbers to a literal
"""

# How about x = y = 1?
x = y = 1
print("x = ", x)
print("y = ", y)
"""
x =  1
y =  1
"""

# In some languages every statement ends with a semi-colon, ;. What happens if
# you put a semi-colon at the end of a Python statement?
print("testing");
"""
testing
# the solution has no difference, but Python doesn't need it
"""

# What if you put a period at the end of a statement?
# print("testing").
"""
    print("testing").
                     ^
SyntaxError: invalid syntax
# We can't add a period at the end of a statement. 
# period or the dot allows you to choose the suggested methods (functions) and 
properties (data) of objects.
"""

# In math notation you can multiply x and y like this: x y. What happens if
# you try that in Python?
x = y = 1
print(xy)
"""
    print(xy)
NameError: name 'xy' is not defined
# We must put * between x and y.
"""
