from datetime import datetime

now = datetime.now()


def getTime():
    return now.strftime("%H:%M:%S - %d/%m/%Y")


def getDate():
    return (
        now.year * 10000000000
        + now.month * 100000000
        + now.day * 1000000
        + now.hour * 10000
        + now.minute * 100
        + now.second
    )
