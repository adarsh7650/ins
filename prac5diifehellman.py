p = 23
g =9

print("The value of p is ",p)
print("The value of g is ",g)

a=4
print("Secret number of ALice is ", a)
x=int(pow(g,a,p))

b=6
print("Secret number of Bob is " ,b)
y = int(pow(g,b,p))


ka=int(pow(y,a,p))
kb =int(pow(x,b,p))

print("Secret key of Alice is ", ka)
print("Secret key of Bob is ", kb)