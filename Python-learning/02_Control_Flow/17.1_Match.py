# Olternative of  many if/else
day = 4
match day :
    case 1 :
        print("Saturday")
    case 2 :
        print("Sunday")
    case 3 :
        print("Monday")
    case 4 :
        print("Tuesday")
    case 5 :
        print("Wednesday")
    case 6 :
        print("Thursday")
    case 7 :
        print("Friday")

#Default_Value
day = 4
match day :
    case 6 :
        print("Today is saturday")      
    case 7 :
        print("Today is sunday")
    case _:
        print("Looking for OFF day")

#Combining value using pipe | operator
day = 7
match day :
    case 1 | 2 | 3 | 4 | 5 :
        print("Today is working day")
    case 6 | 7 :
        print("Today is weekeend")

#If Statements as Guards
month = 6
day = 5
match day :
    case 1 | 2 | 3 | 4 | 5 if month == 5 :
        print("This is a weekday in May")
    case 1 | 2 | 3 | 4 | 5 if month == 6 :
        print("This is a weekday in July")
    case _:
        print("No match found")