# Tuples = collection which is ordered and unchangeable used to
#           group together related data

student = ("Joyal", 21, "male")

print(student.count("Joyal"))       #prints the count of that value in the tuple
print(student.index("male"))        #print index of that value in the list


for x in student:
    print(x)

if "Joyal" in student:
    print("Joyal is here!")
