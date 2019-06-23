# import tkinter as tk
#
# app = tk.Tk()
# app.geometry('150x100')
#
# chkValue = tk.BooleanVar()
# chkValue.set(True)
#
# chkExample = tk.Checkbutton(app, text='Check Box', var=chkValue)
# chkExample.grid(column=0, row=0)
#
# print("The checkbutton original value is {}".format(chkValue.get()))
# chkExample.select()
# print("The checkbutton value after toggled is {}".format(chkValue.get()))
# chkExample.deselect()
# print("The checkbutton value after toggled twice is {}".format(chkValue.get()))
#
# app.mainloop()

# import tkinter as tk
#
# app = tk.Tk()
# app.geometry('150x100')
#
# chkValue = tk.StringVar()
#
# chkExample = tk.Checkbutton(app, text='Check Box', var=chkValue,
#                             onvalue="RGB", offvalue="YCbCr")
# chkExample.grid(column=0, row=0)
#
# chkExample.select()
# print("The checkbutton value when selected is {}".format(chkValue.get()))
# # chkExample.deselect()
# # print("The checkbutton value when deselected is {}".format(chkValue.get()))
#
# app.mainloop()

# from tkinter import *
# class Checkbar(Frame):
#    def __init__(self, parent=None, picks=[], side=LEFT, anchor=W):
#       Frame.__init__(self, parent)
#       self.vars = []
#       for pick in picks:
#          var = IntVar()
#          chk = Checkbutton(self, text=pick, variable=var)
#          chk.pack(side=side, anchor=anchor, expand=YES)
#          self.vars.append(var)
#    def state(self):
#       return map((lambda var: var.get()), self.vars)
#
# if __name__ == '__main__':
#    root = Tk()
#    lng = Checkbar(root, ['Python', 'Ruby', 'Perl', 'C++'])
#    tgl = Checkbar(root, ['English','German'])
#    lng.pack(side=TOP,  fill=X)
#    tgl.pack(side=LEFT)
#    lng.config(relief=GROOVE, bd=2)
#
#    def allstates():
#       print(list(lng.state()), list(tgl.state()))
#    Button(root, text='Quit', command=root.quit).pack(side=RIGHT)
#    Button(root, text='Peek', command=allstates).pack(side=RIGHT)
#    root.mainloop()
# import tkinter as tk
#
# class MyDialog:
#    def __init__(self, parent):
#       top = self.top = tk.Toplevel(parent)
#       self.myLabel = tk.Label(top, text='Enter your username below')
#       self.myLabel.pack()
#
#       self.myEntryBox = tk.Entry(top)
#       self.myEntryBox.pack()
#
#       self.mySubmitButton = tk.Button(top, text='Submit', command=self.send)
#       self.mySubmitButton.pack()
#
#    def send(self):
#       global username
#       username = self.myEntryBox.get()
#       self.top.destroy()
#
#
# def onClick():
#    inputDialog = MyDialog(root)
#    root.wait_window(inputDialog.top)
#    print('Username: ', username)
#
#
# username = 'Empty'
# root = tk.Tk()
# mainLabel = tk.Label(root, text='Example for pop up input box')
# mainLabel.pack()
#
# mainButton = tk.Button(root, text='Click me', command=onClick)
# mainButton.pack()
#
# root.mainloop()

# from tkinter import *
#
# class GUI(object):
#     def __init__(self, master):
#         self.master = master
#         master.title("Variabelen")
#         Label(master, text="Min").grid(row=0, column=1)
#         Label(master, text="Max").grid(row=0, column=2)
#         Label(master, text="Vaste waarde").grid(row=0, column=3)
#
#         Label(master, text="Oppervlakte chiller").grid(row=1)
#         Label(master, text="Diameter buizen").grid(row=2)
#
#         aChillerMin = Entry(master)
#         aChillerMax = Entry(master)
#         dMin = Entry(master)
#         dMax = Entry(master)
#
#         aChillerMin.grid(row=1, column=1)
#         aChillerMax.grid(row=1, column=2)
#         aChillerVast = IntVar()
#
#         def activateCheck():
#             if aChillerVast.get() == 1:          #whenever checked
#                 aChillerMax.config(state=NORMAL)
#             elif aChillerVast.get() == 0:        #whenever unchecked
#                 aChillerMax.config(state=DISABLED)
#
#         chk = Checkbutton(root, variable=aChillerVast, command=activateCheck).grid(row = 1, column = 3)    #command is given
#
#         aChillerMax.config(state=DISABLED)
#
#         dMin.grid(row=2, column=1)
#         dMax.grid(row=2, column=2)
#
# root = Tk()
# myGUI = GUI(root)
# root.mainloop()

