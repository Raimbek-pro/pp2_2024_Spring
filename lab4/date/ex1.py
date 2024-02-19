from datetime import datetime, timedelta


current_date = datetime.now()


new_date = current_date - timedelta(days=5)


print("Current Date:", current_date.strftime("%Y-%m-%d"))
print("Date after Subtracting Five Days:", new_date.strftime("%Y-%m-%d"))
