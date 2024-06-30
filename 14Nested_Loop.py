#Nested Loop = The "inner Loop" finish all its iterations before finishing
#               one iteration of the "outer loop"

rows = int(input("Please Enter the Rows : "))
columns = int(input("Please Enter the Columns : "))
symbol = input("Please enter a symbol : ")

for i in range(rows):
    for j in range(columns):
        print(symbol, end="")           #  end = ""  is used to privent printing a new line
    print()
