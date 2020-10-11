import random

class Grid_Maker():
    def __init__(self, grid, length, height):
        self.height = height
        self.length = length
        self.door_cord = ()
        self.grid = []

    def grid_init(self):
        #gets the height(y) and length(x) of a room in the dungeon 
        self.height = random.randint(4,10)
        self.length = random.randint(4,self.height)

        #sets up the grid based on the height 
        for i in range(self.height):
            self.grid.append([])

        #then appends to each y value a series of '_' based on length 
        for i in range(len(self.grid)):
            for x in range(self.length):
                self.grid[i].append('_')
        


    def dungeon_setup(self):
        #player position set up allways (0,0) at the start 
        self.grid[0].insert(0, 'p')
        self.grid[0].pop(2)

        #seting up the exit door.
        yd, xd = random.randint(0, self.height-1), random.randint(1, self.length-1)
        self.grid[yd].insert(xd, '#')
        self.grid[yd].pop(xd+1)
        self.door_cord = yd, xd

        return self.grid, self.door_cord


g = Grid_Maker([], 0, 0)
g.grid_init()
g.dungeon_setup()
print(g.door_cord)
