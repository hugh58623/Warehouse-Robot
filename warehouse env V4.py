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
color = ['white', 'black', 'red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'purple']

# shelf coordinates
X_Block_pic = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 27, 28, 29, 30, 31, 32, 33, 34,
               35, 36]
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
    upleft = (coordinate[0] - UNIT, coordinate[1] - UNIT)
    upright = (coordinate[0] + UNIT, coordinate[1] - UNIT)
    downleft = (coordinate[0] - UNIT, coordinate[1] + UNIT)
    downright = (coordinate[0] + UNIT, coordinate[1] + UNIT)
    upup = (coordinate[0], coordinate[1] - 2 * UNIT)
    downdown = (coordinate[0], coordinate[1] + 2 * UNIT)
    leftleft = (coordinate[0] - 2 * UNIT, coordinate[1])
    rightright = (coordinate[0] + 2 * UNIT, coordinate[1])
    nearby = (upleft, upright, downleft, downright, upup, downdown, leftleft, rightright)
    return nearby


def directNearbyEnvironment(coordinate):
    left = (coordinate[0] - UNIT, coordinate[1])
    right = (coordinate[0] + UNIT, coordinate[1])
    up = (coordinate[0], coordinate[1] - UNIT)
    down = (coordinate[0], coordinate[1] + UNIT)
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
        self.canvas.create_rectangle(0 * UNIT, 5 * UNIT, 1 * UNIT, 16 * UNIT, fill='sandybrown')
        self.canvas.create_rectangle(0 * UNIT, 17 * UNIT, 1 * UNIT, 21 * UNIT, fill='sandybrown')

        # create shelves
        for k in range(3, 36, 12):
            for i in range(2, 20, 5):
                self.canvas.create_rectangle(k * UNIT, i * UNIT, (k + 10) * UNIT, (i + 2) * UNIT, fill='bisque4')

        # define starting points
        self.org1 = self.canvas.create_rectangle(origin[0] - 10, origin[1] - 10, origin[0] + 10, origin[1] + 10)
        self.canvas.pack()

    def Targets(self, targets, i):
        # create targets
        X = random.choice(X_Block)
        Y = random.choice(Y_Block)
        self.target[i] = self.canvas.create_rectangle(X, Y, X + UNIT, Y + UNIT, fill=color[i])

        # create robot
        self.position[i] = (origin[0] - 10, origin[1] - 10)
        self.rect[i] = self.canvas.create_rectangle(self.position[i][0], self.position[i][1],
                                                    self.position[i][0] + 20, self.position[i][1] + 20,
                                                    fill=color[i])

        # target location
        if (Y - UNIT) in Y_Block:
            Y += UNIT
        else:
            Y -= UNIT

        targets[i] = [X, Y]
        return (targets)

    def render(self):
        time.sleep(0.01)
        self.update()

    # def action(self):

    def step(self, state, targets, action, i):
        if state[i] == 0:
            if self.position[i] == (origin[0] - 10, origin[1] - 10):
                action[i] = 3  # right
                self.position[i] = move(self.position, i, len(self.position), action)
            else:
                if targets[i][0] <= 480 and targets[i][0] >= 300:
                    if self.position[i][0] <= 240:
                        action[i] = 3  # right
                        self.position[i] = move(self.position, i, len(self.position), action)
                    else:
                        if self.position[i][1] != targets[i][1]:
                            if self.position[i][1] < targets[i][1]:
                                action[i] = 1  # down
                                self.position[i] = move(self.position, i, len(self.position), action)
                            else:
                                action[i] = 0  # up
                                self.position[i] = move(self.position, i, len(self.position), action)

                        else:
                            if self.position[i][0] != targets[i][0]:
                                if self.position[i][0] < targets[i][0]:
                                    action[i] = 3  # right
                                    self.position[i] = move(self.position, i, len(self.position), action)
                                else:
                                    action[i] = 2  # left
                                    self.position[i] = move(self.position, i, len(self.position), action)
                            else:
                                action[i] = 4  # wait
                                state[i] = 1
                elif targets[i][0] >= 540:
                    if self.position[i][0] <= 480:
                        action[i] = 3  # right
                        self.position[i] = move(self.position, i, len(self.position), action)
                    else:
                        if self.position[i][1] != targets[i][1]:
                            if self.position[i][1] < targets[i][1]:
                                action[i] = 1  # down
                                self.position[i] = move(self.position, i, len(self.position), action)
                            else:
                                action[i] = 0  # up
                                self.position[i] = move(self.position, i, len(self.position), action)

                        else:
                            if self.position[i][0] != targets[i][0]:
                                if self.position[i][0] < targets[i][0]:
                                    action[i] = 3  # right
                                    self.position[i] = move(self.position, i, len(self.position), action)
                                else:
                                    action[i] = 2  # left
                                    self.position[i] = move(self.position, i, len(self.position), action)
                            else:
                                action[i] = 4  # wait
                                state[i] = 1
                else:
                    if self.position[i][1] != targets[i][1]:
                        if self.position[i][1] < targets[i][1]:
                            action[i] = 1  # down
                            self.position[i] = move(self.position, i, len(self.position), action)
                        else:
                            action[i] = 0  # up
                            self.position[i] = move(self.position, i, len(self.position), action)

                    else:
                        if self.position[i][0] != targets[i][0]:
                            if self.position[i][0] < targets[i][0]:
                                action[i] = 3  # right
                                self.position[i] = move(self.position, i, len(self.position), action)
                            else:
                                action[i] = 2  # left
                                self.position[i] = move(self.position, i, len(self.position), action)
                        else:
                            action[i] = 4  # wait
                            state[i] = 1
            self.canvas.delete(self.rect[i])
            self.rect[i] = self.canvas.create_rectangle(self.position[i][0], self.position[i][1],
                                                        self.position[i][0] + 20, self.position[i][1] + 20,
                                                        fill=color[i])
            env.render()


        elif state[i] == 1:
            self.canvas.delete(self.target[i])
            if self.position[i] == (terminal[0] + 10, terminal[1] - 10):
                action[i] = 2  # left
                self.position[i] = move(self.position, i, len(self.position), action)
                state[i] = 2
            else:
                if targets[i][0] >= 300 and targets[i][0] <= 480:
                    if self.position[i][0] >= 300:
                        action[i] = 2  # left
                        self.position[i] = move(self.position, i, len(self.position), action)
                    else:
                        if self.position[i][1] != 320:
                            if self.position[i][1] < 320:
                                action[i] = 1  # down
                                self.position[i] = move(self.position, i, len(self.position), action)
                            else:
                                action[i] = 0  # up
                                self.position[i] = move(self.position, i, len(self.position), action)
                        else:
                            if self.position[i][0] != 20:
                                if self.position[i][0] < 20:
                                    action[i] = 3  # right
                                    self.position[i] = move(self.position, i, len(self.position), action)
                                else:
                                    action[i] = 2  # left
                                    self.position[i] = move(self.position, i, len(self.position), action)
                elif targets[i][0] >= 540:
                    if self.position[i][0] >= 540:
                        action[i] = 2  # left
                        self.position[i] = move(self.position, i, len(self.position), action)
                    else:
                        if self.position[i][1] != 320:
                            if self.position[i][1] < 320:
                                action[i] = 1  # down
                                self.position[i] = move(self.position, i, len(self.position), action)
                            else:
                                action[i] = 0  # up
                                self.position[i] = move(self.position, i, len(self.position), action)
                        else:
                            if self.position[i][0] != 20:
                                if self.position[i][0] < 20:
                                    action[i] = 3  # right
                                    self.position[i] = move(self.position, i, len(self.position), action)
                                else:
                                    action[i] = 2  # left
                                    self.position[i] = move(self.position, i, len(self.position), action)
                else:
                    if self.position[i][0] != 20:
                        if self.position[i][0] < 20:
                            action[i] = 3  # right
                            self.position[i] = move(self.position, i, len(self.position), action)
                        else:
                            action[i] = 2  # left
                            self.position[i] = move(self.position, i, len(self.position), action)
                    else:
                        if self.position[i][1] != 320:
                            if self.position[i][1] < 320:
                                action[i] = 1  # down
                                self.position[i] = move(self.position, i, len(self.position), action)
                            else:
                                action[i] = 0  # up
                                self.position[i] = move(self.position, i, len(self.position), action)
            self.canvas.delete(self.rect[i])
            self.rect[i] = self.canvas.create_rectangle(self.position[i][0], self.position[i][1],
                                                        self.position[i][0] + 20, self.position[i][1] + 20,
                                                        fill=color[i])
            env.render()

        else:
            self.canvas.delete(self.rect[i])
            state[i] = 3
            env.render()
        return (state)

    def update1(self):
        n = 6
        targets = []
        self.position = []
        action = []
        state = []
        self.rect = []
        self.target = []
        for i in range(n):
            self.target.append([0, 0])
            targets.append([0, 0])
            self.position.append([0, 0])
            state.append(0)
            action.append(3)
            self.rect.append([0, 0])
            targets = env.Targets(targets, i)
            for j in range(i + 1):
                state = self.step(state, targets, action, j)
                time.sleep(0.1)
        while 1:
            for i in range(n):
                state = self.step(state, targets, action, i)
                # print("0=", targets[0])
                # print("1=", targets[1])
                # print("2=", targets[2])
                time.sleep(0.1)
                if state[i] == 3:
                    state[i] = 0
                    targets = env.Targets(targets, i)


