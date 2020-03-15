import csv

#Task 1
# When we use WITH a file is closed as soon as you finished using with.
# This means that we can't continue using the file as it is closed.
# We have to read the file and save our data so we can continue using it by creating a new list with our data from the csv file
my_data = []
with open('Sales.csv', 'r') as csv_file:
    spreadsheet = csv.DictReader(csv_file)

    for row in spreadsheet:
        my_data.append(row)


#Task 2
sales = []
for row in my_data:
    Sales_sum = int(row['sales'])
    sales.append(Sales_sum)

#Task 3
print('The total sum of the sales for 2018 is {}.'.format(sum(sales)))

#Task 4
print('The average sale per month for 2018 is {}.'.format(round(sum(sales) / len(sales), 2)))

#Task 5

## a function to get the month that is associated with the value provided
def get_month(My_value):
    for row in my_data:
        temp_value = int(row['sales'])
        if My_value == temp_value:
            return row['month']

## get the minimum value of sales and the corresponding month
My_minimum = min(sales)
min_month = get_month(My_minimum)
print('The minimum sales during 2018 is for the month of {} and is £{}.'.format(min_month, My_minimum))

## get the maximum value of sales and the corresponding month
My_maximum = max(sales)
max_month = get_month(My_maximum)
print('The maximum sales during 2018 is for the month of {} and is £{}.'.format(max_month, My_maximum))


