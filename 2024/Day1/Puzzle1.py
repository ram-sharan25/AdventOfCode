first = []
second = []

def get_count(arr,target):
    count = 0
    for i in arr:
        if(i==target):
            count+=1
    return count


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
total_difference = 0
for idx,x in enumerate(sorted_first):
    y  = sorted_second[idx]
    diff = abs(x - y)
    # print(diff,x,y)
    total_difference += diff

total_similarity = 0
for idx,x  in enumerate(sorted_first):
    count = get_count(sorted_second,x);
    similarity = x * count
    total_similarity += similarity

# only unique elements from list a
# but it is not necessary here
# seen = set()
# unique_first = [val for val in sorted_first if val not in seen and (seen.add(val)) or True]

print(total_similarity)

print(total_difference)
