from datetime import date
from datetime import date

date_input = input("Enter a date(YYYY-MM-DD):")

try:
    date_object = date.fromisoformat(date_input)
    print("The date is:", date_object)
    print("Today's date is:", date.today())
    difference =  date.today() - date_object
    print("The difference is:", difference)
    print("In seconds the difference is:", difference.total_seconds())
    print("In minutes the difference is:", difference.total_seconds() / 60)
    print("In hours the difference is:", difference.total_seconds() / 60 / 60)
    print("In days the difference is:", difference.total_seconds() / 60 / 60 / 24)
except ValueError:
    print ("Invalid format")