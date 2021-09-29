from tkinter import *
import random
root =Tk()
root.title("memoreis_game")
# root.title('codemy.com - Match Game!')
# root.iconbitmap('c:/gui/codemy.ico')
# root.geometry("500*550")
# create our matches

matches = [1,1,2,2,3,3,4,4,5,5,6,6,]
# suffle our matches
random.shuffle(matches)

print(matches)


root.mainloop()