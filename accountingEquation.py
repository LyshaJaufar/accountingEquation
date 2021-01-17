from sys import argv, exit
import csv

# Check for command-line args
if len(argv) != 2:
    print("Error")
    exit(1)

# Open the csv file
database = open(argv[1], "r")

# Answer Sheet
file = open('Accounting Equation - Answer Sheet.csv', 'w')
if (file == None):
    exit(1)

# Create DictReader
reader = csv.DictReader(database)

# Write the fieldnames/column names in row 0
for i in range(len(reader.fieldnames)):
    file.write(reader.fieldnames[i] + ',')
file.write("\n")

for row in reader: 
    # Variables for names of each column
    assets = row['Assets'].lower()
    liabilities = row['Liabilities'].lower()
    caital = row['Capital'].lower()

    # Assets
    if assets == "":
        liabilities = int(input("Liabiilties: "))
        capital = int(input("Capital: "))
        assets = capital + liabilities


    # Liabilities
    if liabilities == "":
        assets = int(input("Assets: "))
        capital = int(input("Capital: "))
        liabilities = assets - capital


    # Capital
    if capital == "":
        assets = int(input("Assets: "))
        liabilities = int(input("Liabiilties: "))
        capital = assets - liabilities

    file.write(assets + ",")
    file.write(liabilities + ",")
    file.write(capital + "\n") 