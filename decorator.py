import calendar

class Calendar():

    def __init__(self, year, month):
        self.year = year
        self.month = month

    def getCalendar(self):
        return calendar.month(self.year, self.month)

class PrintCalendar():

    def __init__(self, cal):
        self.cal = cal

    def showCalendar(self):
        print("Here is the calendar:\n" + self.cal.getCalendar())

if __name__ == "__main__":

    year = int(input("Enter year: "))
    month = int(input("Enter month: "))

    data = Calendar(year, month)
    cal = PrintCalendar(data)

    print(cal.showCalendar())



