class CActor:
    x=0 #postion of the square in x-axis
    y=0 #postion of the square in y-axis
    ht=70 #height of the square
    wd=70 #width of the square
    type=0 # type 0 for normal square - 1 for start and end squares - 2 for walls that stops the search
    row=-1
    column=-1
    level = -1  # node level
    BNode_r=-1#the row of the Back Node
    BNode_c = -1#the column of the Back Node

# Importing the library
import pygame
import sys
clock = pygame.time.Clock()

def drawing_Game():
    # Drawing Squares
    for x in largeList:
        for i in range(n):
            if x[i].type == 0:
                pygame.draw.rect(surface, normal_color, pygame.Rect(x[i].x, x[i].y, x[i].wd - 2, x[i].ht - 2))
            elif x[i].type == 1:
                pygame.draw.rect(surface, startAndend_color, pygame.Rect(x[i].x, x[i].y, x[i].wd - 2, x[i].ht - 2))
            elif x[i].type == 2:
                pygame.draw.rect(surface, wall_color, pygame.Rect(x[i].x, x[i].y, x[i].wd - 2, x[i].ht - 2))
            elif x[i].type == 3:
                pygame.draw.rect(surface, visited_node_color, pygame.Rect(x[i].x, x[i].y, x[i].wd - 2, x[i].ht - 2))
            else: pygame.draw.rect(surface, path_color, pygame.Rect(x[i].x, x[i].y, x[i].wd - 2, x[i].ht - 2))
    for x in range(len(Search_Techniques)):
        pygame.draw.rect(surface, white_color, pygame.Rect(600, 100 * (x + 1), 150, 50))
        text = font.render(Search_Techniques[x], True, black_color)
        textRect = text.get_rect()
        if (x == 0):
            textRect.x = 640
        if x == 1:
            textRect.x = 630
        if x == 2:
            textRect.x = 610
        textRect.y = (100 * (x + 1)) + 10
        surface.blit(text, textRect)

    pygame.display.flip()
    ##########################################################################################:::BFS


def visited_Node_check_BFS(node):
    global visited

    for x in visited:
        if node == x:
            print(node.row, ",", node.column, " it is visited or it is wall")

            return True
    return False

def BFS():
    global fringe
    while True:
        current_node = fringe.pop(0)
        print(current_node.row, ",", current_node.column)
        if (current_node == largeList[end_r][end_c]):
            print("Last")
            print(current_node.row, ",", current_node.column)
            print("lenth of visited is ", len(visited))
            print("found goal")
            return True
            break
        if visited_Node_check_BFS(current_node) == True:
            continue
        expand_Node_BFS(current_node)
        visited.append(largeList[current_node.row][current_node.column])
        largeList[current_node.row][current_node.column].type = 3
        drawing_Game()
        clock.tick(1)

# it works clockwise
def expand_Node_BFS(node):
    global fringe

    # check left
    if (node.row > 0):
        if (visited_Node_check_BFS(largeList[node.row - 1][node.column]) == False):
            fringe.append(largeList[node.row - 1][node.column])

    # check down
    if (node.column < n - 1):
        if (visited_Node_check_BFS(largeList[node.row][node.column + 1]) == False):
            fringe.append(largeList[node.row][node.column + 1])

    # check right
    if (node.row < n - 1):
        if (visited_Node_check_BFS(largeList[node.row + 1][node.column]) == False):
            fringe.append(largeList[node.row + 1][node.column])

    # check up
    if (node.column > 0):
        if (visited_Node_check_BFS(largeList[node.row][node.column - 1]) == False):
            fringe.append(largeList[node.row][node.column - 1])

    ##################################################################################::::Iterative

def expand_Node_iterative(node):
    global fringe
    # LIFO = last in first out
    # add left
    if node.column - 1 >= 0:
        print("L")
        print(largeList[node.row][node.column - 1].row)
        print(largeList[node.row][node.column - 1].column)
        largeList[node.row][node.column - 1].level = node.level + 1
        fringe.insert(0, largeList[node.row][node.column - 1])
    # add down
    if node.row + 1 < n:
        print("d")
        print(largeList[node.row + 1][node.column].row)
        print(largeList[node.row + 1][node.column].column)
        largeList[node.row + 1][node.column].level = node.level + 1
        print(f"level node {largeList[node.row + 1][node.column].level}")
        fringe.insert(0, largeList[node.row + 1][node.column])
    # add right
    if node.column + 1 < n:
        print("r")
        print(largeList[node.row][node.column + 1].row)
        print(largeList[node.row][node.column + 1].column)
        largeList[node.row][node.column + 1].level = node.level + 1
        fringe.insert(0, largeList[node.row][node.column + 1])
    # add up
    if node.row - 1 >= 0:
        print("up")

        print(largeList[node.row - 1][node.column].row)
        print(largeList[node.row - 1][node.column].column)
        largeList[node.row - 1][node.column].level = node.level + 1
        fringe.insert(0, largeList[node.row - 1][node.column])

