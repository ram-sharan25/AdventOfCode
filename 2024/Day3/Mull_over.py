import re


def get_all_expressions():
    all = []
    with open('input.txt','r') as f:
        for line in f :
            val     = re.findall(r"mul\(\d+,\d+\)", line)
            numbers = [[int(re.findall(r"\d+",x1)[0]) for x1 in x.split(',')] for x in val ]
            all.append(numbers)
    return all


arr   = get_all_expressions()
total = 0
for nums in arr:
    print()
    for num in nums:
       print(num)
       total+= num[0]*num[1]


print(total)
