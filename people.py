import courses

auxwn = 0


class People:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def email(self):
        print('{}.{}@email.gr'.format(self.first, self.last))

    @property
    def fullname(self):
        print('{} {}'.format(self.first, self.last))


class Student(People):

    def __init__(self, first, last, year):
        super().__init__(first, last)
        self.year = year

    def calcAM(self):
        global auxwn
        auxwn += 1

        am = '{}{}'.format(self.year % 2000, '{:0>4d}'.format(auxwn))
        return am

    @property
    def am(self):
        print(self.calcAM())


class Teachers(People):

    def __init__(self, first, last):
        super().__init__(first, last)
        self.coursesArray = []

    def addCourse(self, course):
        self.coursesArray.append(course)

    def removeCourse(self, course):
        removed = course.naco
        self.coursesArray.remove(course)
        print("{} was removed from {} {}'s courses".format(removed, self.first, self.last))

    @property
    def courses(self):
        print('{} {} is teaching:'.format(self.first, self.last))
        for i in self.coursesArray:
            print(i.naco)



