import people
import courses

stud_1 = people.Student('Nikos', 'Nikou', 2017)
stud_2 = people.Student('Menelaos', 'Neto', 2019)

cou_1 = courses.Courses('Java 1', '132')
cou_2 = courses.Courses('Java 2', '245')

tea_1 = people.Teachers('Hlias', 'Bretos')

tea_1.addCourse(cou_1)
tea_1.addCourse(cou_2)

tea_1.courses
tea_1.removeCourse(cou_1)
tea_1.courses
stud_1.am
stud_2.am
stud_2.email

