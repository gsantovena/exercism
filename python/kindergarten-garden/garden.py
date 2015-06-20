class Garden(object):


    plants_list = ["Clover", "Grass", "Radishes", "Violets"]

    def __init__(self, diagram, students = ["Alice", "Bob", "Charlie", "David", "Eve", "Fred", "Ginny", "Harriet", "Ileana", "Joseph", "Kincaid", "Larry"]):
        self.diagram = diagram.split('\n')
        self.students = sorted(students)

    def plants(self, student):
        n = self.students.index(student)

        p = self.diagram[0][n * 2]
        p += self.diagram[0][n * 2 + 1]
        p += self.diagram[1][n * 2]
        p += self.diagram[1][n * 2 + 1]

        return [x for y in p for x in self.plants_list if x[0] == y]

if __name__ == '__main__':
        garden = Garden("VRCGVVRVCGGCCGVRGCVCGCGV\nVRCCCGCRRGVCGCRVVCVGCGCV")
        print garden.plants("Alice")

