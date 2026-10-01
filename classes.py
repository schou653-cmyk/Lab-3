
class PatientExam:

    def __init__(self, exam_id, date, name, weight, height):
        self.exam_id = exam_id
        self.date = date
        self.name = name
        self.weight = weight
        self.height = height

    def get_BMI(self):
        return self.weight / (self.height ** 2)

    def get_exam_month(self):
        date_parts = self.date.split('/')
        return int(date_parts[0])
    # your code here