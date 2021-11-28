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

    def targets1(self):
        #create targets
        X = random.choice(X_Block)
        Y = random.choice(Y_Block)
        self.target1 = self.canvas.create_rectangle(X, Y, X+UNIT, Y+UNIT, fill='light salmon')


        # create robot
        self.position1 = (origin[0] - 10, origin[1] - 10)
        self.rect1 = self.canvas.create_rectangle(self.position1[0], self.position1[1], self.position1[0] + 20, self.position1[1] + 20,fill='light salmon')

        #target location
        self.Xt = X
        if (Y - UNIT) in Y_Block:
            self.Yt = Y + UNIT
        else:
            self.Yt = Y - UNIT

        targets=[self.Xt, self.Yt]
        return(targets)
        # self.canvas.pack()
        # env.render()

        # position = self.canvas.create_rectangle(self.Xt, self.Yt, self.Xt + 20, self.Yt + 20,fill='SkyBlue1')
        # pack all
        # self.canvas.pack()
    def targets2(self):
        #create targets
        X = random.choice(X_Block)
        Y = random.choice(Y_Block)
        self.target2 = self.canvas.create_rectangle(X, Y, X+UNIT, Y+UNIT, fill='sandybrown')


        # create robot
        self.position2 = (origin[0] - 10, origin[1] - 10)
        self.rect2 = self.canvas.create_rectangle(self.position2[0], self.position2[1], self.position2[0] + 20, self.position2[1] + 20,fill='sandybrown')

        #target location
        self.Xt = X
        if (Y - UNIT) in Y_Block:
            self.Yt = Y + UNIT
        else:
            self.Yt = Y - UNIT

        targets=[self.Xt, self.Yt]
        return(targets)

    def targets3(self):
        #create targets
        X = random.choice(X_Block)
        Y = random.choice(Y_Block)
        self.target3 = self.canvas.create_rectangle(X, Y, X+UNIT, Y+UNIT, fill='SkyBlue1')


        # create robot
        self.position3 = (origin[0] - 10, origin[1] - 10)
        self.rect3 = self.canvas.create_rectangle(self.position3[0], self.position3[1], self.position3[0] + 20, self.position3[1] + 20,fill='SkyBlue1')

        #target location
        self.Xt = X
        if (Y - UNIT) in Y_Block:
            self.Yt = Y + UNIT
        else:
            self.Yt = Y - UNIT

        targets=[self.Xt, self.Yt]
        return(targets)



    def render(self):
        time.sleep(0.01)
        self.update()

    # def moveAgent(self):


    def step1(self, state, targets):
        if state == 0:
            if self.position1 == (origin[0] - 10, origin[1] - 10):
                self.position1 = (int(self.position1[0]) + UNIT, int(self.position1[1]))
            else:
                # print(self.position)
                if self.position1[1] != targets[1]:
                    if self.position1[1] < targets[1]:
                        self.position1 = (int(self.position1[0]), int(self.position1[1]) + UNIT)
                    else:
                        self.position1 = (int(self.position1[0]), int(self.position1[1]) - UNIT)
                else:
                    if self.position1[0] != targets[0]:
                        if self.position1[0] < targets[0]:
                            self.position1 = (int(self.position1[0]) + UNIT, int(self.position1[1]))
                        else:
                            self.position1 = (int(self.position1[0]) - UNIT, int(self.position1[1]))
                    else:
                        state = 1
            self.canvas.delete(self.rect1)
            self.rect1 = self.canvas.create_rectangle(self.position1[0], self.position1[1],
                                                      self.position1[0] + 20, self.position1[1] + 20,
                                                      fill='light salmon')
            env.render()


        elif state == 1:
            if self.position1 == (terminal[0] + 10, terminal[1] - 10):
                self.position1 = (int(self.position1[0]) - UNIT, int(self.position1[1]))
                state = 2
            else:
                # print(self.position)
                if self.position1[0] != 20:
                    if self.position1[0] < 20:
                        self.position1 = (int(self.position1[0]) + UNIT, int(self.position1[1]))
                    else:
                        self.position1 = (int(self.position1[0]) - UNIT, int(self.position1[1]))
                else:
                    if self.position1[1] != 320:
                        if self.position1[1] < 320:
                            self.position1 = (int(self.position1[0]), int(self.position1[1]) + UNIT)
                        else:
                            self.position1 = (int(self.position1[0]), int(self.position1[1]) - UNIT)
            self.canvas.delete(self.rect1)
            self.rect1 = self.canvas.create_rectangle(self.position1[0], self.position1[1],
                                                      self.position1[0] + 20, self.position1[1] + 20,
                                                      fill='light salmon')
            env.render()

        else:
            self.canvas.delete(self.rect1)
            self.canvas.delete(self.target1)
            state = 3
            env.render()
        return(state)

    def step2(self, state, targets):
        if state == 0:
            if self.position2 == (origin[0] - 10, origin[1] - 10):
                self.position2 = (int(self.position2[0]) + UNIT, int(self.position2[1]))
            else:
                # print(self.position)
                if self.position2[1] != targets[1]:
                    if self.position2[1] < targets[1]:
                        self.position2 = (int(self.position2[0]), int(self.position2[1]) + UNIT)
                    else:
                        self.position2 = (int(self.position2[0]), int(self.position2[1]) - UNIT)
                else:
                    if self.position2[0] != targets[0]:
                        if self.position2[0] < targets[0]:
                            self.position2 = (int(self.position2[0]) + UNIT, int(self.position2[1]))
                        else:
                            self.position2 = (int(self.position2[0]) - UNIT, int(self.position2[1]))
                    else:
                        state = 1
            self.canvas.delete(self.rect2)
            self.rect2 = self.canvas.create_rectangle(self.position2[0], self.position2[1],
                                                      self.position2[0] + 20, self.position2[1] + 20,
                                                      fill='sandybrown')
            env.render()


        elif state == 1:
            if self.position2 == (terminal[0] + 10, terminal[1] - 10):
                self.position2 = (int(self.position2[0]) - UNIT, int(self.position2[1]))
                state = 2
            else:
                # print(self.position)
                if self.position2[0] != 20:
                    if self.position2[0] < 20:
                        self.position2 = (int(self.position2[0]) + UNIT, int(self.position2[1]))
                    else:
                        self.position2 = (int(self.position2[0]) - UNIT, int(self.position2[1]))
                else:
                    if self.position2[1] != 320:
                        if self.position2[1] < 320:
                            self.position2 = (int(self.position2[0]), int(self.position2[1]) + UNIT)
                        else:
                            self.position2 = (int(self.position2[0]), int(self.position2[1]) - UNIT)
            self.canvas.delete(self.rect2)
            self.rect2 = self.canvas.create_rectangle(self.position2[0], self.position2[1],
                                                      self.position2[0] + 20, self.position2[1] + 20,
                                                      fill='sandybrown')
            env.render()

        else:
            self.canvas.delete(self.rect2)
            self.canvas.delete(self.target2)
            state = 3
            env.render()

        return (state)


    def step3(self, state, targets):
        if state == 0:
            if self.position3 == (origin[0] - 10, origin[1] - 10):
                self.position3 = (int(self.position3[0]) + UNIT, int(self.position3[1]))
            else:
                # print(self.position)
                if self.position3[1] != targets[1]:
                    if self.position3[1] < targets[1]:
                        self.position3 = (int(self.position3[0]), int(self.position3[1]) + UNIT)
                    else:
                        self.position3 = (int(self.position3[0]), int(self.position3[1]) - UNIT)
                else:
                    if self.position3[0] != targets[0]:
                        if self.position3[0] < targets[0]:
                            self.position3 = (int(self.position3[0]) + UNIT, int(self.position3[1]))
                        else:
                            self.position3 = (int(self.position3[0]) - UNIT, int(self.position3[1]))
                    else:
                        state = 1
            self.canvas.delete(self.rect3)
            self.rect3 = self.canvas.create_rectangle(self.position3[0], self.position3[1],
                                                      self.position3[0] + 20, self.position3[1] + 20,
                                                      fill='SkyBlue1')
            env.render()


        elif state == 1:
            if self.position3 == (terminal[0] + 10, terminal[1] - 10):
                self.position3 = (int(self.position3[0]) - UNIT, int(self.position3[1]))
                state = 2
            else:
                # print(self.position)
                if self.position3[0] != 20:
                    if self.position3[0] < 20:
                        self.position3 = (int(self.position3[0]) + UNIT, int(self.position3[1]))
                    else:
                        self.position3 = (int(self.position3[0]) - UNIT, int(self.position3[1]))
                else:
                    if self.position3[1] != 320:
                        if self.position3[1] < 320:
                            self.position3 = (int(self.position3[0]), int(self.position3[1]) + UNIT)
                        else:
                            self.position3 = (int(self.position3[0]), int(self.position3[1]) - UNIT)
            self.canvas.delete(self.rect3)
            self.rect3 = self.canvas.create_rectangle(self.position3[0], self.position3[1],
                                                      self.position3[0] + 20, self.position3[1] + 20,
                                                      fill='SkyBlue1')
            env.render()
        else:
            self.canvas.delete(self.rect3)
            self.canvas.delete(self.target3)
            state = 3
            env.render()
        return (state)

def update():
    state1 = 0  # 3: reset 2: terminal. 1: way to terminal. 0: way to target
    state2 = 0  # 3: reset 2: terminal. 1: way to terminal. 0: way to target
    state3 = 0  # 3: reset 2: terminal. 1: way to terminal. 0: way to target
    targets1 = env.targets1()
    targets2 = env.targets2()
    targets3 = env.targets3()
    env.step1(state1, targets1)
    time.sleep(0.01)
    env.step1(state1, targets1)
    env.step2(state2, targets2)
    time.sleep(0.01)
    while 1:
        state1 = env.step1(state1, targets1)
        state2 = env.step2(state2, targets2)
        state3 = env.step3(state3, targets3)
        if state1 == 3:
            state1 = 0
            targets1 = env.targets1()

        if state2 == 3:
            state2 = 0
            targets2 = env.targets2()

        if state3 == 3:
            state3 = 0
            targets3 = env.targets3()



if __name__ == '__main__':
    env = Maze()
    # env.after(200, env.update(env.Xt,env.Yt))
    # env.targets1()
    # env.targets2()
    # env.targets3()
    update()
    env.mainloop()

