from os import _exit as stop
from Errors import error_stop as errstop
from Details import Details as dtls

# The stopping row for the data.
stopping_row = 0
# The array holding the data.
data = []

try:
    # Get user input for the row to stop generating data at.
    stopping_row = int(input("Stopping Row: "))
except KeyboardInterrupt:
    # Exit the program on ctrl+C
    print("\nExiting...")
    stop(0)
except ValueError:
    # Use the user-defined "errstop" method to exit the program.
    errstop("You didn't enter a number.")
except Exception:
    # Use the user-defined "errstop" method to exit the program.
    errstop("Unspecified Error.")
else:
    # Display that the program is writing to the file.
    print("Writing to file...")

# Create the Details (with the alias "dtls") object
details = dtls()

# Loop from 0 to the stopping row
# (+1 to account for zero-based indexes)
for i in range(stopping_row + 1):
    details.randomise()

    # Declare a temporary array called "row"
    row = []

    # Append the index to the array
    row.append(i + 1)
    row.append(details.uniqueID) # Unique ID
    row.append(details.fname) # First Name
    row.append(details.lname) # Last Name
    row.append(details.age) # Age
    row.append(details.city) # City
    row.append(details.owed) # Amount Owed

    # Append the "row" array to the "data" array
    data.append(row)

# Write to the CSV File
with open("Data.csv", "w+") as csv:
    # Print the headings
    csv.write("ID, first_name,last_name,age,city,amount_owed\n")

    # From 0 to the index provided
    for i in range(0, stopping_row):
        for j in range(0, 6):
            # Write the data generated into the CSV file.
            csv.write(f"{data[i][j]},")
        # Skip to the next line.
        csv.write("\n")
