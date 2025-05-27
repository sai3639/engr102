
# Date: 14/9/2021
#

x = 1
y = 10
z = 0
z += x
print(z)

x += 1
y *= x
z += x
z += x
z += y
print(z)

x = 1
z = 0
z += x
z += x
y = 10
x = y
y *= x
z += y

print(z)
y = 10
y *= x
y *= x
x = y
y *= x
y *= x
z = 0
z += y
print(z)

y = 10 
x = 1
x += 1
x += 1
x += 1
x += 1
x += 1
y *= x

x = 1
x += 1
x += 1
x += 1
x += 1
x += 1 
x += 1
x += 1
y += x
x = y
z = 0
z += x

y = 10
x = 1
x += 1
y *= x
x = y
y *= x
z += y

y = 10
x = y
y *= x
y *= x
x = 1
x += 1
y *= x
z += y
print(z)
