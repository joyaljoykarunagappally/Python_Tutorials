#Type Casting = Convert the datatype of a value to another Datatype

x = 1             #int
y = 3.0           #float
z = "5"           #string


int(z)          #converted to int

print(z)

print(float(x))     #converted to float
print(str(y))       #converted to string

# concatination of str with int is not possible. first convert that int to str then proceed
print("hello "+str(z))