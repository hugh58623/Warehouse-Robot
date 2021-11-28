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
i = 0
color = ['white','black','red', 'orange', 'yellow', 'green', 'blue','indigo', 'purple']



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
    if action == 0 and (alien_agent == directEnvironment[0]):
        return 'upward_collision'
    elif action == 1 and (alien_agent == directEnvironment[1]):
        return 'downward_collision'
    elif action == 2 and (alien_agent == directEnvironment[2]):
        return 'left_collision'
    elif action == 3 and (alien_agent == directEnvironment[3]):
        return 'right_collision'
    else:
        return 'no_collision'

def indirectNearbyEnvironment(coordinate):
    upleft = [coordinate[0]-UNIT, coordinate[1]-UNIT]
    upright = [coordinate[0]+UNIT, coordinate[1]-UNIT]
    downleft = [coordinate[0]-UNIT, coordinate[1]+UNIT]
    downright = [coordinate[0]+UNIT, coordinate[1]+UNIT]
    upup = [coordinate[0], coordinate[1]-2*UNIT]
    downdown = [coordinate[0], coordinate[1]+2*UNIT]
    leftleft = [coordinate[0]-2*UNIT, coordinate[1]]
    rightright = [coordinate[0]+2*UNIT, coordinate[1]]
    nearby = [upleft, upright, downleft, downright, upup, downdown, leftleft, rightright]
    return nearby

