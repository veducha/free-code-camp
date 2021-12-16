def add_time(startTime, duration, day=None):
    time = startTime.split()[0]
    xM = startTime.split()[1]

    if xM == 'AM':
        period = 0
    elif xM == 'PM':
        period = 1

    # Reading input and converting to minutes
    hour = int(time.split(':')[0])
    hour = hour*60 + period * 12 * 60
    minu = int(time.split(':')[1])

    hourDur = int(duration.split(":")[0])
    hourDur = hourDur*60
    minuDur = int(duration.split(":")[1])

    startTime = hour + minu
    duration = hourDur + minuDur

    # End time in minutes
    endTime = startTime + duration

    # Computing end hour, minutes, how many days after, and AM or PM (period)

    endMinu = endTime % 60
    endHour = endTime // 60
    daysAfter = endHour // (24)
    periodAfter = (endHour % 24) // 12

    # Converting hours to 12-hour clock format
    endHour = endHour % 12

    # Renaming period to AM or PM
    if periodAfter == 0:
        per = "AM"
    elif periodAfter == 1:
        per = "PM"

    # String to display clock
    # Ensuring it displays minutes as 04 instead of 4
    if endMinu < 10:
        endMinu = "0"+str(endMinu)

    if endHour == 0:
        endHour = 12

    endClock = str(endHour)+":"+str(endMinu)+" "+per

    # Output logic depending whether day is present or not
    if day is not None:

        day = day[0].upper() + day[1:].lower()

        numb2days = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday',
                     3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'}
        days2numb = {'Monday': 0, 'Tuesday': 1, 'Wednesday': 2,
                     'Thursday': 3, 'Friday': 4, 'Saturday': 5, 'Sunday': 6}

        dayNumb = days2numb[day]
        endDay = numb2days[(dayNumb+daysAfter) % 7]

        if daysAfter == 0:
            return endClock+", " + endDay
        elif daysAfter == 1:
            return endClock+", "+endDay + " (next day)"
        elif daysAfter > 1:
            return (endClock+", " + endDay + f" ({daysAfter} days later)")

    elif day is None:
        if daysAfter == 0:
            return endClock
        elif daysAfter == 1:
            return endClock + " (next day)"
        elif daysAfter > 1:
            return endClock + f" ({daysAfter} days later)"


# add_time("11:30 PM", "50:01", "monday")
