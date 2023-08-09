monthName = [
    " ",
    "Jan",
    "Feb",
    "Mar",
    "Apr",
    "May",
    "Jun",
    "Jul",
    "Aug",
    "Sep",
    "Oct",
    "Nov",
    "Dec",
]
monthDays = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


class Date:
    def get(self):
        while True:
            try:
                self.y = int(input("Year: "))
                while self.y < 1:
                    self.y = int(input("Year: "))

                self.m = int(input("Month: "))
                while self.m > 12 or self.m < 1:
                    self.m = int(input("Month: "))

                EndDay = monthDays[self.m]
                if self.m == 2 and self.kabise():
                    EndDay += 1
                self.d = int(input("Day: "))
                while self.d < 1 or self.d > EndDay:
                    print("Error")
                    self.d = int(input("Day: "))
                break
            except ValueError:
                print("invalid input")

    def __init__(self, a=1900, b=1, c=1):
        self.y = a
        self.m = b
        self.d = c

    def __str__(self):
        return f"{self.y}:{self.m}:{self.d}"

    def show(self):
        print(f"{self.y}/{self.m}/{self.d}")

    def show1(self):
        print(f"{self.d} - { monthName[self.m]} - {self.y}")

    def kabise(self):
        if self.y % 400 == 0:
            return True
        if self.y % 100 != 0 and self.y % 4 == 0:
            return True
        return False

    # _
    def rooz(self):
        s = 0
        for i in range(1, self.m):
            s = s + monthDays[i]
        s = s + self.d

        year = self.y - 1900

        roz = year * 365
        kab = year // 4
        s = roz + kab
        print(s)

        if self.kabise() and self.m > 2:
            s = s + 1

