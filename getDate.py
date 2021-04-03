from datetime import datetime


def getDate():
    days = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    ]
    time = datetime.now()
    time = time.strftime(f"{days[time.weekday()]}, %d %b %Y")
    return time


print(getDate())
