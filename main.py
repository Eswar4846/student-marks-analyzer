import numpy as np

marks=np.array([
    [85,20,40],
    [78,67,63],
    [45,33,18],
    [54,78,91],
    [78,81,79]
])

print("Marks:")
print(marks)

print("\nAverage marks:")
print(np.mean(marks))

print("\nHighest marks:")
print(np.max(marks))

print("\nLowest marks:")
print(np.min(marks))

totals=np.sum(marks,axis=1)
averages=np.mean(marks,axis=1)
subject_averages=np.mean(marks,axis=0)
highest_subject=np.max(marks,axis=0)
print(marks.ndim)
print(marks.shape)
print(marks.size)
print(marks.dtype)
print(marks[0])
print(marks[0,1])
print(marks[0][1])
print(marks[:,0])
print(marks[0:3])
print(marks[:,0:2])
highest=np.max(marks)
print(highest)
lowest=np.min(marks)
print(lowest)

student_average=np.mean(marks,axis=1)
print(student_average)

passed=student_average>=50
print(passed)

passed_students = student_average[student_average >= 50]
print(passed_students)

best_student_index = np.argmax(student_average)
print(best_student_index)
def calculate_totals(marks):
    return np.sum(marks, axis=1)
totals = calculate_totals(marks)
def calculate_averages(marks):
    return np.mean(marks, axis=1)
def analyze_pass_fail(averages):
    passed = averages >= 50
    passed_count = np.sum(passed)
    failed_count = np.sum(averages < 50)

    return passed, passed_count, failed_count
def analyze_subjects(marks):
    subject_average = np.mean(marks, axis=0)
    subject_highest = np.max(marks, axis=0)

    return subject_average, subject_highest

totals = calculate_totals(marks)

averages = calculate_averages(marks)

passed, passed_count, failed_count = analyze_pass_fail(averages)

subject_average, subject_highest = analyze_subjects(marks)


print("===== STUDENT MARKS ANALYZER =====")

print("\nStudent totals:")
print(totals)

print("\nStudent averages:")
print(averages)

print("\nPass/Fail:")
print(passed)

print("\nPassed students:", passed_count)
print("Failed students:", failed_count)

print("\nSubject averages:")
print(subject_average)

print("\nHighest mark in each subject:")
print(subject_highest)

num_students = int(input("Enter number of students: "))
all_marks = []
for i in range(num_students):
    print(f"\nStudent {i + 1}")

    student_marks = []

    for j in range(3):
        mark = float(input(f"Enter mark for subject {j + 1}: "))
        student_marks.append(mark)
    all_marks.append(student_marks)
marks=np.array(all_marks)

totals = calculate_totals(marks)

averages = calculate_averages(marks)

passed, passed_count, failed_count = analyze_pass_fail(averages)

subject_average, subject_highest = analyze_subjects(marks)


# Output
print("\n===== STUDENT MARKS ANALYZER =====")

print("\nMarks:")
print(marks)

print("\nStudent totals:")
print(totals)

print("\nStudent averages:")
print(averages)

print("\nPass/Fail:")
print(passed)

print("\nPassed students:", passed_count)
print("Failed students:", failed_count)

print("\nSubject averages:")
print(subject_average)

print("\nHighest mark in each subject:")
print(subject_highest)