#Import the datetime module and display the current date
import datetime
x = datetime.datetime.now()
print(x)

#Return the year and name of weekday
import datetime
x = datetime.datetime.now()
print(x.year)
print(x.strftime("%A"))

#Creating Date Objects
import datetime
x = datetime.datetime(2025, 6, 29)
print(x)

#The strftime() Method
import datetime
x = datetime.datetime(2001, 12, 1)
print(x.strftime("%B"))