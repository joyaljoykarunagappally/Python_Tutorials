import time

# for loop = a statement that will execute a block of code a limited of time
#       while = Unlimited
#       for =   limited

#for i in range(10):            #prints 0 1 2 3 4 5 6 7 8 9
#    print(i)

#for i in range(50,100,2):       #prints 50 52 54 56....98
#    print(i)                    #starts in 50 ends in 100 with an iteration of 2
#                                #50 is implicit and 100 is explicit

#for i in "JOYAL":                #prints J O Y A L
#    print(i)

for seconds in range(10,0,-1):
    print(seconds)
    time.sleep(1)
print("HAPPY NEW YEAR")
