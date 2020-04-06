import csv

class Date:

    def __init__(self,date):
        """
        pre date(str)
        """
        self.day = date[:2]
        self.month = date[3:5]
        self.year = date[6:]

    def __eq__(self,other):
        if self.day == other.day and self.month == other.month and\
        self.year == other.year:
            return True
        return False

    def __lt__(self, other):
        if int(self.year) > int(other.year):
            return False
        if  int(self.year) == int(other.year) and int(self.month) >\
         int(other.month):
            return False
        if  int(self.year) == int(other.year) and int(self.month) == \
        int(other.month) and int(self.day) >= int(other.day):
            return False
        return True

    def __str__(self):
        return "{}/{}/{}".format(self.day,self.month,self.year)


def is_earlier_or_equal(d1,d2):
    """
    pre d1(str) : date format xx/yy/zzzz
    pre d2(str) : date format xx/yy/zzzz
    retrun (bool) : d1 is earlier than d2
    """
    if int(d1[6:]) > int(d2[6:]):
        return False
    if  int(d1[6:]) == int(d2[6:]) and int(d1[3:5]) > int(d2[3:5]):
        return False
    if  int(d1[6:]) == int(d2[6:]) and int(d1[3:5]) == int(d2[3:5]) and\
     int(d1[:2]) > int(d2[:2]):
        return False
    return True


def total_death(filename,date):
    """
    pre file(str) : csv filename
    pre date(str) : date format xx/yy/zzzz
    return (int) : total of death
    """
    #read file and put data in a usable list
    data = []
    with open(filename, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter='-', quotechar='|')
        for row in spamreader:
            row = (row[0].split(";"))
            data.append(row)
    data.reverse()
    del data[-1]
    #count total of death until the chosen date
    count = 0
    country = data[0][6]
    for row in data:
        if is_earlier_or_equal(row[0],date) and row[6] == country:
            count += int(row[5])
        elif not is_earlier_or_equal(row[0],date):
            pass
        else:
            country = row[6]
            count += int(row[5])
    return count


def valid_dates(filename):
    """
    pre file(str) : csv filename
    return (list) : every dates in csv file
    """
    #read file and put data in a usable list
    data = []
    with open(filename, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter='-', quotechar='|')
        for row in spamreader:
            row = (row[0].split(";"))
            data.append(row)
    data.reverse()
    del data[-1]
    #put every dates in file in a list
    dates_class = []
    for row in data:
        if Date(row[0]) not in dates_class:
            dates_class.append(Date(row[0]))
    #sorte list
    dates_class = sorted(dates_class)
    #convert Dates objects to dates in strings
    dates = []
    for date in dates_class:
        dates.append(str(date))
    return dates

print(total_death("data.csv","04/03/2020"))
print(valid_dates("data.csv"))
