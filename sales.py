import csv
import matplotlib.pyplot as plt
import seaborn as sb

#Task 1 & 2 (the answers!)))
my_data = []
with open('Sales.csv', 'r') as csv_file:
    spreadsheet = csv.DictReader(csv_file)

    for row in spreadsheet:
        my_data.append(row)

#Task 3
sales = []
for row in my_data:
    Sales_sum = int(row['sales'])
    sales.append(Sales_sum)

print('The total sum of the sales for 2018 is £{}.'.format(sum(sales)))

print ('\n')

#Task 4
print('The average sale per month for 2018 is £{}.'.format(round(sum(sales) / len(sales), 2)))

print ('\n')

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

print ('\n')

## get the maximum value of sales and the corresponding month
My_maximum = max(sales)
max_month = get_month(My_maximum)
print('The maximum sales during 2018 is for the month of {} and is £{}.'.format(max_month, My_maximum))

print ('\n')

#Task 6
# Calculating monthly balance as percentage of sales

def balance_percent(myDict):
    balance = int(myDict['sales']) - int(myDict['expenditure'])
    if balance < 0:
        return 0
    else:
        percentage = (balance / int(myDict['sales']))*100
        return round(percentage, 2)


print('Balance as a percentage of the sales:')
for row in my_data:
    month = row['month']
    balance = balance_percent(row)
    print('For {}: {}%'.format(month, balance))


print('\n')
print('Monthly sales chart:')

sales = list(map(lambda x: int(x['sales']), my_data))
month = list(map(lambda x: x['month'], my_data))

sb.lineplot(month, sales, sort=False)
plt.xlabel('Month')
plt.ylabel('Sales in pounds')
plt.title('Sales per month for 2018')
#plt.savefig('fig1.png')
plt.show()

