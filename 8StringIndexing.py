#indexing = [start:stop:step]

name="Joyal Joy"

first_name=name[0:5]                #first value is implisit index number and second is explicit count not index
#first_name=name[:5]                #default first value is index 0
print(first_name)

last_name=name[6:]                  #default last value is full string count not index
print(last_name)

funky_name=name[0:8:2]              #third value is the count of ignore step
#funky_name=nam[::3]                #default[0:9:x]
print(funky_name)

reversed_name = name[::-1]
print(reversed_name)