import random

import numpy as np
import time
import sys

if sys.version_info.major == 2:
    import Tkinter as tk
else:
    import tkinter as tk

UNIT = 20  # pixels
MAZE_H = 21  # grid height
MAZE_W = 39  # grid width



# shelf coordinates
X_Block_pic = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]
X_Block = [element * UNIT for element in X_Block_pic]
Y_Block_pic = [2, 3, 7, 8, 12, 13, 17, 18]
Y_Block = [element * UNIT for element in Y_Block_pic]


origin = np.array([10, 90])
terminal = np.array([10, 330])

def stateChecking(alien_agent, key_agent, action):
    directEnvironment = directNearbyEnvironment(key_agent)

    indirectEnvironment = indirectNearbyEnvironment(key_agent)
    if action == 0 and (alien_agent in [directEnvironment[0], indirectEnvironment[0], indirectEnvironment[1]]):
            return 'upward_collision'
    elif action == 1 and (alien_agent in [directEnvironment[1], indirectEnvironment[2], indirectEnvironment[3]]):
            return 'downward_collision'
    elif action == 2 and (alien_agent in [directEnvironment[3], indirectEnvironment[1], indirectEnvironment[3]]):
            return 'right_collision'
    elif action == 3 and (alien_agent in [directEnvironment[2], indirectEnvironment[0], indirectEnvironment[2]]):
            return 'left_collision'
    else:
        return 'no_collision'

def indirectNearbyEnvironment(coordinate):
    upleft = [coordinate[0]-UNIT, coordinate[1]-UNIT, coordinate[2]-UNIT, coordinate[3]-UNIT]
    upright = [coordinate[0]+UNIT, coordinate[1]-UNIT, coordinate[2]+UNIT, coordinate[3]-UNIT]
    downleft = [coordinate[0]-UNIT, coordinate[1]+UNIT, coordinate[2]-UNIT, coordinate[3]+UNIT]
    downright = [coordinate[0]+UNIT, coordinate[1]+UNIT, coordinate[2]+UNIT, coordinate[3]+UNIT]
    nearby = [upleft, upright, downleft, downright]
    return nearby

def directNearbyEnvironment(coordinate):
    left = [coordinate[0]-UNIT, coordinate[1], coordinate[2]-UNIT, coordinate[3]]
    right = [coordinate[0]+UNIT, coordinate[1], coordinate[2]+UNIT, coordinate[3]]
    up = [coordinate[0], coordinate[1]-UNIT, coordinate[2], coordinate[3]-UNIT]
    down = [coordinate[0], coordinate[1]+UNIT, coordinate[2], coordinate[3]+UNIT]
    nearby = [up, down, left, right]
    return nearby


class Maze(tk.Tk, object):
    def __init__(self):
        super(Maze, self).__init__()
        self.title('Warehouse')
        self.geometry('{0}x{1}'.format(MAZE_H * UNIT, MAZE_H * UNIT))
        self._build_maze()

    def _build_maze(self):
        self.canvas = tk.Canvas(self, bg='oldlace', height=MAZE_H * UNIT, width=MAZE_W * UNIT)

        # create grids
        for c in range(0, MAZE_W * UNIT, UNIT):
            x0, y0, x1, y1 = c, 0, c, MAZE_H * UNIT
            self.canvas.create_line(x0, y0, x1, y1)
        for r in range(0, MAZE_H * UNIT, UNIT):
            x0, y0, x1, y1 = 0, r, MAZE_W * UNIT, r
            self.canvas.create_line(x0, y0, x1, y1)

        # create operation desks
        self.canvas.create_rectangle(0 * UNIT, 0 * UNIT, 1 * UNIT, 4 * UNIT, fill='sandybrown')
        self.canvas.create_rectangle(0 * UNIT, 5 * UNIT, 1 * UNIT, 16* UNIT, fill='sandybrown')
        self.canvas.create_rectangle(0 * UNIT, 17 * UNIT, 1 * UNIT, 21 * UNIT, fill='sandybrown')

        # create shelves
        for k in range(3, 36, 12):
            for i in range(2, 20, 5):
                self.canvas.create_rectangle(k * UNIT, i * UNIT, (k + 10) * UNIT, (i + 2) * UNIT, fill='bisque4')


        # define starting points
        self.org1 = self.canvas.create_rectangle(origin[0] - 10, origin[1] - 10, origin[0] + 10, origin[1] + 10)
        self.canvas.pack()


        #create targets
        X = random.choice(X_Block)
        Y = random.choice(Y_Block)
        self.target = self.canvas.create_rectangle(X, Y, X+UNIT, Y+UNIT, fill='SkyBlue1')


        # create robot
        self.position = (origin[0] - 10, origin[1] - 10)
        self.rect = self.canvas.create_rectangle(self.position[0], self.position[1], self.position[0] + 20, self.position[1] + 20,fill='SkyBlue1')

        #target location
        self.Xt = X
        if (Y - UNIT) in Y_Block:
            self.Yt = Y + UNIT
        else:
            self.Yt = Y - UNIT
        # position = self.canvas.create_rectangle(self.Xt, self.Yt, self.Xt + 20, self.Yt + 20,fill='SkyBlue1')
        # pack all
        self.canvas.pack()

    def moveAgent(self, Xt, Yt):
        state = 0  # 1: arrive. 0: not arrive
        while state == 0:
            time.sleep(0.5)
            if self.position == (origin[0] - 10, origin[1] - 10):
                self.position =  ( int(self.position[0]) + UNIT , int(self.position[1]))
            else:
                if self.position[1] != Yt:
                    if self.position[1] < Yt:
                        self.position =  ( int(self.position[0]) , int(self.position[1]) + UNIT )
                    else:
                        self.position =  ( int(self.position[0]) , int(self.position[1]) - UNIT )
                else:
                    if self.position[0] != Xt:
                        if self.position[0] < Xt:
                            self.position =  ( int(self.position[0]) + UNIT , int(self.position[1]))
                        else:
                            self.position =  ( int(self.position[0]) - UNIT , int(self.position[1]))
                    else:
                        state = 1
            self.canvas.delete(self.rect)
            self.rect = self.canvas.create_rectangle(self.position[0], self.position[1], self.position[0] + 20, self.position[1] + 20, fill='SkyBlue1')
            env.render()


        while state == 1:
            time.sleep(0.5)
            if self.position == (terminal[0] + 10, terminal[1] - 10):
                self.position =  ( int(self.position[0]) - UNIT , int(self.position[1]))
                state = 2
            else:
                if self.position[0] != 20:
                    if self.position[0] < 20:
                        self.position =  ( int(self.position[0]) + UNIT, int(self.position[1]))
                    else:
                        self.position =  ( int(self.position[0]) - UNIT, int(self.position[1]))
                else:
                    if self.position[1] != 320:
                        if self.position[1] < 320:
                            self.position =  ( int(self.position[0]), int(self.position[1]) + UNIT )
                        else:
                            self.position =  ( int(self.position[0]), int(self.position[1]) - UNIT )
            self.canvas.delete(self.rect)
            self.rect = self.canvas.create_rectangle(self.position[0], self.position[1], self.position[0] + 20, self.position[1] + 20, fill='SkyBlue1')
            env.render()

        while state == 2:
            time.sleep(0.5)
            self.canvas.delete(self.rect)
            env.render()


    def render(self):
        time.sleep(0.01)
        self.update()

if __name__ == '__main__':
    env = Maze()
    # env.after(200, env.update(env.Xt,env.Yt))
    env.moveAgent(env.Xt, env.Yt)
    env.mainloop()

