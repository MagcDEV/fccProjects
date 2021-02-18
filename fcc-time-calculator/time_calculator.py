def add_time(start, duration, weekday="None"):
    import re
    import datetime
    if weekday == "None":
        old_day = "Monday"
    else:
        old_day = weekday

    old_day = weekday
    old_day = old_day.lower()
    am_pm = re.split("\s", start)[1]
    hours_minutes = re.split("\s", start)[0]
    hour = int(re.split(":", hours_minutes)[0])
    minutes = int(re.split(":", hours_minutes)[1])

    if am_pm == "PM":
        hour += 12

    add_hours = int(re.split(":", duration)[0])
    add_minutes = int(re.split(":", duration)[1])
    weekday_num = 1

    if old_day == "monday":
        weekday_num = 1
    elif old_day == "tuesday":
        weekday_num = 2
    elif old_day == "wednesday":
        weekday_num = 3
    elif old_day == "thursday":
        weekday_num = 4
    elif old_day == "friday":
        weekday_num = 5
    elif old_day == "saturday":
        weekday_num = 6
    elif old_day == "sunday":
        weekday_num = 7

    current_time = datetime.datetime(2020, 6, weekday_num, hour, minutes, 0)
    new_time = current_time + \
        datetime.timedelta(hours=add_hours, minutes=add_minutes)
    am_pm = new_time.strftime("%p")

    if new_time.hour > 12:
        new_hour = new_time.hour - 12
    elif new_time.hour == 0:
        new_hour = 12
    else:
        new_hour = new_time.hour

    new_minutes = new_time.minute

    day_pass = ""

    if new_time.day - current_time.day == 1:
        day_pass = " (next day)"
    elif (new_time.day - current_time.day) > 1:
        day_pass = " " + \
            "(" + str(new_time.day - current_time.day)+" days later)"

    if weekday == "None":
        return (str(new_hour) + ":" + ("00" + str(new_minutes))[-2:] + " " + am_pm + day_pass)
    else:
        return (str(new_hour) + ":" + ("00" + str(new_minutes))[-2:] + " " + am_pm + ", " + new_time.strftime("%A") + day_pass)


print(add_time("2:59 AM", "24:00", "saturDay"))
