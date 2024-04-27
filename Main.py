# A program that generates random excel data in a .csv file
from os import _exit as stop
from Errors import error_stop as errstop

# Variables
stopping_row = 0
stopping_column = 0
data = []

try:
    stopping_column = int(input("Stopping Column: "))
    stopping_row = int(input("Stopping Row: "))
except KeyboardInterrupt:    
    print("Exiting...")
    stop(0)
except ValueError:
    errstop("You didn't enter a number.")
except Exception:
    errstop("Unspecified Error.")
else:
    print("Writing to file...")

# Write to the CSV File    
with open("Result.csv") as csv:
    for i in data:
        for j in i:
            pass
            
            
    
    # From 1 to the index provided, instead of 1 to the index provided - 1 (Default)
    for i in range(1, stopping_row + 1):
        for j in range(1, stopping_column + 1):
            csv.write(data[i, j])
