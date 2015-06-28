class School(object):

    def __init__(self, schoolName):
        self.schoolName = schoolName
        self.db = {}

    def add(self, studentName, grade):
        if self.db.has_key(grade):
            self.db[grade].add(studentName)
        else:
            self.db[grade] = {studentName}

    def grade(self, n):
        if self.db.has_key(n):
            return self.db[n]
        else:
            return set()

    def sort(self):
        return sorted((grade, tuple(sorted(students)))
            for grade, students in self.db.items())

if __name__ == '__main__':
    school = School("Haleakala Hippy School")

    students = [
        (3, ("Kyle",)),
        (4, ("Christopher", "Jennifer",)),
        (6, ("Kareem",))
    ]

    for grade, students_in_grade in students:
        for student in students_in_grade:
            school.add(student, grade)

    result = school.sort()
    result_list = list(result.items() if hasattr(result, "items") else result)

    print result
    print result_list