def directNearbyEnvironment(coordinate):
    left = (coordinate[0]-UNIT, coordinate[1])
    right = (coordinate[0]+UNIT, coordinate[1])
    up = (coordinate[0], coordinate[1]-UNIT)
    down = (coordinate[0], coordinate[1]+UNIT)
    nearby = (up, down, left, right)
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
        self.target1 = self.canvas.create_rectangle(X, Y, X+UNIT, Y+UNIT, fill='tomato')


        # create robot
        self.position1 = (origin[0] - 10, origin[1] - 10)
        self.rect1 = self.canvas.create_rectangle(self.position1[0], self.position1[1], self.position1[0] + 20, self.position1[1] + 20,fill='tomato')

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
        self.target2 = self.canvas.create_rectangle(X, Y, X+UNIT, Y+UNIT, fill='green')


        # create robot
        self.position2 = (origin[0] - 10, origin[1] - 10)
        self.rect2 = self.canvas.create_rectangle(self.position2[0], self.position2[1], self.position2[0] + 20, self.position2[1] + 20,fill='green')

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

    # def action(self):

    def step1(self, state, targets):
        if state == 0:
            if self.position1 == (origin[0] - 10, origin[1] - 10):
                action1 = 3  # right
                self.position1 = move(self.position2, self.position3, self.position1, action1, state)
            else:
                if targets[0] <= 480 and targets[0]>= 300:
                    if self.position1[0] <= 240:
                        action1 = 3  # right
                        self.position1 = move(self.position2, self.position3, self.position1, action1, state)
                    else:
                        if self.position1[1] != targets[1]:
                            if self.position1[1] < targets[1]:
                                action1 = 1  # down
                                self.position1 = move(self.position2, self.position3, self.position1, action1, state)
                            else:
                                action1 = 0  # up
                                self.position1 = move(self.position2, self.position3, self.position1, action1, state)

                        else:
                            if self.position1[0] != targets[0]:
                                if self.position1[0] < targets[0]:
                                    action1 = 3  # right
                                    self.position1 = move(self.position2, self.position3, self.position1, action1,
                                                          state)
                                else:
                                    action1 = 2  # left
                                    self.position1 = move(self.position2, self.position3, self.position1, action1,
                                                          state)
                            else:
                                action1 = 4  # wait
                                state = 1
                elif targets[0] >= 540:
                    if self.position1[0] <= 480:
                        action1 = 3  # right
                        self.position1 = move(self.position2, self.position3, self.position1, action1, state)
                    else:
                        if self.position1[1] != targets[1]:
                            if self.position1[1] < targets[1]:
                                action1 = 1  # down
                                self.position1 = move(self.position2, self.position3, self.position1, action1, state)
                            else:
                                action1 = 0  # up
                                self.position1 = move(self.position2, self.position3, self.position1, action1, state)

                        else:
                            if self.position1[0] != targets[0]:
                                if self.position1[0] < targets[0]:
                                    action1 = 3  # right
                                    self.position1 = move(self.position2, self.position3, self.position1, action1,
                                                          state)
                                else:
                                    action1 = 2  # left
                                    self.position1 = move(self.position2, self.position3, self.position1, action1,
                                                          state)
                            else:
                                action1 = 4  # wait
                                state = 1
                else:
                    if self.position1[1] != targets[1]:
                        if self.position1[1] < targets[1]:
                            action1 = 1  # down
                            self.position1 = move(self.position2, self.position3, self.position1, action1, state)
                        else:
                            action1 = 0  # up
                            self.position1 = move(self.position2, self.position3, self.position1, action1, state)

                    else:
                        if self.position1[0] != targets[0]:
                            if self.position1[0] < targets[0]:
                                action1 = 3  # right
                                self.position1 = move(self.position2, self.position3, self.position1, action1, state)
                            else:
                                action1 = 2  # left
                                self.position1 = move(self.position2, self.position3, self.position1, action1, state)
                        else:
                            action1 = 4  # wait
                            state = 1
            self.canvas.delete(self.rect1)
            self.rect1 = self.canvas.create_rectangle(self.position1[0], self.position1[1],
                                                      self.position1[0] + 20, self.position1[1] + 20,
                                                      fill='tomato')
            env.render()


        elif state == 1:
            self.canvas.delete(self.target1)
            if self.position1 == (terminal[0] + 10, terminal[1] - 10):
                action1 = 2  # left
                self.position1 = move(self.position2, self.position3, self.position1, action1, state)
                state = 2
            else:
                if targets[0] >= 300 and targets[0] <= 480:
                    if self.position1[0] >= 300:
                        action1 = 2  # left
                        self.position1 = move(self.position2, self.position3, self.position1, action1, state)
                    else:
                        if self.position1[1] != 320:
                            if self.position1[1] < 320:
                                action1 = 1  # down
                                self.position1 = move(self.position2, self.position3, self.position1, action1, state)
                            else:
                                action1 = 0  # up
                                self.position1 = move(self.position2, self.position3, self.position1, action1, state)
                        else:
                            if self.position1[0] != 20:
                                if self.position1[0] < 20:
                                    action1 = 3  # right
                                    self.position1 = move(self.position2, self.position3, self.position1, action1, state)
                                else:
                                    action1 = 2  # left
                                    self.position1 = move(self.position2, self.position3, self.position1, action1, state)
                elif targets[0] >= 540:
                    if self.position1[0] >= 540:
                        action1 = 2  # left
                        self.position1 = move(self.position2, self.position3, self.position1, action1, state)
                    else:
                        if self.position1[1] != 320:
                            if self.position1[1] < 320:
                                action1 = 1  # down
                                self.position1 = move(self.position2, self.position3, self.position1, action1, state)
                            else:
                                action1 = 0  # up
                                self.position1 = move(self.position2, self.position3, self.position1, action1, state)
                        else:
                            if self.position1[0] != 20:
                                if self.position1[0] < 20:
                                    action1 = 3  # right
                                    self.position1 = move(self.position2, self.position3, self.position1, action1, state)
                                else:
                                    action1 = 2  # left
                                    self.position1 = move(self.position2, self.position3, self.position1, action1, state)
                else:
                    if self.position1[0] != 20:
                        if self.position1[0] < 20:
                            action1 = 3  # right
                            self.position1 = move(self.position2, self.position3, self.position1, action1, state)
                        else:
                            action1 = 2  # left
                            self.position1 = move(self.position2, self.position3, self.position1, action1, state)
                    else:
                        if self.position1[1] != 320:
                            if self.position1[1] < 320:
                                action1 = 1  # down
                                self.position1 = move(self.position2, self.position3, self.position1, action1, state)
                            else:
                                action1 = 0  # up
                                self.position1 = move(self.position2, self.position3, self.position1, action1, state)
            self.canvas.delete(self.rect1)
            self.rect1 = self.canvas.create_rectangle(self.position1[0], self.position1[1],
                                                      self.position1[0] + 20, self.position1[1] + 20,
                                                      fill='light salmon')
            env.render()

        else:
            self.canvas.delete(self.rect1)
            state = 3
            env.render()
        return(state)

    def step2(self, state, targets):
        if state == 0:
            if self.position2 == (origin[0] - 10, origin[1] - 10):
                action2 = 3
                self.position2 = move(self.position1, self.position3, self.position2, action2, state)
            else:
                if targets[0] <= 480 and targets[0] >= 300:
                    if self.position2[0] <= 240:
                        action2 = 3  # right
                        self.position2 = move(self.position1, self.position3, self.position2, action2, state)
                    else:
                        if self.position2[1] != targets[1]:
                            if self.position2[1] < targets[1]:
                                action2 = 1  # down
                                self.position2 = move(self.position1, self.position3, self.position2, action2, state)
                            else:
                                action2 = 0  # up
                                self.position2 = move(self.position1, self.position3, self.position2, action2, state)

                        else:
                            if self.position2[0] != targets[0]:
                                if self.position2[0] < targets[0]:
                                    action2 = 3  # right
                                    self.position2 = move(self.position1, self.position3, self.position2, action2,
                                                          state)
                                else:
                                    action2 = 2  # left
                                    self.position2 = move(self.position1, self.position3, self.position2, action2,
                                                          state)
                            else:
                                action2 = 4
                                state = 1
                elif targets[0] >= 540:
                    if self.position2[0] <= 480:
                        action2 = 3  # right
                        self.position2 = move(self.position1, self.position3, self.position2, action2, state)
                    else:
                        if self.position2[1] != targets[1]:
                            if self.position2[1] < targets[1]:
                                action2 = 1  # down
                                self.position2 = move(self.position1, self.position3, self.position2, action2, state)
                            else:
                                action2 = 0  # up
                                self.position2 = move(self.position1, self.position3, self.position2, action2, state)

                        else:
                            if self.position2[0] != targets[0]:
                                if self.position2[0] < targets[0]:
                                    action2 = 3  # right
                                    self.position2 = move(self.position1, self.position3, self.position2, action2,
                                                          state)
                                else:
                                    action2 = 2  # left
                                    self.position2 = move(self.position1, self.position3, self.position2, action2,
                                                          state)
                            else:
                                action2 = 4
                                state = 1
                else:
                    if self.position2[1] != targets[1]:
                        if self.position2[1] < targets[1]:
                            action2 = 1  # down
                            self.position2 = move(self.position1, self.position3, self.position2, action2, state)
                        else:
                            action2 = 0  # up
                            self.position2 = move(self.position1, self.position3, self.position2, action2, state)

                    else:
                        if self.position2[0] != targets[0]:
                            if self.position2[0] < targets[0]:
                                action2 = 3  # right
                                self.position2 = move(self.position1, self.position3, self.position2, action2, state)
                            else:
                                action2 = 2  # left
                                self.position2 = move(self.position1, self.position3, self.position2, action2, state)
                        else:
                            action2 = 4
                            state = 1
            self.canvas.delete(self.rect2)
            self.rect2 = self.canvas.create_rectangle(self.position2[0], self.position2[1],
                                                      self.position2[0] + 20, self.position2[1] + 20,
                                                      fill='green')
            env.render()


        elif state == 1:
            self.canvas.delete(self.target2)
            if self.position2 == (terminal[0] + 10, terminal[1] - 10):
                action2 = 2
                self.position2 = move(self.position1, self.position3, self.position2, action2, state)
                state = 2
            else:
                if targets[0] >= 300 and targets[0] <= 480:
                    if self.position2[0] >= 300:
                        action2 = 2  # left
                        self.position2 = move(self.position1, self.position3, self.position2, action2, state)
                    else:
                        if self.position2[1] != 320:
                            if self.position2[1] < 320:
                                action2 = 1  # down
                                self.position2 = move(self.position1, self.position3, self.position2, action2, state)
                            else:
                                action2 = 0  # up
                                self.position2 = move(self.position1, self.position3, self.position2, action2, state)
                        else:
                            if self.position2[0] != 20:
                                if self.position2[0] < 20:
                                    action2 = 3  # right
                                    self.position2 = move(self.position1, self.position3, self.position2, action2, state)
                                else:
                                    action2 = 2  # left
                                    self.position2 = move(self.position1, self.position3, self.position2, action2, state)
                elif targets[0] >= 540:
                    if self.position2[0] >= 540:
                        action2 = 2  # left
                        self.position2 = move(self.position1, self.position3, self.position2, action2, state)
                    else:
                        if self.position2[1] != 320:
                            if self.position2[1] < 320:
                                action2 = 1  # down
                                self.position2 = move(self.position1, self.position3, self.position2, action2, state)
                            else:
                                action2 = 0  # up
                                self.position2 = move(self.position1, self.position3, self.position2, action2, state)
                        else:
                            if self.position2[0] != 20:
                                if self.position2[0] < 20:
                                    action2 = 3  # right
                                    self.position2 = move(self.position1, self.position3, self.position2, action2, state)
                                else:
                                    action2 = 2  # left
                                    self.position2 = move(self.position1, self.position3, self.position2, action2, state)
                else:
                    if self.position2[0] != 20:
                        if self.position2[0] < 20:
                            action2 = 3
                            self.position2 = move(self.position1, self.position3, self.position2, action2, state)
                        else:
                            action2 = 2
                            self.position2 = move(self.position1, self.position3, self.position2, action2, state)
                    else:
                        if self.position2[1] != 320:
                            if self.position2[1] < 320:
                                action2 = 1
                                self.position2 = move(self.position1, self.position3, self.position2, action2, state)
                            else:
                                action2 = 0
                                self.position2 = move(self.position1, self.position3, self.position2, action2, state)
            self.canvas.delete(self.rect2)
            self.rect2 = self.canvas.create_rectangle(self.position2[0], self.position2[1],
                                                      self.position2[0] + 20, self.position2[1] + 20,
                                                      fill='green')
            env.render()

        else:
            self.canvas.delete(self.rect2)
            state = 3
            env.render()

        return (state)


    def step3(self, state, targets):
        if state == 0:
            if self.position3 == (origin[0] - 10, origin[1] - 10):
                action3 = 3
                self.position3 = move(self.position1, self.position2, self.position3, action3, state)
            else:
                if targets[0] <= 480 and targets[0] >= 300:
                    if self.position3[0] <= 240:
                        action3 = 3  # right
                        self.position3 = move(self.position1, self.position2, self.position3, action3, state)
                    else:
                        if self.position3[1] != targets[1]:
                            if self.position3[1] < targets[1]:
                                action3 = 1  # down
                                self.position3 = move(self.position1, self.position2, self.position3, action3, state)
                            else:
                                action3 = 0  # up
                                self.position3 = move(self.position1, self.position2, self.position3, action3, state)
                        else:
                            if self.position3[0] != targets[0]:
                                if self.position3[0] < targets[0]:
                                    action3 = 3  # right
                                    self.position3 = move(self.position1, self.position2, self.position3, action3,
                                                          state)
                                else:
                                    action3 = 2  # left
                                    self.position3 = move(self.position1, self.position2, self.position3, action3,
                                                          state)
                            else:
                                action3 = 4
                                state = 1
                elif targets[0] >= 540:
                    if self.position3[0] <= 480:
                        action3 = 3  # right
                        self.position3 = move(self.position1, self.position2, self.position3, action3, state)
                    else:
                        if self.position3[1] != targets[1]:
                            if self.position3[1] < targets[1]:
                                action3 = 1  # down
                                self.position3 = move(self.position1, self.position2, self.position3, action3, state)
                            else:
                                action3 = 0  # up
                                self.position3 = move(self.position1, self.position2, self.position3, action3, state)
                        else:
                            if self.position3[0] != targets[0]:
                                if self.position3[0] < targets[0]:
                                    action3 = 3  # right
                                    self.position3 = move(self.position1, self.position2, self.position3, action3,
                                                          state)
                                else:
                                    action3 = 2  # left
                                    self.position3 = move(self.position1, self.position2, self.position3, action3,
                                                          state)
                            else:
                                action3 = 4
                                state = 1
                else:
                    if self.position3[1] != targets[1]:
                        if self.position3[1] < targets[1]:
                            action3 = 1  # down
                            self.position3 = move(self.position1, self.position2, self.position3, action3, state)
                        else:
                            action3 = 0  # up
                            self.position3 = move(self.position1, self.position2, self.position3, action3, state)
                    else:
                        if self.position3[0] != targets[0]:
                            if self.position3[0] < targets[0]:
                                action3 = 3  # right
                                self.position3 = move(self.position1, self.position2, self.position3, action3, state)
                            else:
                                action3 = 2  # left
                                self.position3 = move(self.position1, self.position2, self.position3, action3, state)
                        else:
                            action3 = 4
                            state = 1
            self.canvas.delete(self.rect3)
            self.rect3 = self.canvas.create_rectangle(self.position3[0], self.position3[1],
                                                      self.position3[0] + 20, self.position3[1] + 20,
                                                      fill='SkyBlue1')
            env.render()


        elif state == 1:
            self.canvas.delete(self.target3)
            if self.position3 == (terminal[0] + 10, terminal[1] - 10):
                action3 = 2
                self.position3 = move(self.position1, self.position2, self.position3, action3, state)
                state = 2
            else:
                if targets[0] >= 300 and targets[0] <= 480:
                    if self.position3[0] >= 300:
                        action3 = 2  # left
                        self.position3 = move(self.position1, self.position2, self.position3, action3, state)
                    else:
                        if self.position3[1] != 320:
                            if self.position3[1] < 320:
                                action3 = 1  # down
                                self.position3 = move(self.position1, self.position2, self.position3, action3, state)
                            else:
                                action3 = 0  # up
                                self.position3 = move(self.position1, self.position2, self.position3, action3, state)
                        else:
                            if self.position3[0] != 20:
                                if self.position3[0] < 20:
                                    action3 = 3  # right
                                    self.position3 = move(self.position1, self.position2, self.position3, action3, state)
                                else:
                                    action3 = 2  # left
                                    self.position3 = move(self.position1, self.position2, self.position3, action3, state)
                elif targets[0] >= 540:
                    if self.position3[0] >= 540:
                        action3 = 2  # left
                        self.position3 = move(self.position1, self.position2, self.position3, action3, state)
                    else:
                        if self.position3[1] != 320:
                            if self.position3[1] < 320:
                                action3 = 1  # down
                                self.position3 = move(self.position1, self.position2, self.position3, action3, state)
                            else:
                                action3 = 0  # up
                                self.position3 = move(self.position1, self.position2, self.position3, action3, state)
                        else:
                            if self.position3[0] != 20:
                                if self.position3[0] < 20:
                                    action3 = 3  # right
                                    self.position3 = move(self.position1, self.position2, self.position3, action3, state)
                                else:
                                    action3 = 2  # left
                                    self.position3 = move(self.position1, self.position2, self.position3, action3, state)
                else:
                    if self.position3[0] != 20:
                        if self.position3[0] < 20:
                            action3 = 3
                            self.position3 = move(self.position1, self.position2, self.position3, action3, state)
                        else:
                            action3 = 2
                            self.position3 = move(self.position1, self.position2, self.position3, action3, state)
                    else:
                        if self.position3[1] != 320:
                            if self.position3[1] < 320:
                                action3 = 1
                                self.position3 = move(self.position1, self.position2, self.position3, action3, state)
                            else:
                                action3 = 0
                                self.position3 = move(self.position1, self.position2, self.position3, action3, state)
            self.canvas.delete(self.rect3)
            self.rect3 = self.canvas.create_rectangle(self.position3[0], self.position3[1],
                                                      self.position3[0] + 20, self.position3[1] + 20,
                                                      fill='SkyBlue1')
            env.render()
        else:
            self.canvas.delete(self.rect3)
            state = 3
            action3 = 4
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
    time.sleep(0.1)
    env.step1(state1, targets1)
    env.step2(state2, targets2)
    time.sleep(0.1)
    while 1:
        time.sleep(0.1)
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


