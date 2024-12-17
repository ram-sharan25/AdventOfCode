import math

# rows,columns =(102,104)
rows,columns =(7,11)


def get_robots():
    arr = [[[] for _ in range(columns)] for _ in range(rows)]
    print(len(arr),len(arr[0]))
    with open("restroom-input.txt",mode="r") as f:
        for line in f:
            splits = line.strip().split('=')
            position = splits[1].strip('v')
            velocity = splits[2]

            position_split =  position.split(',')
            x_position = int(position_split[0])
            y_position = int(position_split[1])
            velocity_split = velocity.split(',')
            velocity = (int(velocity_split[0]),int(velocity_split[1]))
            # print(x_position,y_position,":",velocity)
            arr[x_position][y_position].append(velocity)
    return arr


def printOriginalRobots(robots):
    for i in range(len(robots[0])):
        for j in range(len(robots[0])):
            if(len(robots[i][j])):
                total_robots = len(robots[i][j])
                print(total_robots,end=" ")
            else:
                print("." ,end=" ")
        print()
def totalCounts (robots):
    total = 0
    for i in range(rows):
        for j in range(columns):
            if(len(robots[i][j])):
                total+= len(robots[i][j])
    return total

def countRobots(robot):
    def countQuadrant(quadrant):
        total = 0
       # print(quadrant)
        for i in range(len(quadrant)):
            for j in range(len(quadrant[i])):
                if(len(quadrant[i][j])):
                    #print("found in:",i,j)
                    total += len(quadrant[i][j])
        return total
    def getQuadrants(robots,x,y):
        quadrants=  [[[] for _ in range(columns//2)] for _ in range(rows//2)]
        i=0;
        for x_val in range(x[0],x[1],1):
            # print(x_val,robots[x_val][y[0]:y[1]])
            quadrants[i] = robots[x_val][y[0]:y[1]]
            i+=1
        #print(x,y,len(quadrants),len(quadrants[0]),quadrants)
        return quadrants
    mid_x = math.floor(rows/2)
    mid_y = math.floor(columns/2)
    one_one = countQuadrant(getQuadrants(robot,(0,mid_x),(0,mid_y)))
    one_two = countQuadrant(getQuadrants(robot,(0,mid_x),(mid_y+1,columns)))
    one_three = countQuadrant(getQuadrants(robot,(mid_x+1,rows),(0,mid_y)))
    one_four = countQuadrant(getQuadrants(robot,(mid_x+1,rows),(mid_y+1,columns)))
    # print(one_two)
    print(one_one,one_two,one_three,one_four)
    print(one_one+one_two+one_three+one_four)
    print(one_one*one_two*one_three*one_four)




def printRobots(robots):
    for i in range(rows):
        for j in range(columns):
            if(i==math.floor(rows/2) or j==math.floor(columns/2)):
                print(" ",end=" ")
            else:
                if(len(robots[i][j])):
                    total_robots = len(robots[i][j])
                    print(total_robots,end=" ")
                else:
                    print("." ,end=" ")
        print()

def move_Robots(robot):
    new_robot = [[[] for _ in range(columns)] for _ in range(rows)]
    for i in range(len(robot)):
        for j in range(len(robot[i])):
            if(len(robot[i][j])):
               for k in range(len(robot[i][j])):
                   new_position_y = (j + robot[i][j][k][0])%(columns)
                   new_position_x = (i + robot[i][j][k][1])%(rows)
                   print("from: ",i,j," with: ",robot[i][j][k][0],robot[i][j][k][1]," to: ",new_position_x,new_position_y)
                   new_robot[new_position_x][new_position_y].append(robot[i][j][k])

    return new_robot




robot = [[[] for _ in range(columns)] for _ in range(rows)]

robot_positions = [
    (2, 4, (2, -3)),
    (4, 9, (-1, -3)),
    # (10, 3, (-1, 2)),
    # (2, 0, (2, -1)),
    # (0, 0, (1, 3)),
    # (3, 0, (-2, -2)),
    # (7, 6, (-1, -3)),
    # (3, 0, (-1, -2)),
    # (9, 3, (2, 3)),
    # (7, 3, (-1, 2)),
    # (2, 4, (2, -3)),
    # (9, 5, (-3, -3))
]


for x, y, velocity in robot_positions:
    # Adjust for grid size if needed
    adjusted_x = x
    adjusted_y = y
    robot[adjusted_x][adjusted_y].append(velocity)
print(robot)
printOriginalRobots(robot)
print(totalCounts(robot))
print()
robot = move_Robots(robot)
# for i in range(100):
#     robot = move_Robots(robot)
printOriginalRobots(robot)
print()
printRobots(robot)
print()
countRobots(robot)




# all_robots = get_robots()
# printOriginalRobots(all_robots)
# print(totalCounts(all_robots))

# print()
# for i in range(101):
#     print(i)
#     all_robots  = move_Robots(all_robots)

# printRobots(all_robots)
# countRobots(all_robots)
