from sys import argv, exit
import csv
import re

# Check for command-line args
if len(argv) != 2:
    print("Usage Error: python accountingEquation.py <number of calculations>")
    exit(1)

"""
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
file.write("\n")"""

# Answer Sheet
file = open('Accounting Equation - Answer Sheet.csv', 'w')
if (file == None):
    exit(1)

fieldnames = ['Assets', 'Liabilities', 'Capital']
for fieldname in fieldnames:
    file.write(fieldname + ",")
file.write("\n")

for i in range(int(argv[1])): 
    calculate = input("Enter which of the following you would like to calculate: Assets, Liabilities, Capital: ")

    # Assets
    if re.search("a(ssets)?", calculate, re.IGNORECASE):
        liabilities = int(input("Liabiilties: "))
        capital = int(input("Capital: "))
        assets = capital + liabilities


    # Liabilities
    if re.search("l(iabilities)?", calculate, re.IGNORECASE):
        assets = int(input("Assets: "))
        capital = int(input("Capital: "))
        liabilities = assets - capital


    # Capital
    if re.search("c(apital)?", calculate, re.IGNORECASE):
        assets = int(input("Assets: "))
        liabilities = int(input("Liabiilties: "))
        capital = assets - liabilities

    file.write(str(assets) + ",")
    file.write(str(liabilities) + ",")
    file.write(str(capital) + "\n") 