# import matplotlib.pyplot as plt
#
# ax1 = plt.subplot(131)
# ax1.scatter([1, 2], [3, 4])
# ax1.set_xlim([0, 5])
# ax1.set_ylim([0, 5])
#
#
# ax2 = plt.subplot(132)
# ax2.scatter([1, 2],[3, 4])
# ax2.set_xlim([0, 5])
# ax2.set_ylim([0, 5])
# plt.show()

#
# import matplotlib.pyplot as plt
#
# fig, ax = plt.subplots()
# ax.scatter(0, 0)
# ax.scatter(0, 0.5)
# ax.scatter(0.8, 0.14)
# ax.scatter(-0.4, -0.75)
# ax.scatter(-0.14, -1.4)
# ax.annotate("x", (0, 0.1))
# ax.annotate("y", (0, 0.6))
# ax.annotate("z", (0.8, 0.2))
# ax.annotate("p", (-0.4, -0.7))
# ax.annotate("q", (-0.14, -1.3))
# ax.add_patch(plt.Circle((0, 0), 1, color='r', alpha=0.2))
# ax.add_patch(plt.Circle((0, 0.5), 1, color='r', alpha=0.2))
# ax.add_patch(plt.Circle((0.8, 0.14), 1, color='r', alpha=0.2))
# ax.add_patch(plt.Circle((-0.4, -0.75), 1, color='r', alpha=0.2))
# ax.add_patch(plt.Circle((-0.14, -1.4), 1, color='r', alpha=0.2))
#
#
# #Use adjustable='box-forced' to make the plot area square-shaped as well.
# ax.set_aspect('equal', adjustable='datalim')
# ax.plot()   #Causes an autoscale update.
# plt.show()

# import matplotlib.pyplot as plt
#
# # line 1 points
# x1 = [50, 60, 70, 80, 90, 100]
# y1 = [0.9193, 0.920, 0.8947, 0.8848, 0.8786, 0.8790]
# # plotting the line 1 points
# plt.plot(x1, y1, label="Fault-Tolerant Mean")
#
# # line 2 points
# y2 = [0.8607, 0.8502, 0.8421, 0.8332, 0.8223, 0.8224]
# plt.xticks(x1)
# # plotting the line 2 points
# plt.plot(x1, y2, label="Fault-Tolerant Midpoint")
# # y3 = [23, 19, 18, 16, 15, 14]
# # plt.plot(x1, y3, label="Field size = 70x70")
# #
# # y4 = [32, 29, 26, 24, 22, 21]
# # plt.plot(x1, y4, label="Field size = 80x80")
#
#
# # naming the x axis
# plt.xlabel('Number of sensors')
# # naming the y axis
# plt.ylabel('Average convergence rates after running simulation 100 times')
# # giving a title to my graph
# # plt.title('Graph!')
#
# # show a legend on the plot
# plt.legend()
#
# # function to show the plot
# plt.show()

# import tkinter as tk
#
#
# def on_configure(event):
#     # update scrollregion after starting 'mainloop'
#     # when all widgets are in canvas
#     canvas.configure(scrollregion=canvas.bbox('all'))
#
#
# root = tk.Tk()
#
# # --- create canvas with scrollbar ---
#
# canvas = tk.Canvas(root)
# canvas.pack(side=tk.LEFT)
#
# scrollbar = tk.Scrollbar(root, command=canvas.yview)
# scrollbar.pack(side=tk.LEFT, fill='y')
#
# canvas.configure(yscrollcommand = scrollbar.set)
#
# # update scrollregion after starting 'mainloop'
# # when all widgets are in canvas
# canvas.bind('<Configure>', on_configure)
#
# # --- put frame in canvas ---
#
# frame = tk.Frame(canvas)
# canvas.create_window((0,0), window=frame, anchor='nw')
#
# # --- add widgets in frame ---
#
# l = tk.Label(frame, text="Hello", font="-size 50")
# l.pack()
#
# l = tk.Label(frame, text="World", font="-size 50")
# l.pack()
#
# l = tk.Label(frame, text="Test text 1\nTest text 2\nTest text 3\nTest text 4\nTest text 5\nTest text 6\nTest text 7\nTest text 8\nTest text 9", font="-size 20")
# l.pack()
#
# # --- start program ---
#
# root.mainloop()


import tkinter as tk

root=tk.Tk()

class Application (tk.Frame):
    def __init__(self,master):
        tk.Frame.__init__(self, master)
        self.grid()
        self.create_windgets()

    def DoNothing(self):
        print("")

    def Compute(self):
        self.sampleButton['state']='normal'
        self.CB1['state']='normal'

    def create_windgets (self):

        self.sampleButton=tk.Button(self, text="Sample",state='disable' , command=self.DoNothing)
        self.sampleButton.grid()

        # self.EDButton=tk.Button(self, text="Enable")
        # self.EDButton.grid()

        self.o1=tk.BooleanVar()
        self.CB1 = tk.Checkbutton(self, text="submit", state='active', variable=self.o1, command=self.Compute)
        self.CB1.grid()

app=Application(root)
root.mainloop()