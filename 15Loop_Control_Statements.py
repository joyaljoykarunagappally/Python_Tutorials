# Loop Control Statements = change a loops execution from its normal sequences.

# break = used to terminate the Loop entirely
# continue = skips the next iteration for the loop
# pass = does nothing, act as a placeholder


# while True:
#     name = input("Enter Name : ")
#     if name != "":
#         break

# phone_number = "1234-5678-90"

# for i in phone_number:
#     if i == "-":
#         continue
#     print(i, end="")

for i in range(1, 20):
    if i == 9:
        pass
    else:
        print(i)
