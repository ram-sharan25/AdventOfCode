import re


def get_all_expressions():
    all = []
    with open('input.txt','r') as f:
        for line in f :
            val     = re.findall(r"mul\(\d+,\d+\)", line)
            numbers = [[int(re.findall(r"\d+",x1)[0]) for x1 in x.split(',')] for x in val ]
            all.append(numbers)
    return all


def get_all_expressions_with_do_dont():
    all = []
    with open('input.txt','r') as f:
        for line in f :
            val     = re.findall(r"(mul\(\d+,\d+\)|don't\(\)|do\(\))", line)
            all.append(val)
    return all

def part_one():
    arr   = get_all_expressions()
    total = 0
    for nums in arr:
        for num in nums:
            total+= num[0]*num[1]
    print("Part one: ",total)

def part_two():
    all = get_all_expressions_with_do_dont()
    total=0
    mul = True
    for collection in all:
        for  val in collection:
            if(val=="don't()"):
                mul = False
            elif(val=="do()"):
                mul = True
            elif mul:
                numbers = re.findall(r'\d{1,3}', val)
                total+= int(numbers[0])*int(numbers[1])
    print("Part two: ",total)
part_one()
part_two()
