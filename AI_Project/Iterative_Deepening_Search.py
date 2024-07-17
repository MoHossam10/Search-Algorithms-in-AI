class CActor:
    x=0 #postion of the square in x-axis
    y=0 #postion of the square in y-axis
    ht=70 #height of the square
    wd=70 #width of the square
    type=0 # type 0 for normal square - 1 for start and end squares - 2 for walls that stops the search
    row=-1 #node row postion
    column=-1 #node coloum postion
    level=-1 # node level

def drawing_Game():
    # Drawing Squares
    for x in largeList:
        for i in range(n):
            if x[i].type == 0:
                pygame.draw.rect(surface, normal_color, pygame.Rect(x[i].x, x[i].y, x[i].wd-2, x[i].ht-2))
            elif x[i].type == 1:
                pygame.draw.rect(surface, startAndend_color, pygame.Rect(x[i].x, x[i].y, x[i].wd - 2, x[i].ht - 2))
            elif x[i].type == 2:
                pygame.draw.rect(surface, wall_color, pygame.Rect(x[i].x, x[i].y, x[i].wd - 2, x[i].ht - 2))
            else:
                pygame.draw.rect(surface, visited_node_color, pygame.Rect(x[i].x, x[i].y, x[i].wd - 2, x[i].ht - 2))


    pygame.display.flip()

def expand_Node(node):
    global fringe
    #LIFO = last in first out
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
    #add up
    if node.row -1 >= 0 :
        print("up")

        print(largeList[node.row-1][node.column].row)
        print(largeList[node.row - 1][node.column].column)
        largeList[node.row - 1][node.column].level= node.level + 1
        fringe.insert(0, largeList[node.row-1][node.column])




def visited_Node_check(node):
    global visited
    for x in visited: # loop to check if the node that received from fringe check is visited before
        if node == x:
            return True


    node.type = 3 # make the node color green which means it is visited

    visited.append(node) # add node to visited list

    drawing_Game()
    clock.tick(1)
    return False

def fringe_Check():
    global fringe,ctBreak
    print(f"len1 {len(fringe)}")
    mylist=fringe.copy() # make a copy from fringe list to let me delete any node without any problems in index and looping in mylist

    for x in mylist:
        print(f"check lev {x.level} and curr lev {level}")

        if visited_Node_check(x) == False: # call function to check the node if it is not visited

            if x == largeList[end_r][end_c]: # if node equal to goal postion return true
                print("found it")
                return True
            else:# if node not equal the goal
                if x.level < level:  # if node level less than the searching level
                    expand_Node(x) # call function to expand node
                    print("3alih eldor")
                    print(x.row)
                    print(x.column)
                    fringe.remove(x) # delete node after expanded it
                    return "again"
                else:  # if node level not less than the searching level delete the node
                    print("poped2")
                    visited_Node_check(x)
                    fringe.remove(x)
        else: # call function to check the node if it is not visited so if it visited delete it from fringe
            print("poped visited (already)")
            fringe.remove(x)


    print(f"len2 {len(fringe)}")


    if len(fringe) == 0: # it maens all fringe node visited or not less than the level of searching so all of them deleted and the lenght equal zero
        ctBreak +=1
        print("break1")
        return False



def searching_iterative():
    global fringe,level, visited
    # loop for checking fringe until find the goal
    while True:
        print(f"fringe of level{level} and visited count {len(visited)}######")
        for x in fringe:

            print(x.row)
            print(x.column)

        print("fringe ######")

        fringeValue=fringe_Check() #varibale to get the return from function fringe_check
        if fringeValue == True : # if the var equal true that mean it reached the goal and should stop searching
            break
        elif fringeValue == False: # if the var equal false it means it will increase the level of searching to try reach the goal
            level+=1

            for x in largeList: # loop over the 2d array to return all colors to its original color and not visited color
                for c in range(n):
                    if x[c].type==3:
                        x[c].type=0

            fringe=[] #clear the fringe because it will start a new level of search and wants to start from the start point
            fringe.append(largeList[start_r][start_c]) # adding the start point that the user selected to be the first node we search from
            visited=[] # clear the visited list because it will start a new level of search and wants to start from the start point
            visited=tempVisited.copy() # visited list takes copy from temp list that always has the walls the user entered and it may be empty if the user did not select any walls
            print(f"level {level} ####")
            largeList[start_r][start_c].level=0 # return the start point to level 0 as it should always be
            largeList[start_r][start_c].type=1 # return the start point color to red


        else: #it means the fringe have nodes that wants to be checked

            print("again")

        drawing_Game()
        clock.tick(1)

# Importing the library
import pygame
import sys
# init timer
clock = pygame.time.Clock()
n=8
thisList=[]
largeList=[]
# creating the 2D List of objects from type CActor
for r in range(n):
    for c in range(n):
        act = CActor()

        act.x= act.x + ( c * act.wd)
        act.y= act.y + ( r * act.ht)
        act.row=r
        act.column=c


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
#custom varibale
tempVisited=[]
ctBreak=0
ctStart=0
level=0
fringe=[]
visited=[]
start_r=-1
start_c=-1
end_r=-1
end_c=-1
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
            if ctClicks <2:
                ctClicks+=1
                # check if user click the mouse button in the area of the board not outside
                if pygame.mouse.get_pos()[1] < n*70 and pygame.mouse.get_pos()[0] < n*70:
                    # tring to find the selected square that the user clicked on it and change its type to 1
                    for r in range(len(largeList)):
                        for c in range(n):
                            if pygame.mouse.get_pos()[0] > largeList[r][c].x and pygame.mouse.get_pos()[0] < largeList[r][c].x +largeList[r][c].wd and pygame.mouse.get_pos()[1] >largeList[r][c].y and pygame.mouse.get_pos()[1] <largeList[r][c].y +largeList[r][c].ht:
                                largeList[r][c].type=1
                                if ctClicks == 1:

                                    start_r=r
                                    start_c=c
                                    largeList[r][c].level=0
                                    fringe.append(largeList[r][c])


                                else:
                                    end_r = r
                                    end_c = c
            else:
                searching_iterative()
                ctStart = 0



        # check if user click any button and we use it to put walls
        if event.type ==pygame.KEYDOWN:

            # check if user click the mouse button in the area of the board not outside
            if pygame.mouse.get_pos()[1] < n * 70 and pygame.mouse.get_pos()[0] < n * 70:

                # tring to find the selected square that the user clicked on it and change its type to 1
                    for r in range(len(largeList)):
                        for c in range(n):
                            if pygame.mouse.get_pos()[0] > largeList[r][c].x and pygame.mouse.get_pos()[0] < largeList[r][c].x + largeList[r][c].wd and pygame.mouse.get_pos()[1] > largeList[r][c].y and pygame.mouse.get_pos()[1] < largeList[r][c].y + largeList[r][c].ht:
                                largeList[r][c].type = 2
                                visited.append(largeList[r][c])
                    tempVisited=visited.copy()





    # call function to draw
    drawing_Game()


