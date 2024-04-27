# A program that generates random excel data in a .csv file
from os import _exit as stop
from Errors import error_stop as errstop

# Variables
stopping_row = 0
stopping_column = 0
arr = []

try:
    stopping_column = int(input("Stopping Column"))
    stopping_row = int(input("Stopping Row: "))
except ValueError:
    errstop("You didn't enter a number.")
except Exception:
    errstop("Unspecified Error.")
    
# Write to the CSV File    
with open("Result.csv") as csv:
    for i in range(1, len(arr)):
        pass
    
    # From 1 to the index provided, instead of 1 to the index provided - 1 (Default)
    for i in range(1, stopping_row + 1):
        csv.write()
