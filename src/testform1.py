#! /usr/bin/env python
#
# GUI module generated by PAGE version 4.9
# In conjunction with Tcl version 8.6
#    May 04, 2017 10:16:05 AM
import sys
import time

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = 0
except ImportError:
    import tkinter.ttk as ttk
    py3 = 1

import test_support



def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    test_support.set_Tk_var()
    top = SwipeSense_Product_Functional_ (root)
    test_support.init(root, top)
    top.update_clock()
    root.mainloop()

w = None
def create_SwipeSense_Product_Functional_(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    test_support.set_Tk_var()
    top = SwipeSense_Product_Functional_ (w)
    test_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_SwipeSense_Product_Functional_():
    global w
    w.destroy()
    w = None




class SwipeSense_Product_Functional_:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("1168x879+-1858+677")
        top.title("SwipeSense Product Functional ")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")
        top.wm_iconbitmap('swipesense1.ico')



        self.menubar = Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.settings = Menu(top,tearoff=0)
        self.menubar.add_cascade(menu=self.settings,
                activebackground="#d9d9d9",
                activeforeground="#000000",
                background="#d9d9d9",
                font="TkMenuFont",
                foreground="#000000",
                label="Settings")
        self.settings.add_command(
                activebackground="#d8d8d8",
                activeforeground="#000000",
                background="#d9d9d9",
                command=test_support.configDataBase,
                font="TkMenuFont",
                foreground="#000000",
                label="Database")
        self.settings.add_command(
                activebackground="#d8d8d8",
                activeforeground="#000000",
                background="#d9d9d9",
                command=test_support.configSerialPort,
                font="TkMenuFont",
                foreground="#000000",
                label="Serial Port")
        self.settings.add_command(
                activebackground="#d8d8d8",
                activeforeground="#000000",
                background="#d9d9d9",
                command=test_support.extraMenuItem,
                font="TkMenuFont",
                foreground="#000000",
                label="Test Station")
        


        self.Labelframe1 = LabelFrame(top)
        self.Labelframe1.place(relx=0.02, rely=0.03, relheight=0.19
                , relwidth=0.96)
        self.Labelframe1.configure(relief=GROOVE)
        self.Labelframe1.configure(foreground="black")
        self.Labelframe1.configure(text='''Pending...''')
        self.Labelframe1.configure(background="#d9d9d9")
        self.Labelframe1.configure(highlightbackground="#d9d9d9")
        self.Labelframe1.configure(highlightcolor="black")
        self.Labelframe1.configure(width=1120)

        self.MessageDB = Message(self.Labelframe1)
        self.MessageDB.place(relx=0.01, rely=0.24, relheight=0.27, relwidth=0.31)

        self.MessageDB.configure(anchor=W)
        self.MessageDB.configure(background="#d9d9d9")
        self.MessageDB.configure(foreground="#000000")
        self.MessageDB.configure(highlightbackground="#d9d9d9")
        self.MessageDB.configure(highlightcolor="black")
        self.MessageDB.configure(text= "Database: ")
        self.MessageDB.configure(width=318)

        self.MessageDBS = Message(self.Labelframe1)
        self.MessageDBS.place(relx=0.01, rely=0.55, relheight=0.27, relwidth=0.31)
        self.MessageDBS.configure(anchor=W)
        self.MessageDBS.configure(background="#d9d9d9")
        self.MessageDBS.configure(foreground="#000000")
        self.MessageDBS.configure(highlightbackground="#d9d9d9")
        self.MessageDBS.configure(highlightcolor="black")
        self.MessageDBS.configure(text=" DB Status: ")
        self.MessageDBS.configure(width=318)

        self.MessageTF = Message(self.Labelframe1)
        self.MessageTF.place(relx=0.33, rely=0.55, relheight=0.27, relwidth=0.31)

        self.MessageTF.configure(anchor=W)
        self.MessageTF.configure(background="#d9d9d9")
        self.MessageTF.configure(foreground="#000000")
        self.MessageTF.configure(highlightbackground="#d9d9d9")
        self.MessageTF.configure(highlightcolor="black")
        self.MessageTF.configure(text='''Test Fixture:''')
        self.MessageTF.configure(width=150)

        self.MessageTS = Message(self.Labelframe1)
        self.MessageTS.place(relx=0.33, rely=0.24, relheight=0.27, relwidth=0.31)

        self.MessageTS.configure(anchor=W)
        self.MessageTS.configure(background="#d9d9d9")
        self.MessageTS.configure(foreground="#000000")
        self.MessageTS.configure(highlightbackground="#d9d9d9")
        self.MessageTS.configure(highlightcolor="black")
        self.MessageTS.configure(text='''Test Station:''')
        self.MessageTS.configure(width=150)

        self.MessageWO = Message(self.Labelframe1)
        self.MessageWO.place(relx=0.66, rely=0.24, relheight=0.27, relwidth=0.31)

        self.MessageWO.configure(anchor=W)
        self.MessageWO.configure(background="#d9d9d9")
        self.MessageWO.configure(foreground="#000000")
        self.MessageWO.configure(highlightbackground="#d9d9d9")
        self.MessageWO.configure(highlightcolor="black")
        self.MessageWO.configure(text='''Work Order''')
        self.MessageWO.configure(width=150)

        self.MessagePN = Message(self.Labelframe1)
        self.MessagePN.place(relx=0.66, rely=0.55, relheight=0.27, relwidth=0.31)
        self.MessagePN.configure(anchor=W)
        self.MessagePN.configure(background="#d9d9d9")
        self.MessagePN.configure(foreground="#000000")
        self.MessagePN.configure(highlightbackground="#d9d9d9")
        self.MessagePN.configure(highlightcolor="black")
        self.MessagePN.configure(text='''Part Number''')
        self.MessagePN.configure(width=150)

        self.Labelframe2 = LabelFrame(top)
        self.Labelframe2.place(relx=0.03, rely=0.26, relheight=0.29
                , relwidth=0.95)
        self.Labelframe2.configure(relief=GROOVE)
        self.Labelframe2.configure(foreground="black")
        self.Labelframe2.configure(text='''PRODUCTION FUNCTION''')
        self.Labelframe2.configure(background="#d9d9d9")
        self.Labelframe2.configure(highlightbackground="#d9d9d9")
        self.Labelframe2.configure(highlightcolor="black")
        self.Labelframe2.configure(width=1110)

        self.MessageOP = Message(self.Labelframe2)
        self.MessageOP.place(relx=0.18, rely=0.16, relheight=0.17, relwidth=0.52)

        self.MessageOP.configure(background="#d9d9d9")
        self.MessageOP.configure(foreground="#000000")
        self.MessageOP.configure(highlightbackground="#d9d9d9")
        self.MessageOP.configure(highlightcolor="black")
        self.MessageOP.configure(text='''PLACE UNIT ON FIXTURE AND SCAN TO START TEST..''')
        self.MessageOP.configure(width=574)

        self.Message9 = Message(self.Labelframe2)
        self.Message9.place(relx=0.01, rely=0.75, relheight=0.17, relwidth=0.1)
        self.Message9.configure(background="#d9d9d9")
        self.Message9.configure(foreground="#000000")
        self.Message9.configure(highlightbackground="#d9d9d9")
        self.Message9.configure(highlightcolor="black")
        self.Message9.configure(text='''Message''')
        self.Message9.configure(width=100)

        self.Entry1 = Entry(self.Labelframe2)
        self.Entry1.place(relx=0.32, rely=0.51, relheight=0.11, relwidth=0.26)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(highlightbackground="#d9d9d9")
        self.Entry1.configure(highlightcolor="black")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(selectbackground="#c4c4c4")
        self.Entry1.configure(selectforeground="black")
        self.Entry1.configure(textvariable=test_support.barCodeEntry)
        self.Entry1.bind('<Return>',test_support.getBarcodeEntry)

        self.Button1 = Button(self.Labelframe2)
        self.Button1.place(relx=0.89, rely=0.27, height=51, width=80)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Button''')

        self.Button2 = Button(self.Labelframe2)
        self.Button2.place(relx=0.89, rely=0.63, height=51, width=80)
        self.Button2.configure(activebackground="#d9d9d9")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''Button''')

        self.CheckOption1 = Checkbutton(self.Labelframe2)
        self.CheckOption1.place(relx=0.01, rely=0.31, relheight=0.17
                , relwidth=0.11)
        self.CheckOption1.configure(activebackground="#d9d9d9")
        self.CheckOption1.configure(activeforeground="#000000")
        self.CheckOption1.configure(background="#d9d9d9")
        self.CheckOption1.configure(disabledforeground="#a3a3a3")
        self.CheckOption1.configure(foreground="#000000")
        self.CheckOption1.configure(highlightbackground="#d9d9d9")
        self.CheckOption1.configure(highlightcolor="black")
        self.CheckOption1.configure(justify=LEFT)
        self.CheckOption1.configure(text='''OPTION 1''')
        self.CheckOption1.configure(variable=test_support.che58)

        self.CheckOption2 = Checkbutton(self.Labelframe2)
        self.CheckOption2.place(relx=0.01, rely=0.51, relheight=0.17
                , relwidth=0.11)
        self.CheckOption2.configure(activebackground="#d9d9d9")
        self.CheckOption2.configure(activeforeground="#000000")
        self.CheckOption2.configure(background="#d9d9d9")
        self.CheckOption2.configure(disabledforeground="#a3a3a3")
        self.CheckOption2.configure(foreground="#000000")
        self.CheckOption2.configure(highlightbackground="#d9d9d9")
        self.CheckOption2.configure(highlightcolor="black")
        self.CheckOption2.configure(justify=LEFT)
        self.CheckOption2.configure(text='''OPTION 2''')
        self.CheckOption2.configure(variable=test_support.che59)

        self.TProgressbar = ttk.Progressbar(self.Labelframe2)
        self.TProgressbar.place(relx=0.32, rely=0.82, relwidth=0.26
                , relheight=0.0, height=22)
        self.TProgressbar.configure(variable=test_support.TestProgress)

        self.Labelframe3 = LabelFrame(top)
        self.Labelframe3.place(relx=0.03, rely=0.59, relheight=0.4
                , relwidth=0.93)
        self.Labelframe3.configure(relief=GROOVE)
        self.Labelframe3.configure(foreground="black")
        self.Labelframe3.configure(text='''RESULTS''')
        self.Labelframe3.configure(background="#d9d9d9")
        self.Labelframe3.configure(highlightbackground="#d9d9d9")
        self.Labelframe3.configure(highlightcolor="black")
        self.Labelframe3.configure(width=1090)

        self.TextResults = Text(self.Labelframe3)
        self.TextResults.place(relx=0.03, rely=0.17, relheight=0.8
                , relwidth=0.29)
        self.TextResults.configure(background="#c0c0c0")
        self.TextResults.configure(font="TkTextFont")
        self.TextResults.configure(foreground="black")
        self.TextResults.configure(highlightbackground="#d9d9d9")
        self.TextResults.configure(highlightcolor="black")
        self.TextResults.configure(insertbackground="black")
        self.TextResults.configure(selectbackground="#c4c4c4")
        self.TextResults.configure(selectforeground="black")
        self.TextResults.configure(width=314)
        self.TextResults.configure(wrap=WORD)

        self.Canvas1 = Canvas(self.Labelframe3)
        self.Canvas1.place(relx=0.35, rely=0.17, relheight=0.8, relwidth=0.47)
        self.Canvas1.configure(background="white")
        self.Canvas1.configure(borderwidth="2")
        self.Canvas1.configure(highlightbackground="#d9d9d9")
        self.Canvas1.configure(highlightcolor="black")
        self.Canvas1.configure(insertbackground="black")
        self.Canvas1.configure(relief=RIDGE)
        self.Canvas1.configure(selectbackground="#c4c4c4")
        self.Canvas1.configure(selectforeground="black")
        self.Canvas1.configure(width=509)

        self.Button3 = Button(self.Labelframe3)
        self.Button3.place(relx=0.9, rely=0.31, height=51, width=80)
        self.Button3.configure(activebackground="#d9d9d9")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="#d9d9d9")
        self.Button3.configure(disabledforeground="#a3a3a3")
        self.Button3.configure(foreground="#000000")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(pady="0")
        self.Button3.configure(text='''Button''')

        self.Button4 = Button(self.Labelframe3)
        self.Button4.place(relx=0.9, rely=0.68, height=51, width=80)
        self.Button4.configure(activebackground="#d9d9d9")
        self.Button4.configure(activeforeground="#000000")
        self.Button4.configure(background="#d9d9d9")
        self.Button4.configure(disabledforeground="#a3a3a3")
        self.Button4.configure(foreground="#000000")
        self.Button4.configure(highlightbackground="#d9d9d9")
        self.Button4.configure(highlightcolor="black")
        self.Button4.configure(pady="0")
        self.Button4.configure(text='''EXIT''')
        self.Button4.bind('<ButtonRelease-1>',lambda e:test_support.button4OnClick(e))
    
    def update_clock(self):
 #       now = time.strftime("%c")
        now = time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.gmtime())
        self.Labelframe1.configure(text= now)
        root.after(1000,self.update_clock)    
        


if __name__ == '__main__':
    vp_start_gui()



