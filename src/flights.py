'''
We will write at least the following functions to implement our Flights program:

data(filename) -> returns a matrix of all the data contained in a .csv file, given the filename
print_table(data) -> prints a table containing data from the given matrix
print_table_row(data, cell_width) -> prints a row of table cells with a given width
column_widths(data) -> returns a dictionary {column header: column width}

The last three functions above should be implemented in their own separate file, since
this code could actually be used for programs other than this Flights program. It makes
a lot of sense to close it off so that it could be imported into other files if need be.
Let's call this new file "tables.py".

When this code is completed, you'll import it into this file and write your Flights program, 
which you should be able to do on your own.
'''

from tables import *
import os
import operator


dir_path = os.path.dirname(os.path.realpath(__file__))
text_file = open(dir_path + "\\flights.csv", "r")

data = []
for line in text_file:
    data.append(line.strip().split(","))

def print_menu():
    print("Choose one of the options to sort by:")
    options = ["Airline", "Flight", "Arrival time", "Departure time", "Fare", "Quit"]
    for i in range(0,len(options)):
        print(str(i + 1) + " -- " + options[i])

def get_data():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    text_file = open(dir_path + "\\flights.csv", "r")

    data = []
    for line in text_file:
        data.append(line.strip().split(","))
    return data

def main():
    data = get_data()
    while True:
        print_menu()
        response = input("~> ")
        if response == "6":
            return
        i = int(response) - 1
        sort = data[:1] + sorted(data[1:],key=operator.itemgetter(i))
        print_table(sort)

main()

'''
def flights_menu():
    response = ""
    while response.lower() != "quit":
        response = input("Select a category you would like to sort by: Airline, Flight, Arrives, Departs, Fare ").lower()  
        i = None
             
        if response == "airline":
            i = 0
        elif response == "flight":
            i = 1
        elif response == "arrives":
            i = 2
        elif response == "departs":
            i = 3
        elif response == "fare":
            i = 4
        else:
            continue
        sort = data[:1] + sorted(data[1:],key=operator.itemgetter(i))
        
        print_table(sort)

#flights_menu()


# text_file.close()

# print_table(data)
'''
