from datetime import datetime

class Date:
    def __init__(self, dateString):
        self.dateString = dateString
        self.year = "year"
        self.month = "month"
        self.day = "day"
        self.hour = "hour"
        self.minute = "minute"
        self.second = "second"
        self.millisecond = "millisecond"
    
    def parseDateString(self, dateString):
        split = dateString.split("-")
        self.year = split[0]
        self.month = split[1]
        getDay = split[2].split("T")
        self.day = getDay[0]
        hourAndMinute = getDay[1].split(":")
        self.hour = hourAndMinute[0]
        self.minute = hourAndMinute[1]
        sec = split[3].split(":")
        self.second = sec[0]
        self.millisecond = sec[1]
    
    def useDatetime(self, str):
        date_obj = datetime.strptime(str, "%Y-%m-%dT%H:%M-%S:%f")
        print(date_obj)



date = Date('2022-01-06T12:14-05:00')
date.parseDateString(date.dateString)
print(date.hour)
date.useDatetime(date.dateString)