def move(position, i, n, action):
    for j in range(n):
        s = stateChecking(position[j], position[i], action[i])
        if s != 'no_collision':
            break

    if s == 'right_collision':
        if directNearbyEnvironment(position[i])[0][1] in Y_Block:
            position = (int(position[i][0]), int(position[i][1]) + UNIT)
        else:
            if directNearbyEnvironment(position[i])[1][1] in Y_Block:
                position = (int(position[i][0]), int(position[i][1]) - UNIT)
            else:
                position = (int(position[i][0]), int(position[i][1]) + UNIT)

    elif s == 'left_collision':
        if directNearbyEnvironment(position[i])[0][1] in Y_Block:
            position = (int(position[i][0]), int(position[i][1]) + UNIT)
        else:
            if directNearbyEnvironment(position[i])[1][1] in Y_Block:
                position = (int(position[i][0]), int(position[i][1]) - UNIT)
            else:
                position = (int(position[i][0]), int(position[i][1]) + UNIT)

    elif s == 'upward_collision':
        if directNearbyEnvironment(position[i])[3][0] in X_Block:
            position = (int(position[i][0]) - UNIT, int(position[i][1]))
        else:
            position = (int(position[i][0]) + UNIT, int(position[i][1]))

    elif s == 'downward_collision':
        if directNearbyEnvironment(position[i])[3][0] in X_Block:
            position = (int(position[i][0]) - UNIT, int(position[i][1]))
        else:
            position = (int(position[i][0]) + UNIT, int(position[i][1]))

    elif s == 'no_collision':
        position = moveagent(position[i], action[i])

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
    # position = [[40,60], [40,40], [40,80]]
    # action=[3,3,3]
    # move(position, 0, n, action)
    env.update1()
    # env.after(200, env.update(env.Xt,env.Yt))
    env.mainloop()