def visited_Node_check_iterative(node):
    global visited
    for x in visited:  # loop to check if the node that received from fringe check is visited before
        if node == x:
            return True

    node.type = 3  # make the node color green which means it is visited

    visited.append(node)  # add node to visited list

    drawing_Game()
    clock.tick(1)
    return False

def fringe_Check_iterative():
    global fringe, ctBreak
    print(f"len1 {len(fringe)}")
    mylist = fringe.copy()  # make a copy from fringe list to let me delete any node without any problems in index and looping in mylist

    for x in mylist:
        print(f"check lev {x.level} and curr lev {level}")

        if visited_Node_check_iterative(x) == False:  # call function to check the node if it is not visited

            if x == largeList[end_r][end_c]:  # if node equal to goal postion return true
                print("found it")
                return True
            else:  # if node not equal the goal
                if x.level < level:  # if node level less than the searching level
                    expand_Node_iterative(x)  # call function to expand node
                    print("3alih eldor")
                    print(x.row)
                    print(x.column)
                    fringe.remove(x)  # delete node after expanded it
                    return "again"
                else:  # if node level not less than the searching level delete the node
                    print("poped2")
                    visited_Node_check_iterative(x)
                    fringe.remove(x)
        else:  # call function to check the node if it is not visited so if it visited delete it from fringe
            print("poped visited (already)")
            fringe.remove(x)

    print(f"len2 {len(fringe)}")

    if len(fringe) == 0:  # it maens all fringe node visited or not less than the level of searching so all of them deleted and the lenght equal zero
        ctBreak += 1
        print("break1")
        return False
def searching_iterative():
    global fringe, level, visited
    # loop for checking fringe until find the goal
    while True:
        print(f"fringe of level{level} and visited count {len(visited)}######")
        for x in fringe:
            print(x.row)
            print(x.column)

        print("fringe ######")

        fringeValue = fringe_Check_iterative()  # varibale to get the return from function fringe_check
        if fringeValue == True:  # if the var equal true that mean it reached the goal and should stop searching
            break
        elif fringeValue == False:  # if the var equal false it means it will increase the level of searching to try reach the goal
            level += 1

            for x in largeList:  # loop over the 2d array to return all colors to its original color and not visited color
                for c in range(n):
                    if x[c].type == 3:
                        x[c].type = 0

            fringe = []  # clear the fringe because it will start a new level of search and wants to start from the start point
            fringe.append(largeList[start_r][
                              start_c])  # adding the start point that the user selected to be the first node we search from
            visited = []  # clear the visited list because it will start a new level of search and wants to start from the start point
            visited = tempVisited.copy()  # visited list takes copy from temp list that always has the walls the user entered and it may be empty if the user did not select any walls
            print(f"level {level} ####")
            largeList[start_r][start_c].level = 0  # return the start point to level 0 as it should always be
            largeList[start_r][start_c].type = 1  # return the start point color to red


        else:  # it means the fringe have nodes that wants to be checked

            print("again")

        drawing_Game()
        clock.tick(1)

######################################################################################::::Depth

def Depth_Serching():
    global fringe
    while True:
        if len(fringe)!=0:
            current_node=fringe.pop()#pop the last pushed node and save it in current_node
            print(current_node.row, ",", current_node.column)
            if(current_node==largeList[end_r][end_c]):#check if the current_node(poped node)is the end or not
                print("Last")
                print(current_node.row, ",", current_node.column)
                print("len",len(visited))
                print("found it")
                while True:
                    largeList[current_node.BNode_r][current_node.BNode_c].type=4 #chagne the color of the path

                    current_node=largeList[current_node.BNode_r][current_node.BNode_c]
                    if(current_node==largeList[start_r][start_c]):
                        print("opaa")
                        break
                return True
                break
            if visited_Node_check_Depth(current_node)==True:#check if the current_node(poped node) visited or not
                continue#if it in the visited list
            if expand_Node_Depth(current_node)==False:
                return True

            visited.append(largeList[current_node.row][current_node.column])#add the current_node(poped node) to the visited list
            largeList[current_node.row][current_node.column].type=3
            drawing_Game()
            clock.tick(2)
        else:return True

def visited_Node_check_Depth(node):
    global visited
    for x in visited:
        if node == x:
            return True
    return False
def expand_Node_Depth(node):
    global fringe
    #push left,Down,Right and Up in the order
    Flag=0#Flag to check if a node is surrounded by a walls
    if(node.column>0):
        if (visited_Node_check_Depth(largeList[node.row][node.column - 1]) == False):
            largeList[node.row][node.column - 1].BNode_r=node.row
            largeList[node.row][node.column - 1].BNode_c = node.column
            fringe.append(largeList[node.row][node.column - 1])
            Flag = 1

    if(node.row<7):
        if (visited_Node_check_Depth(largeList[node.row + 1][node.column]) == False):
            largeList[node.row + 1][node.column].BNode_r=node.row
            largeList[node.row + 1][node.column].BNode_c = node.column
            fringe.append(largeList[node.row+1][node.column])
            Flag = 2
    if(node.column<7):
        if (visited_Node_check_Depth(largeList[node.row][node.column + 1]) == False):
            largeList[node.row][node.column + 1].BNode_r=node.row
            largeList[node.row][node.column + 1].BNode_c = node.column
            fringe.append(largeList[node.row][node.column + 1])
            Flag = 3
    if(node.row>0):
        if (visited_Node_check_Depth(largeList[node.row - 1][node.column]) == False):
            largeList[node.row - 1][node.column].BNode_r=node.row
            largeList[node.row - 1][node.column].BNode_c = node.column
            fringe.append(largeList[node.row-1][node.column])
            Flag = 4
    if(Flag==0 & largeList[node.row][node.column - 1].type==2 & largeList[node.row+1][node.column].type==2 & largeList[node.row][node.column + 1].type==2 & largeList[node.row-1][node.column].type==2):#if the flag is surrounded by a walls it will return false
        return False
    else:return True

