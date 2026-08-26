import numpy as np


# -----------------------------
# Functions
# -----------------------------

def calculate_totals(marks):
    return np.sum(marks, axis=1)


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


# -----------------------------
# Get number of students
# -----------------------------

while True:
    try:
        num_students = int(input("Enter number of students: "))

        if num_students > 0:
            break

        print("Enter at least 1 student.")

    except ValueError:
        print("Please enter a valid number.")


# -----------------------------
# Get student names and marks
# -----------------------------

names = []
all_marks = []

for i in range(num_students):

    # Student name
    name = input(f"\nEnter name of student {i + 1}: ")
    names.append(name)

    # Student marks
    student_marks = []

    for j in range(3):

        while True:

            try:
                mark = float(
                    input(f"Enter mark for subject {j + 1}: ")
                )

                if 0 <= mark <= 100:
                    break

                print("Enter a mark between 0 and 100.")

            except ValueError:
                print("Please enter a valid number.")

        student_marks.append(mark)

    all_marks.append(student_marks)


# -----------------------------
# Convert to NumPy array
# -----------------------------

marks = np.array(all_marks)


# -----------------------------
# Analysis
# -----------------------------

totals = calculate_totals(marks)

averages = calculate_averages(marks)

passed, passed_count, failed_count = analyze_pass_fail(averages)

subject_average, subject_highest = analyze_subjects(marks)


# -----------------------------
# Display results
# -----------------------------

print("\n===================================")
print("       STUDENT MARKS ANALYZER")
print("===================================")

print("\nMarks:")
print(marks)


# Student results
print("\n===== STUDENT RESULTS =====")

for i in range(len(names)):

    if passed[i]:
        status = "PASS"
    else:
        status = "FAIL"

    print(
        f"{names[i]} → "
        f"Total: {totals[i]:.0f}, "
        f"Average: {averages[i]:.2f}, "
        f"Status: {status}"
    )


# Pass/Fail summary
print("\n===== PASS / FAIL SUMMARY =====")

print("Passed students:", passed_count)
print("Failed students:", failed_count)


# Subject analysis
print("\n===== SUBJECT ANALYSIS =====")

print("Maths average:", round(subject_average[0], 2))
print("Physics average:", round(subject_average[1], 2))
print("Chemistry average:", round(subject_average[2], 2))

print("\nHighest mark in each subject:")

print("Maths:", subject_highest[0])
print("Physics:", subject_highest[1])
print("Chemistry:", subject_highest[2])


# Overall highest and lowest
print("\n===== OVERALL ANALYSIS =====")

print("Highest mark:", np.max(marks))
print("Lowest mark:", np.min(marks))


# Best student
best_student_index = np.argmax(averages)

print(
    "Best student:",
    names[best_student_index]
)

print(
    "Best average:",
    round(averages[best_student_index], 2)
)
ranking_indices = np.argsort(averages)[::-1]

print("\n===== STUDENT RANKING =====")

for rank, index in enumerate(ranking_indices, start=1):
    print(
        f"{rank}. {names[index]} → "
        f"Average: {averages[index]:.2f}"
    )