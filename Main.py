# A program that generates random excel data in a .csv file
from os import _exit as stop
from Errors import error_stop as errstop
from Details import Details as dtls

# Variables
stopping_row = 0
data = []

try:
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

details = dtls()
for i in range(stopping_row + 1):
    details.randomise()

    temp = []

    temp.append(i + 1)
    temp.append(details.fname)
    temp.append(details.lname)
    temp.append(details.age)
    temp.append(details.city)
    temp.append(details.owed)

    data.append(temp)

# Write to the CSV File
with open("Result.csv", "w+") as csv:
    # Print the headings
    csv.write("ID, first_name,last_name,age,city,amount_owed\n")

    # From 1 to the index provided
    for i in range(0, stopping_row):
        for j in range(0, 6):
            csv.write(f"{data[i][j]},")
        csv.write("\n")
