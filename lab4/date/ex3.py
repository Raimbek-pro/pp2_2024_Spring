from datetime import datetime

# Get the current date and time
current_datetime = datetime.now()

# Drop microseconds
rounded_datetime = current_datetime.replace(microsecond=0)

# Display the results
print("Current Date and Time:", current_datetime)
print("Date and Time without Microseconds:", rounded_datetime)
