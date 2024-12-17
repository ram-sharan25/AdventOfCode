# reports = [[7, 6 ,4 ,2, 1],
#            [1, 2 ,7, 8, 9],
#            [9, 7, 6, 2, 1],
#            [1 ,3, 2, 4, 5],
#            [8 ,6 ,4, 4, 1],
#            [1 ,3 ,6 ,7, 9]]
# print(reports)
reports = []

with open('Red_Nosed_input.txt','r') as file:
    for line in file.readlines():
        line_split = line.strip().split(" ")
        report = [int(val) for val in line_split ]
        reports.append(report)

# print(reports)
def is_safe(report):
    val = []
    increasing = report[1]>report[0] or False
    for idx in range(len(report)-1):
        diff = (report[idx+1]-report[idx])
        if ((((diff>0) and (diff <=3)) and increasing )or((diff<0 and diff>=(-3)) and not(increasing))):
            val.append(True)
        else: val.append(False)
    false_count = sum(not x for x in val)
    # false_count = val.count(False)
    print(false_count)
    if (false_count<2): return True
    else: return False

total_safe = 0
for report in reports:
    total_safe+=is_safe(report)
print(total_safe)
