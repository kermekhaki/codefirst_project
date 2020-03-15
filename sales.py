import csv

with open('Sales.csv', 'r') as csv_file:
    spreadsheet = csv.DictReader(csv_file)

    sales = []

    for row in spreadsheet:
       # print(row.keys()) gives names of columns
        Sales_sum = row['sales']
        sales.append(Sales_sum)
