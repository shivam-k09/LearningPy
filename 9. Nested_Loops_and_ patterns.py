print("Rectangular pattern of symbol")

row = int(input("How many rows? : "))
column = int(input("How many columns? : "))
sym = input("Which symbol to use? :")

for i in range(row):
    for j in range(column):
         print(sym, end="")
    print()