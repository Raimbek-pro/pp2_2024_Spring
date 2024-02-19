from datetime import datetime, timedelta


current_date = datetime.now()


yestersay = current_date - timedelta(days=1)
tomorrow=current_date+timedelta(days=1)

print("Current Date:", current_date.strftime("%Y-%m-%d"))
print("Yesterday", yestersay.strftime("%Y-%m-%d"))
print("Tomorrow",tomorrow.strftime("%Y-%m-%d"))
