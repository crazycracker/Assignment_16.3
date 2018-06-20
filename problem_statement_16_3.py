import math

# there are 100 students
# 80 failed in 0 subjects
# 10 failed in 1 subject
# 7  failed in 2 subjects
# 3  failed in 3 subjects

# count of students according to number of subjects they failed
li = [80, 10, 7, 3]

# total number of students
n = 100

for x in range(4):
    print("probability of student failing in %d subjects is %.2f. " % (x, li[x]/n))
