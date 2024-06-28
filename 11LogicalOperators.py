#Logical Operators(and, or, not) are used for checking more than 1 conditions


temp = int(input("Enter the temperature in Celsius : "))

if temp >= 0 and temp <= 30:
    print("The temperature is good today!")
    print("Go Outside!")
elif temp < 0 or temp > 30:
    print("The temperature is bad today!")
    print("Stay Inside!")

#not is used for get the opposite result of the condition
'''
if not(temp >= 0 and temp <= 30):
    print("The temperature is bad today!")
    print("Stay Inside!")
elif not(temp < 0 or temp > 30):
    print("The temperature is good today!")
    print("Go Outside!")
'''