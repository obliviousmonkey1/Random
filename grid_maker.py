''' What we need'''
#Need height of list (y)
#Need length of list (x)

def movement(grid, player_pos):
    player_new_pos = (0, 0)
    
    print ("\n" * 1)
    movement = input('Enter command: up/w, down/s, left/a, right/d : ')
    
    
    if movement.lower() == 'w' or movement.lower() == 'up':
        if player_pos[0]+1 >= len(grid):
            print("You can't move up")
            for i in range(len(grid)):
                p = len(grid)-1
                print(grid[p-i])
            return grid, player_pos
        player_new_pos = player_pos[0]+1, player_pos[1]   

    elif movement.lower() == 's' or movement.lower() == 'down':
        if player_pos[0]-1 < 0:
            print("You can't move down")
            for i in range(len(grid)):
                p = len(grid)-1
                print(grid[p-i])
            return grid, player_pos
        player_new_pos = player_pos[0]-1, player_pos[1]
    
    elif movement.lower() == 'd' or movement.lower() == 'right':
        if player_pos[1]+1 >= length:
            print("You can't move right")
            for i in range(len(grid)):
                p = len(grid)-1
                print(grid[p-i])
            return grid, player_pos 
        player_new_pos = player_pos[0], player_pos[1]+1

    elif movement.lower() == 'a' or movement.lower() == 'left':
        if player_pos[1]-1 < 0:
            print("You can't move left")
            for i in range(len(grid)):
                p = len(grid)-1
                print(grid[p-i])
            return grid, player_pos
        player_new_pos = player_pos[0], player_pos[1]-1
    print ("\n" * 1)
        
            
      

    row_del = player_new_pos[1]+1
  
    grid[player_new_pos[0]].insert(player_new_pos[1], 'p')
    grid[player_new_pos[0]].pop(random.randint(row_del, len(grid)))

    grid[player_pos[0]].pop(player_pos[1])
    grid[player_pos[0]].insert(player_pos[1],'_')
    

    for i in range(len(grid)):
        p = len(grid)-1
        print(grid[p-i])

    
    return grid, player_new_pos
                
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
height = int(input('Please enter the height of the grid : '))
length = int(input('Please enter the length of the grid : '))
print ("\n" * 1)
grid = []
a = True 

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
            

for i in range(len(grid)):
        p = len(grid)-1
        print(grid[p-i])

while a == True:
    
    grid, player_pos = movement(grid, player_pos)
    

