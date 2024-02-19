from datetime import datetime

# Input two dates as strings
date_str1 = input("Enter the first date (YYYY-MM-DD HH:MM:SS): ")
date_str2 = input("Enter the second date (YYYY-MM-DD HH:MM:SS): ")

# Convert the input strings to datetime objects
date_format = "%Y-%m-%d %H:%M:%S"
date1 = datetime.strptime(date_str1, date_format)
date2 = datetime.strptime(date_str2, date_format)

# Calculate the difference between the two dates
time_difference = date2 - date1

# Convert the time difference to seconds
difference_in_seconds = time_difference.total_seconds()

# Display the result
print("Difference between the two dates in seconds:", difference_in_seconds)
