def comp(time1, time2):
    if time1.year != time2.year:
        if time1.year < time2.year:
            return "first time is older"
        else:
            return "second time is older"

    elif time1.month != time2.month:
        if time1.month < time2.month:
            return "first time is older"
        else:
            return "second time is older"

    elif time1.day != time2.day:
        if time1.day < time2.day:
            return "first time is older"
        else:
            return "second time is older"

    elif time1.hour != time2.hour:
        if time1.hour < time2.hour:
            return "first time is older"
        else:
            return "second time is older"

    elif time1.min != time2.min:
        if time1.min < time2.min:
            return "first time is older"
        else:
            return "second time is older"

    elif time2.sec < time1.sec:
        return "second time is older"
    else:
        return "first time is older"
