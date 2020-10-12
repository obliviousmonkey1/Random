import random
# OUTDATED 

''' What we need'''
#Need height of list (y)
#Need length of list (x)

def movement(grid, player_pos, a_bool):
    player_new_pos = (0, 0)
    door_coord = (yd, xd)
    a_bool = True
    
    print ("\n" * 1)
    movement = input('Enter command: up/w, down/s, left/a, right/d, e(enter): ')

    if movement  == '':
        print("Please enter a command")
        return grid,player_pos, a_bool
    
    if movement.lower() == 'w' or movement.lower() == 'up':
        if player_pos[0]+1 >= len(grid):
            print("You can't move up")
            for i in range(len(grid)):
                p = len(grid)-1
                print(grid[p-i])
            return grid, player_pos, a_bool
        player_new_pos = player_pos[0]+1, player_pos[1]   

    elif movement.lower() == 's' or movement.lower() == 'down':
        if player_pos[0]-1 < 0:
            print("You can't move down")
            for i in range(len(grid)):
                p = len(grid)-1
                print(grid[p-i])
            return grid, player_pos, a_bool
        player_new_pos = player_pos[0]-1, player_pos[1]
    
    elif movement.lower() == 'd' or movement.lower() == 'right':
        if player_pos[1]+1 >= length:
            print("You can't move right")
            for i in range(len(grid)):
                p = len(grid)-1
                print(grid[p-i])
            return grid, player_pos, a_bool
        player_new_pos = player_pos[0], player_pos[1]+1

    elif movement.lower() == 'a' or movement.lower() == 'left':
        if player_pos[1]-1 < 0:
            print("You can't move left")
            for i in range(len(grid)):
                p = len(grid)-1
                print(grid[p-i])
            return grid, player_pos, a_bool
        player_new_pos = player_pos[0], player_pos[1]-1

    elif movement.lower() == 'e':
        try:
            if grid[player_pos[0]][player_pos[1]] != grid[door_coord[0]][door_coord[1]]:
                print("There is no door to enter through")
                return grid, player_pos, a_bool
        except:
            pass
        print('Well done you exited the dungeon')
        return grid, player_pos, False
    else:
        print("Please enter a command")
        return grid,player_pos, a_bool
    print ("\n" * 1)      
      

    row_del = player_new_pos[1]+1

    if player_new_pos == door_coord:  
        grid[player_new_pos[0]].insert(player_new_pos[1], 'p')
        grid[player_new_pos[0]].pop(player_new_pos[1]+1)
    else:
        grid[player_new_pos[0]].insert(player_new_pos[1], 'p')
        grid[player_new_pos[0]].pop(player_new_pos[1]+1)

    
    grid[player_pos[0]].pop(player_pos[1])
    grid[player_pos[0]].insert(player_pos[1],'_')

    
    if grid[yd][xd] != '#':
        if grid[door_coord[0]][door_coord[1]] == 'p':
           pass
        else:
            grid[door_coord[0]].insert(door_coord[1], '#')
            grid[door_coord[0]].pop(door_coord[1]+1)
        
    for i in range(len(grid)):
        p = len(grid)-1
        print(grid[p-i])

    
    return grid, player_new_pos, a_bool
                
print('''                             ,--.
                            {    }
                            K,   }
                           /  `Y`
                      _   /   /
                     {_'-K.__/
                       `/-.__L._
                       /  ' /`\_}
                      /  ' /     -ART BY ZEUS-
              ____   /  ' /
       ,-'~~~~    ~~/  ' /_
     ,'             ``~~~%%',
    (                     %  Y
   {                      %% I
  {      -                 %  `.
  |       ',                %  )
  |        |   ,..__      __. Y
  |    .,_./  Y ' / ^Y   J   )|
  \           |' /   |   |   ||
   \          L_/    . _ (_,.'(
    \,   ,      ^^""' / |      )
      \_  \          /,L]     /
        '-_`-,       ` `   ./`
           `-(_            )
               ^^\..___,.--` ''')
print('''▄▄▌ ▐ ▄▌▄▄▄ .▄▄▌   ▄▄·       • ▌ ▄ ·. ▄▄▄ .     ▄▄▄· ·▄▄▄▄   ▌ ▐·▄▄▄ . ▐ ▄ ▄▄▄▄▄▄• ▄▌▄▄▄  ▄▄▄ .▄▄▄  
██· █▌▐█▀▄.▀·██•  ▐█ ▌▪▪     ·██ ▐███▪▀▄.▀·    ▐█ ▀█ ██▪ ██ ▪█·█▌▀▄.▀·•█▌▐█•██  █▪██▌▀▄ █·▀▄.▀·▀▄ █·
██▪▐█▐▐▌▐▀▀▪▄██▪  ██ ▄▄ ▄█▀▄ ▐█ ▌▐▌▐█·▐▀▀▪▄    ▄█▀▀█ ▐█· ▐█▌▐█▐█•▐▀▀▪▄▐█▐▐▌ ▐█.▪█▌▐█▌▐▀▀▄ ▐▀▀▪▄▐▀▀▄ 
▐█▌██▐█▌▐█▄▄▌▐█▌▐▌▐███▌▐█▌.▐▌██ ██▌▐█▌▐█▄▄▌    ▐█ ▪▐▌██. ██  ███ ▐█▄▄▌██▐█▌ ▐█▌·▐█▄█▌▐█•█▌▐█▄▄▌▐█•█▌
 ▀▀▀▀ ▀▪ ▀▀▀ .▀▀▀ ·▀▀▀  ▀█▄▀▪▀▀  █▪▀▀▀ ▀▀▀      ▀  ▀ ▀▀▀▀▀• . ▀   ▀▀▀ ▀▀ █▪ ▀▀▀  ▀▀▀ .▀  ▀ ▀▀▀ .▀  ▀''')
print('\n')
##height = int(input('Please enter the height of the grid : '))
##length = int(input('Please enter the length of the grid : '))
b = True
score = 0
while b == True:
    height = random.randint(4,8)
    length = random.randint(4,height)
    print ("\n" * 1)
    grid = []
    a = True
    print(f'SCORE IS : {score}')
    player_pos = (0, 0)

    for i in range(height):
        grid.append([])

    for i in range(len(grid)):
        for x in range(length):
            grid[i].append('_')

    grid[0].insert(0, 'p')

    for y in range(len(grid)):
        for x in range(length):
            if grid[y][x] == 'p':
                grid[y].pop(length)

    yd = random.randint(0, height-1)
    xd = random.randint(1, length-1)

    try:
        grid[yd].insert(xd, '#')
    except:
        grid[yd].insert(1, '#')
        xd = 1
        print('insert')
        
    try:
        grid[yd].pop(xd+1)
    except:
        grid[yd].pop(1)

        
    print('xd',xd,'length', length)
    print('yd',yd, 'height', height)
          
    for i in range(len(grid)):
            p = len(grid)-1
            print(grid[p-i])

    while a == True:
        
        grid, player_pos, a = movement(grid, player_pos, a)

    score+=1
    

