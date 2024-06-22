name = input("What is your name : ")
age = int(input("How old are you : "))              #type casting with input
height = float(input("How tall are you : "))

age = age+1     #Only works where the input is int. defaulty it become str

print("Hello "+name+".")
print("You are "+str(age)+" years old.")   #works only convert it to string
print("You are "+str(height)+"cm tall.")
