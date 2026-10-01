from classes import PatientExam

def main():
    patient_exams = []

    with open('patient_data.csv', 'r') as file:
        first_row = True

        for row in file:
            if first_row:
                first_row = False
            else:
                data = row.strip().split(',')

                exam_id = int(data[0])
                date = data[1]
                name = data[2].strip()
                weight = int(data[3])
                height = float(data[4])

                patient = PatientExam(exam_id, date, name, weight, height)
                patient_exams.append(patient)

    total_BMI = 0

    for patient in patient_exams:
        total_BMI += patient.get_BMI()

    average_BMI = total_BMI / len(patient_exams)
    print(f'Average BMI: {average_BMI:.2f}')

    month_counts = [0] * 12

    for patient in patient_exams:
        month = patient.get_exam_month()
        month_counts[month - 1] += 1

    busiest_month = 1

    for i in range(len(month_counts)):
        if month_counts[i] > month_counts[busiest_month - 1]:
            busiest_month = i + 1

    print(f'Busiest month: {busiest_month}')


main()
# your code here