def move(position1, position2, position3, action, state):
    if stateChecking(position1, position3, action) == 'right_collision' or stateChecking(position2, position3,
                                                                                         action) == 'right_collision':
        if directNearbyEnvironment(position3)[0][1] in Y_Block:
            position = (int(position3[0]), int(position3[1]) + UNIT)
        else:
            if directNearbyEnvironment(position3)[1][1] in Y_Block:
                position = (int(position3[0]), int(position3[1]) - UNIT)
            else:
                position = (int(position3[0]), int(position3[1]) + UNIT)

    elif stateChecking(position1, position3, action) == 'left_collision' or stateChecking(position2, position3,
                                                                                          action) == 'left_collision':
        if directNearbyEnvironment(position3)[0][1] in Y_Block:
            position = (int(position3[0]), int(position3[1]) + UNIT)
        else:
            if directNearbyEnvironment(position3)[1][1] in Y_Block:
                position = (int(position3[0]), int(position3[1]) - UNIT)
            else:
                position = (int(position3[0]), int(position3[1]) + UNIT)

    elif stateChecking(position1, position3, action) == 'upward_collision' or stateChecking(position2, position3,
                                                                                            action) == 'upward_collision':
        if directNearbyEnvironment(position3)[3][0] in [60, 300, 540]:
            position = (int(position3[0]) - UNIT, int(position3[1]))
        elif directNearbyEnvironment(position3)[2][0] in [0, 240, 480, 720]:
            position = (int(position3[0]) + UNIT, int(position3[1]))
        elif state == 0:
            position = (int(position3[0]) + UNIT, int(position3[1]))
        else:
            position = (int(position3[0]) - UNIT, int(position3[1]))

    elif stateChecking(position1, position3, action) == 'downward_collision' or stateChecking(position2, position3,
                                                                                              action) == 'downward_collision':
        if directNearbyEnvironment(position3)[3][0] in [60, 300, 540]:
            position = (int(position3[0]) - UNIT, int(position3[1]))
        elif directNearbyEnvironment(position3)[2][0] in [0, 240, 480, 720]:
            position = (int(position3[0]) + UNIT, int(position3[1]))
        elif state == 0:
            position = (int(position3[0]) + UNIT, int(position3[1]))
        else:
            position = (int(position3[0]) - UNIT, int(position3[1]))

    elif stateChecking(position1, position3, action) == 'no_collision' or stateChecking(position2, position3,
                                                                                        action) == 'no_collision':
        position = moveagent(position3, action)

    return (position)


def moveagent(position, action):
    if action == 0:
        position = (int(position[0]), int(position[1]) - UNIT)
    elif action == 1:
        position = (int(position[0]), int(position[1]) + UNIT)
    elif action == 2:
        position = (int(position[0]) - UNIT, int(position[1]))
    elif action == 3:
        position = (int(position[0]) + UNIT, int(position[1]))
    elif action == 4:
        position = position

    return (position)





if __name__ == '__main__':
    env = Maze()
    env.render()
    # env.after(200, env.update(env.Xt,env.Yt))
    # env.targets1()
    # env.targets2()
    # env.targets3()
    update()
    env.mainloop()

