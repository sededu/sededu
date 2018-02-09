import Tkinter as tk
import random
from . import guiUtils as gui

root = tk.Tk()
w = 800
h = 600 # make these intelligent to screen size with other package?
o = 100
root.geometry(str(w) + "x" + str(h) + "+" + str(o) + "+" + str(o)) # width x height + x_offset + y_offset:

#a = gui.gridPlace(6, [100, 300])
a = gui.testing.testing()
print a

b = gui.placement.gridButton(10, [100, 100])
print b

categories = ['Rivers','Deltas','Deserts','Coasts','Stratigraphy','Behind the Module'] # read these from file?
labels = range(len(categories))
for i in labels:
    ct = [random.randrange(256) for x in range(3)]
    brightness = int(round(0.299*ct[0] + 0.587*ct[1] + 0.114*ct[2]))
    ct_hex = "%02x%02x%02x" % tuple(ct)
    bg_colour = '#' + "".join(ct_hex)
    l = tk.Label(root, 
        text=categories[i], 
            fg='White' if brightness < 120 else 'Black', 
            bg=bg_colour)
    l.place(x = 20, y = 30 + i*30, width=120, height=25)


def createWidgets(self):
        self.quitButton = tk.Button(self, text='Quit',
            command=self.quit)
        self.quitButton.grid()

#app.master.title('Sample application')
root.mainloop()
