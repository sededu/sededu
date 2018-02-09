import Tkinter as tk
import random
from . import guiUtils as gui

root = tk.Tk()
root.wm_title("SedEdu")
w = 1000 #
h = 800 # make these intelligent to screen size with other package?
o = 100 #
root.geometry(str(w) + "x" + str(h) + "+" + str(o) + "+" + str(o)) # width x height + x_offset + y_offset:

categories = ["Rivers", "Deltas", "Deserts", "Coasts", "Stratigraphy", "Behind the \nModules"] # read these from file?
buttons = range(len(categories))
gridMargs = gui.placement.margins([w, h]) # workable area margins
gridWork = gui.placement.divideWindow(gridMargs)
gridPlace = gui.placement.gridButton(len(categories), gridWork)

for i in buttons:
    ct = [random.randrange(256) for x in range(3)]
    brightness = int(round(0.299*ct[0] + 0.587*ct[1] + 0.114*ct[2]))
    ct_hex = "%02x%02x%02x" % tuple(ct)
    bg_colour = '#' + "".join(ct_hex)
    l = tk.Button(root, 
            text=categories[i], font=("Courier", int(gridPlace.h*0.1)),
            fg='White' if brightness < 120 else 'Black', 
            bg=bg_colour)
    l.place(x = gridPlace.x[i], y = gridPlace.y[i], width=gridPlace.w, height=gridPlace.h)


def createWidgets(self):
        self.quitButton = tk.Button(self, text='Quit',
            command=self.quit)
        self.quitButton.grid()

#app.master.title('Sample application')
root.mainloop()
