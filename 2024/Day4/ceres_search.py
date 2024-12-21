# letters = [["MMMSXXMASM"],
#            ["MSAMXMSMSA"],
#            ["AMXSXMAAMM"],
#            ["MSAMASMSMX"],
#            ["XMASAMXAMM"],
#            ["XXAMMXXAMA"],
#            ["SMSMSASXSS"],
#            ["SAXAMASAAA"],
#            ["MAMMMXMMMM"],
#            ["MXMXAXMASX"]]



def get_all_expressions():
    letters = []
    with open('input.txt','r') as f:
        for line in f :
            letters.append([line.strip()])

    return letters

letters = get_all_expressions()

def letter(i,j):
    if(i>len(letters)-1 or i<0):
        return
    if(j>len(letters[i][0])-1 or j<0):
        return
    val = letters[i][0][j]
    return val

def check_forward_letters(i,j):
    direction = []
    position = []

    def  push_dir(val,i,j):
        direction.append(val)
        position.append([i,j])

    if(letter(i,j)=="X" and letter(i,j+1)=="M" and letter(i,j+2)=="A" and letter(i,j+3)=="S"):
        push_dir('r',i,j)
    if(letter(i,j)=="X" and letter(i,j-1)=="M" and letter(i,j-2)=="A" and letter(i,j-3)=="S"):
        push_dir('l',i,j)
    if(letter(i,j)=="X" and letter(i+1,j)=="M" and letter(i+2,j)=="A" and letter(i+3,j)=="S"):
        push_dir('d',i,j)
    if(letter(i,j)=="X" and letter(i-1,j)=="M" and letter(i-2,j)=="A" and letter(i-3,j)=="S"):
        push_dir('d',i,j)
    if(letter(i,j)=="X" and letter(i-1,j-1)=="M" and letter(i-2,j-2)=="A" and letter(i-3,j-3)=="S"):
        push_dir('l u',i,j)
    if(letter(i,j)=="X" and letter(i-1,j+1)=="M" and letter(i-2,j+2)=="A" and letter(i-3,j+3)=="S"):
        push_dir('l d',i,j)
    if(letter(i,j)=="X" and letter(i+1,j-1)=="M" and letter(i+2,j-2)=="A" and letter(i+3,j-3)=="S"):
        push_dir('r u',i,j)
    if(letter(i,j)=="X" and letter(i+1,j+1)=="M" and letter(i+2,j+2)=="A" and letter(i+3,j+3)=="S"):
        push_dir('r d',i,j)
    return direction,position

def check_forward_slash(i,j):
    if((letter(i-1,j-1)=="S") and (letter(i,j)=="A") and (letter(i+1,j+1)=="M")):
        return True
    if((letter(i-1,j-1)=="M") and (letter(i,j)=="A") and (letter(i+1,j+1)=="S")):
        return True
    return False

def check_backward_slash(i,j):
    if((letter(i-1,j+1)=="S") and (letter(i,j)=="A") and (letter(i+1,j-1)=="M")):
        return True
    if((letter(i-1,j+1)=="M") and (letter(i,j)=="A") and (letter(i+1,j-1)=="S")):
        return True
    return False




def check_X(i,j):
    position = []
    def  push_dir(i,j):
        position.append([i,j])
    if(check_forward_slash(i,j) and check_backward_slash(i,j) ):
        push_dir(i,j)

    return position,


def run_part_one():
    total = 0
    for i in range(len(letters)):
        for j in range(len(letters[i][0])):
            direction,position = check_forward_letters(i,j)
            if(len(direction)):
                total+=len(direction)
    print(total)

def run_part_two():
     total = 0
     for i in range(len(letters)):
        for j in range(len(letters[i][0])):
            position = check_X(i,j)
            if(len(position) and position[0]):
                print(position)
                total+=len(position)
     print(total)
run_part_two()
