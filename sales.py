import csv

#Task 1 & Task 2
with open('Sales.csv', 'r') as csv_file:
    spreadsheet = csv.DictReader(csv_file)

    sales = []

    for row in spreadsheet:
        #print(row.keys()) gives names of columns
        Sales_sum = int(row['sales'])
        sales.append(Sales_sum)

#Task 3
print('The total sum of the sales for 2018 is {}.'.format(sum(sales)))

#Task4
print('The average sale per month for 2018 is {}.'.format(round(sum(sales) / len(sales), 2)))




