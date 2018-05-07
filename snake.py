import random
import curses
import time

stdscr = curses.initscr()
curses.cbreak()
stdscr.keypad(1)
stdscr.nodelay(1)
curses.curs_set(0)
sy, sx = stdscr.getmaxyx()

while(1):
    stdscr.erase()
    s_pos = []
    s_pos.append([sy/2, sx/4])

    stdscr.addstr(s_pos[0][0], s_pos[0][1], "#")

    dir = [0, 1]

    food = [random.randint(1, sy-1), random.randint(1, sx-1)]
    stdscr.addch(food[0], food[1], "*")

    gameover = False
    while(1):
        time.sleep(.1)
        c = stdscr.getch()
        if c == curses.KEY_UP:
            dir = [-1, 0]
        elif c == curses.KEY_DOWN:
            dir = [1, 0]
        elif c == curses.KEY_RIGHT:
            dir = [0, 1]
        elif c == curses.KEY_LEFT:
            dir = [0, -1]

        newHead = [s_pos[0][0] + dir[0], s_pos[0][1] + dir[1]]

        for i in range(len(s_pos)):
            if(newHead == s_pos[i] or not 0 < newHead[0] < sy or not 0 < newHead[1] < sx ):
                gameover = True
                break
        if(gameover):
            break

        stdscr.addch(newHead[0], newHead[1], "#")
        s_pos.insert(0, newHead)

        if(newHead != food):
            oldHead = s_pos.pop()
            stdscr.addch(oldHead[0], oldHead[1], " ")
        else:
            food = None


        while food == None:
            food = [random.randint(1, sy-1), random.randint(1, sx-1)]
            for i in range(len(s_pos)):
                if food == s_pos[i]:
                    food = None
                    break

        stdscr.addch(food[0], food[1], "*")