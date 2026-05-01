# Count the number of instances of a chosen day of the week in a month

import calendar

def count_days(year, month, whichday):
    count = 0
    weekes = calendar.monthcalendar(year, month)

    for week in weekes:
        if week[whichday] != 0:
            count += 1
    return count

instace_year = 2025
instance_month = 12
instance_day = 0

instances = count_days(instace_year, instance_month, instance_day)

print(instances)