class CActor:
    x=0 #postion of the square in x-axis
    y=0 #postion of the square in y-axis
    ht=70 #height of the square
    wd=70 #width of the square
    type=0 # type 0 for normal square - 1 for start and end squares - 2 for walls that stops the search
    row=-1
    column=-1
    BNode_r=-1#the row of the Back Node
    BNode_c = -1#the column of the Back Node

# Importing the library
import pygame
import sys
clock = pygame.time.Clock()
def visited_Node_check(node):
    global visited
    for x in visited:
        if node == x:
            return True
    return False
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

    pygame.display.flip()
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
            if visited_Node_check(current_node)==True:#check if the current_node(poped node) visited or not
                continue#if it in the visited list
            if expand_Node(current_node)==False:
                return True

            visited.append(largeList[current_node.row][current_node.column])#add the current_node(poped node) to the visited list
            largeList[current_node.row][current_node.column].type=3
            drawing_Game()
            clock.tick(2)
        else:return True
def expand_Node(node):
    global fringe
    #push left,Down,Right and Up in the order
    Flag=0#Flag to check if a node is surrounded by a walls
    if(node.column>0):
        if (visited_Node_check(largeList[node.row][node.column - 1]) == False):
            largeList[node.row][node.column - 1].BNode_r=node.row
            largeList[node.row][node.column - 1].BNode_c = node.column
            fringe.append(largeList[node.row][node.column - 1])
            Flag = 1

    if(node.row<7):
        if (visited_Node_check(largeList[node.row+1][node.column]) == False):
            largeList[node.row + 1][node.column].BNode_r=node.row
            largeList[node.row + 1][node.column].BNode_c = node.column
            fringe.append(largeList[node.row+1][node.column])
            Flag = 2
    if(node.column<7):
        if (visited_Node_check(largeList[node.row][node.column + 1]) == False):
            largeList[node.row][node.column + 1].BNode_r=node.row
            largeList[node.row][node.column + 1].BNode_c = node.column
            fringe.append(largeList[node.row][node.column + 1])
            Flag = 3
    if(node.row>0):
        if (visited_Node_check(largeList[node.row-1][node.column]) == False):
            largeList[node.row - 1][node.column].BNode_r=node.row
            largeList[node.row - 1][node.column].BNode_c = node.column
            fringe.append(largeList[node.row-1][node.column])
            Flag = 4
    if(Flag==0 & largeList[node.row][node.column - 1].type==2 & largeList[node.row+1][node.column].type==2 & largeList[node.row][node.column + 1].type==2 & largeList[node.row-1][node.column].type==2):#if the flag is surrounded by a walls it will return false
        return False
    else:return True

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
SCREEN_HEIGHT = 620
SCREEN_WIDTH = 620
# Initializing surface
surface = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT)) # size of the window

# Initialing Color
normal_color = (100, 88, 99)
startAndend_color = (255,0,0)
wall_color=(100,50,0)
visited_node_color=(0, 255, 0)
path_color=(255,215,0)
#custom varibale
ctBreak=0
ctBreak2=0
ctStart=0
level=0
fringe=[]
visited=[]
start_r=-1;
start_c=-1;
end_r=-1;
end_c=-1;
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


                # check if user click the mouse button in the area of the board not outside
                if pygame.mouse.get_pos()[1] < n*70 and pygame.mouse.get_pos()[0] < n*70:
                    ctClicks += 1
                    if ctClicks == 3:
                        if Depth_Serching() == True:
                            break
                    # tring to find the selected square that the user clicked on it and change its type to 1
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



    # Drawing Squares
    drawing_Game()

