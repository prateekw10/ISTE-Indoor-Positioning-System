import curses
import time
myscreen = curses.initscr()
myscreen.border(0)

object = open("sample.txt", "r")
print "Name of the file: ", object.name

myX=[]
myY=[]
lines = object.readlines()

i=0      
for line in lines:
    line=line.split(' ')  
    x=int(line[0])
    y=int(line[1])
    myscreen.addstr(x,y,"A")
    time.sleep(1)
    myscreen.refresh()
    myscreen.clear()
   

object.close()  
    





myscreen.getch()

curses.endwin()
