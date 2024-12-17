first = []
second = []

def sort_list(val):
    for i in range(0,len(val)):
        min = i
        for j in range(i,len(val)):
            if(val[min]>=val[j]):
               min = j
        temp = val[i]
        val[i]= val[min]
        val[min] = temp
    return val

with open('Puzzle_1_input.txt','r') as file:
    for line in file.readlines():
        line_split = line.strip().split(" ")
        first.append(int(line_split[0]))
        second.append(int(line_split[3]))

sorted_first = sort_list(first)
sorted_second = sort_list(second)
# print(second)
total = 0
for idx,x in enumerate(sorted_first):
    y  = sorted_second[idx]
    diff = abs(x - y)
    # print(diff,x,y)
    total += diff


print(total)