######################################################################



n=8
thisList=[]
largeList=[]
# creating the 2D List of objects from type CActor
for r in range(n):
    for c in range(n):
        act = CActor()

        act.x= act.x + ( c * act.wd)
        act.y= act.y + ( r * act.ht)
        act.row = r
        act.column = c

        thisList.append(act)


    largeList.append(thisList)
    thisList = []

# Initializing Pygame
pygame.init()
SCREEN_HEIGHT = 570
SCREEN_WIDTH = 800
# Initializing surface
surface = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT)) # size of the window

# Initialing Color
normal_color = (100, 88, 99)
startAndend_color = (255,0,0)
wall_color=(100,50,0)
visited_node_color=(0, 255, 0)
path_color=(0,255,0)
black_color=(0,0,0)
white_color=(250,250,250)
#custom varibale
font = pygame.font.Font('freesansbold.ttf', 32)
ctBreak=0
ctBreak2=0
ctStart=0
level=0
fringe=[]
visited=[]
tempVisited=[]
Search_Techniques=["BFS","Depth","iterative"]
start_r=-1;
start_c=-1;
end_r=-1;
end_c=-1;
start_flag=0
ctClicks=0
# infinite loop to display the game
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        # check if user click the mouse button and we use it to know the Start and End of search
        if event.type == pygame.MOUSEBUTTONDOWN:
            # the user have only two clicks one for Start and the second one for End
                if ctClicks >= 2 and pygame.mouse.get_pos()[0] <= 750 and pygame.mouse.get_pos()[0] >= 600 and \
                        pygame.mouse.get_pos()[1] >= 100 and pygame.mouse.get_pos()[1] <= 150 and start_flag==0:
                    start_flag=1
                    if BFS()==True:
                        break
                if ctClicks >= 2 and pygame.mouse.get_pos()[0] <= 750 and pygame.mouse.get_pos()[0] >= 600 and \
                        pygame.mouse.get_pos()[1] >= 300 and pygame.mouse.get_pos()[1] <= 350 and start_flag==0:
                        start_flag = 1
                        searching_iterative()

                if ctClicks >= 2 and pygame.mouse.get_pos()[0] <= 750 and pygame.mouse.get_pos()[0] >= 600 and \
                        pygame.mouse.get_pos()[1] >= 200 and pygame.mouse.get_pos()[1] <= 250 and start_flag==0:
                    start_flag = 1
                    if Depth_Serching() == True:
                        break
                # check if user click the mouse button in the area of the board not outside
                if pygame.mouse.get_pos()[1] < n*70 and pygame.mouse.get_pos()[0] < n*70:
                    ctClicks += 1

                    # tring to find the selected square that the user clicked on it and change its type to 1
                    if ctClicks<=2:
                        for r in range(len(largeList)):
                            for c in range(n):
                                if pygame.mouse.get_pos()[0] > largeList[r][c].x and pygame.mouse.get_pos()[0] < \
                                        largeList[r][c].x + largeList[r][c].wd and pygame.mouse.get_pos()[1] > largeList[r][
                                    c].y and pygame.mouse.get_pos()[1] < largeList[r][c].y + largeList[r][c].ht:
                                    largeList[r][c].type = 1
                                    if ctClicks == 1:
                                        start_r = r
                                        start_c = c
                                        fringe.append(largeList[r][c])
                                    if ctClicks == 2:
                                        if largeList[r][c]!=largeList[start_r][start_c]:
                                            end_r = r
                                            end_c = c
                                        else:ctClicks-=1

        # check if user click any button and we use it to put walls
        if event.type == pygame.KEYDOWN:
            # check if user click the mouse button in the area of the board not outside
            if pygame.mouse.get_pos()[1] < n * 70 and pygame.mouse.get_pos()[0] < n * 70:
                    # tring to find the selected square that the user clicked on it and change its type to 1
                    for r in range(len(largeList)):
                        for c in range(n):
                            if pygame.mouse.get_pos()[0] > largeList[r][c].x and pygame.mouse.get_pos()[0] < \
                                    largeList[r][c].x + largeList[r][c].wd and pygame.mouse.get_pos()[1] > largeList[r][
                                c].y and pygame.mouse.get_pos()[1] < largeList[r][c].y + largeList[r][c].ht:
                                largeList[r][c].type = 2
                                visited.append(largeList[r][c])
                    tempVisited = visited.copy()

    # Drawing Squares
    drawing_Game()

