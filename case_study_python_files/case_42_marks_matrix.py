"""Case 42: Student marks matrix analysis."""

STUDENTS = ["Asha", "Bala", "Charan"]
SUBJECTS = ["Python", "Maths", "English"]
MARKS = [
    [82, 74, 91],
    [68, 88, 79],
    [95, 93, 89],
]
LOW_AVERAGE_LIMIT = 60.0


def analyze_marks(students, subjects, marks, low_average_limit):
    if len(students) != len(marks) or len(marks) == 0:
        raise ValueError("Each student must have one marks row.")
    for row in marks:
        if len(row) != len(subjects):
            raise ValueError("Each marks row must contain one mark per subject.")
        for mark in row:
            if mark < 0 or mark > 100:
                raise ValueError("Marks must be between 0 and 100.")

    print("STUDENT MARKS MATRIX ANALYSIS")
    totals = []
    for index, student in enumerate(students):
        total = sum(marks[index])
        average = total / len(subjects)
        totals.append(total)
        print(f"{student}: total={total}, average={average:.2f}")

    subject_averages = []
    for column in range(len(subjects)):
        total = 0
        for row in range(len(marks)):
            total += marks[row][column]
        average = total / len(marks)
        subject_averages.append(average)
        status = "LOW" if average < low_average_limit else "OK"
        print(f"{subjects[column]} average={average:.2f} ({status})")

    top_index = totals.index(max(totals))
    print(f"Top performer: {students[top_index]} ({totals[top_index]} marks)")
    return totals, subject_averages, students[top_index]


if __name__ == "__main__":
    analyze_marks(STUDENTS, SUBJECTS, MARKS, LOW_AVERAGE_LIMIT)
