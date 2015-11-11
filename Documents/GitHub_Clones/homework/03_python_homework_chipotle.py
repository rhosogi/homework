'''
Python Homework with Chipotle data
https://github.com/TheUpshot/chipotle
'''

'''
BASIC LEVEL
PART 1: Read in the file with csv.reader() and store it in an object called 'file_nested_list'.
Hint: This is a TSV file, and csv.reader() needs to be told how to handle it.
      https://docs.python.org/2/library/csv.html
'''
import csv
with open('chipotle.tsv', 'rb') as csvfile:
    file_nested_list = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in file_nested_list:
        print ',' .join(row)
        


'''
BASIC LEVEL
PART 2: Separate 'file_nested_list' into the 'header' and the 'data'.
'''
import csv
with open('chipotle.tsv', 'rb') as csvfile:
    file_nested_list = csv.reader(csvfile, delimiter=' ', quotechar='|')
    
rownum=0
for row in file_nested_list:
    if rownum == 0:
        header=row
    else:
        column=0
        for col in row:
            print '%-8s: %s'(header[column], col)
            column+=1
        rownum+=1
    


'''
INTERMEDIATE LEVEL
PART 3: Calculate the average price of an order.
Hint: Examine the data to see if the 'quantity' column is relevant to this calculation.
Hint: Think carefully about the simplest way to do this!  Break the problem into steps and then code each step
'''
import csv
with open ('chipotle.tsv', 'rb') as csvfile:
    file_nested_list = csv.reader(csvfile, delimiter= ' ', quotechar= '|')
    class Order:
        'Order count for Chipotle data'
        ordCount = 0
        
    def __init__ (self, number, price):
        
        def writerows(self, rows):
            for row in rows:
                self.writerow(row)
            print row(0)


'''
INTERMEDIATE LEVEL
PART 4: Create a list (or set) of all unique sodas and soft drinks that they sell.
Note: Just look for 'Canned Soda' and 'Canned Soft Drink', and ignore other drinks like 'Izze'.
'''
#[your code here]

'''
ADVANCED LEVEL
PART 5: Calculate the average number of toppings per burrito.
Note: Let's ignore the 'quantity' column to simplify this task.
Hint: Think carefully about the easiest way to count the number of toppings!
'''

#[your code here]


'''
ADVANCED LEVEL
PART 6: Create a dictionary in which the keys represent chip orders and
  the values represent the total number of orders.
Expected output: {'Chips and Roasted Chili-Corn Salsa': 18, ... }
Note: Please take the 'quantity' column into account!
Optional: Learn how to use 'defaultdict' to simplify your code.
'''

#[your code here]


'''
BONUS: Think of a question about this data that interests you, and then answer it!
'''

#[your code here]
