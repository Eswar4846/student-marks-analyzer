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