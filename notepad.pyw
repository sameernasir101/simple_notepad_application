import os
import datetime
import tkvideo
from tkinter import *
import tkinter.messagebox as mbox
from tkinter.filedialog import askopenfilename, asksaveasfilename

cwd = os.path.dirname(os.path.abspath(__file__))


def Notepad():
    
    # HIDE THE LOADING SCREEN
    win.withdraw()
    
    # TITLEBAR TEXT (FILENAME)
    titleText = "Untitled - Notepad by Sameer"
    
    root = Tk()
    
    # DESTROY ALL WINDOWS
    def DestroyAllWindows():
        root.destroy()
        win.destroy()
        
    # CLOSE LOADING SCREEN TOO IF A NOTEPAD FILE IS CLOSED
    root.protocol('WM_DELETE_WINDOW', DestroyAllWindows)
    
    # SETTING PROGRAM DIMENSIONS
    windows_width = 775
    windows_height = 460
    position_x = int((screen_width/2)-(windows_width/2))
    position_y = int((screen_height/2)-(windows_height/2))-70
    
    # SETTING PROPERTIES FOR THE NOTEPAD WINDOW
    root.geometry(f"{windows_width}x{windows_height}+{position_x}+{position_y}")
    root.minsize(325,175)
    root.title(titleText)
    root.iconbitmap("icon.ico")
    root.focus_force()
    
    # -------------------------------------------------------------------------------------------
    
    # SET SCROLLBAR ON RIGHT SIDE (NO NEED FOR HORIZONTAL SCROLLBAR)
    scroll_y = Scrollbar(root, orient=VERTICAL)
    scroll_y.pack(side=RIGHT, fill=Y)
    
    # -------------------------------------------------------------------------------------------
    
    # MAKE A AREA FOR ENTRING TEXT
    textWindow = Text(root, font=("Consolas", 11), wrap=WORD, undo=True)
    textWindow.pack(fill=BOTH, expand=True)
    textWindow.focus_force()
    
    # -------------------------------------------------------------------------------------------
    
    # CONFIGURING THE SCROLLBAR AND TEXT AREA FOR SCROLLING
    scroll_y.config(command=textWindow.yview)
    textWindow.config(yscrollcommand=scroll_y.set)
    
    # -------------------------------------------------------------------------------------------
    
    # MAKE A MENU BAR IN CALCULATOR
    menuBar = Menu(root)
    
    global fileName
    fileName = None


    # METHODS FOR SUB MENU 1
    
    def SaveFile(event=None):
        global fileName
        if fileName == None:
            fileName = asksaveasfilename(initialfile="Untitled.txt", defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("Python Source Code Files", ".py"), ("All Files", "*.*")])
            if fileName == "":
                fileName = None
            else:
                with open(fileName, "w") as f:
                    f.write(textWindow.get(1.0, "end-1c"))
            root.title(fileName + " - Notepad by Sameer")
            textWindow.focus_force()
        else:
            with open(fileName, "w") as f:
                f.write(textWindow.get(1.0, "end-1c"))
            root.title(fileName + " - Notepad by Sameer")
            textWindow.focus_force()
            
    root.bind('<Control_L><S>', SaveFile)
    root.bind('<Control_L><s>', SaveFile)

    def NewFile(event=None):
        global fileName
        if textWindow.get(1.0, "end-1c") != '\n' and fileName == None:
            confirm = mbox.askyesnocancel("Notepad", "Do you want to save your current file?")
            textWindow.focus_force()
            if confirm == False:
                textWindow.delete(1.0, "end-1c")
                root.title("Untitled - Notepad by Sameer")
                fileName = None
                textWindow.focus_force()
            if confirm == True:
                SaveFile()
                textWindow.delete(1.0, "end-1c")
                root.title("Untitled - Notepad by Sameer")
                fileName = None
                textWindow.focus_force()
                
        else:
            textWindow.delete(1.0, "end-1c")
            root.title("Untitled - Notepad by Sameer")
            fileName = None
            textWindow.focus_force()
        
    root.bind('<Control_L><N>', NewFile)
    root.bind('<Control_L><n>', NewFile)
    
    def OpenFile(event=None):
        global fileName
        fileName = askopenfilename(defaultextension='.txt', filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if fileName == '':
            fileName = None
        else:
            root.title(os.path.basename(fileName) + " - Notepad by Sameer")
            textWindow.delete(1.0, "end-1c")
            with open(fileName, "r") as f:
                text = f.read()
                textWindow.insert(1.0, text)    
            textWindow.focus_force()
        
    root.bind('<Control_L><O>', OpenFile)
    root.bind('<Control_L><o>', OpenFile)
    
    def ClearAllText(event=None):
        if textWindow.get(1.0, "end-1c") != '\n':
            confirm = mbox.askyesnocancel("Notepad", "Do you want to clear all the text in your file?")
            textWindow.focus_force()
            if confirm == True:
                textWindow.delete(1.0, "end-1c")
        else:
            textWindow.delete(1.0, "end-1c")
    
    root.bind('<Control_L><Q>', ClearAllText)
    root.bind('<Control_L><q>', ClearAllText)
    
    def DestroyAll():
        if textWindow.get(1.0, "end-1c") != '\n':
            confirm = mbox.askyesnocancel("Notepad", "Do you want to save your file?")
            textWindow.focus_force()
            if confirm == False:
                root.destroy()
                win.destroy()
            elif confirm == True:
                SaveFile()
                root.destroy()
                win.destroy()
        else:
            root.destroy()
            win.destroy()
            
    
    # ENTER SUB MENUS TO MENUBAR (SUB-MENU 1)
    menu1 = Menu(menuBar, tearoff=0)
    menu1.add_command(label="New", accelerator="Ctlr+N", command=NewFile)
    menu1.add_command(label="Open", accelerator="Ctrl+O", command=OpenFile)
    menu1.add_command(label="Save", accelerator="Ctrl+S", command=SaveFile)
    menu1.add_separator()
    menu1.add_command(label="Clear All", accelerator="Ctrl+Q", command=ClearAllText)
    menu1.add_command(label="Exit", accelerator="Alt+F4", command=DestroyAll)


    # PACKING SUB MENU 1 INTO MENU BAR
    menuBar.add_cascade(menu=menu1, label="File")
    
    # -------------------------------------------------------------------------------------------

    # METHODS FOR SUB MENU 2
    
    root.bind('<Control_L><Z>', textWindow.edit_undo)
    root.bind('<Control_L><z>', textWindow.edit_undo)
    
    root.bind('<Control_L><Y>', textWindow.edit_redo)
    root.bind('<Control_L><y>', textWindow.edit_redo)
    
    def Cut():
        textWindow.event_generate(('<<Cut>>'))
    
    def Copy():
        textWindow.event_generate(('<<Copy>>'))
    
    def Paste():
        textWindow.event_generate(('<<Paste>>'))
            
    
    
    def Find(event=None):
        root1 = Toplevel()
        root1.geometry("330x130")
        root1.title("Find")
        root1.resizable(width=0, height=0)
        root1.iconbitmap("icon.ico")
        Label(root1, text="Enter the text you want to find").pack(side=TOP, pady=10)
        findKey = StringVar()
        entry = Entry(root1, font=("lucida", 11), textvariable=findKey)
        entry.pack(side=TOP, pady=10)
        root1.focus_force()
        entry.focus_force()

        def Search(event=0):
            
            textWindow.tag_remove('found', '1.0', END)
            s = entry.get() # Grabs the text from the entry box
            if s:
                idx = '1.0'
                while 1:
                    idx = textWindow.search(s, idx, nocase=1, stopindex=END)
                    if not idx: break
                    lastidx = '%s+%dc' % (idx, len(s))
                    textWindow.tag_add('found', idx, lastidx)
                    idx = lastidx
                    textWindow.see(idx)  # Once found, the scrollbar automatically scrolls to the text
                textWindow.tag_config('found', background='orange')
            entry.focus_set()
            def RestoreColor():
                textWindow.tag_remove('found', '1.0', END)
                root1.destroy()
            root1.protocol('WM_DELETE_WINDOW', RestoreColor)

        root1.bind('<Enter>', Search)

        
        
    root.bind('<Control_L><F>', Find)
    root.bind('<Control_L><f>', Find)
    
    def FindReplace(event=None):
        root1 = Toplevel()
        root1.geometry("330x150")
        root1.resizable(width=0, height=0)
        root1.title("Find and Replace")
        root1.iconbitmap("icon.ico")
        findKey = StringVar(value='Find')
        Label(root1, text="Enter the word you want to find and replace for.").pack(side=TOP, pady=5)
        replaceKey = StringVar(value='Replace')
        entry1 = Entry(root1, font=("lucida", 11), textvariable=findKey)
        entry1.pack( pady=8)
        entry2 = Entry(root1, font=("lucida", 11), textvariable=replaceKey)
        entry2.pack(pady=8)
        root1.focus_force()
        entry1.focus_force()

        def Search(event=0):
            
            textWindow.tag_remove('found', '1.0', END)
            s = entry1.get()
            r = entry2.get()
            if s and r:
                idx = '1.0'
                while 1:
                    idx = textWindow.search(s, idx, nocase=1, stopindex=END)
                    if not idx: break
                    lastidx = '%s+%dc' % (idx, len(s))
                    textWindow.delete(idx, lastidx) 
                    textWindow.insert(idx, r)
                    lastidx = '% s+% dc' % (idx, len(r)) 
                    textWindow.tag_add('found', idx, lastidx)
                    idx = lastidx
                    textWindow.see(idx)
                textWindow.tag_config('found', background='orange')
            entry1.focus_set()
            def RestoreColor():
                textWindow.tag_remove('found', '1.0', END)
                root1.destroy()
            root1.protocol('WM_DELETE_WINDOW', RestoreColor)

        root1.bind('<Return>', Search)

        Button(root1, text="Submit", command=Search).pack(side=TOP, pady=5)
    
    root.bind('<Control_L><G>', FindReplace)
    root.bind('<Control_L><g>', FindReplace)
    
    def SelectAll():
        textWindow.tag_add('sel', 1.0, "end-1c")

    
    def InsertDateTime(event=None):
        try:
            today = datetime.datetime.now()
            today = today.strftime("%H:%M:%S %p, %d/%m/%Y  ")
            textWindow.insert(index=INSERT, chars=today)
        except Exception:
            mbox.showerror("Error", "Sorry, could not insert Date/Time")
    
    root.bind('<Control_L><T>', InsertDateTime)
    root.bind('<Control_L><t>', InsertDateTime)
    
    # ENTER SUB MENUS TO MENUBAR (SUB-MENU 2)
    menu2 = Menu(menuBar, tearoff=0)
    menu2.add_command(label="Undo", accelerator="Ctrl+Z", command=textWindow.edit_undo)
    menu2.add_command(label="Redo", accelerator="Ctrl+Y", command=textWindow.edit_redo)
    menu2.add_separator()
    menu2.add_command(label="Cut", accelerator="Ctrl+X", command=Cut)
    menu2.add_command(label="Copy", accelerator="Ctrl+C", command=Copy)
    menu2.add_command(label="Paste", accelerator="Ctrl+V", command=Paste)
    menu2.add_separator()
    menu2.add_command(label="Find", accelerator="Ctrl+F", command=Find)
    menu2.add_command(label="Find and Replace", accelerator="Ctrl+G", command=FindReplace)
    menu2.add_separator()
    menu2.add_command(label="Select All", underline=7, accelerator="Ctrl+A",command=SelectAll)
    menu2.add_command(label="Insert Date/Time",  accelerator="Ctrl+T",command=InsertDateTime)
    
    
    # PACKING SUB MENU 2 INTO MENU BAR
    menuBar.add_cascade(menu=menu2, label="Edit")

    # -------------------------------------------------------------------------------------------

    # METHODS FOR SUB MENU 3
    checkVariable = IntVar(root)
    
    def AlwaysOnTop():
        if checkVariable.get() == 1:
            root.wm_attributes("-topmost", 1)
        elif checkVariable.get() == 0:
            root.wm_attributes("-topmost", 0)
    
    def Maximize():
        root.wm_state("zoomed")

    def Restore():
        root.wm_state("normal")

    def Minimize():
        root.wm_state("iconic")
        

    # ENTER SUB MENUS TO MENUBAR (SUB-MENU 2)
    menu3 = Menu(menuBar, tearoff=0)
    menu3.add_checkbutton(label="Always on Top", variable=checkVariable, onvalue=True, offvalue=False, command=AlwaysOnTop)
    menu3.add_separator()
    menu3.add_command(label="Maximize", accelerator="Ctrl+M", command=Maximize)
    menu3.add_command(label="Restore", accelerator="Ctrl+R", command=Restore)
    menu3.add_command(label="Minimize", accelerator="Ctrl+I", command=Minimize)
    
    
    # PACKING SUB MENU 2 INTO MENU BAR
    menuBar.add_cascade(menu=menu3, label="Window")
    
    # -------------------------------------------------------------------------------------------
    
    # METHODS FOR SUB MENU 4
    def Version():
        main = Tk()
        main.overrideredirect(1)
        main.withdraw()
        mbox.showinfo("Build Version", "                          No Updates Available\n\nYou currently have the latest version of Notepad installed\nCurrent Version: 1.0.0")
        main.destroy()
        root.focus_force()

    def Help(event=None):
        main = Tk()
        main.overrideredirect(1)
        main.withdraw()
        mbox.showinfo("Notepad", "                                   > Notepad <\n                            ==>Help Section<==\n\nNotepad has been the fast and simple text editor on Windows for over 30 years. View, edit, and search through plain text documents and source code files instantly. Edit text-based files and source code instantly.\nCustomize your view with lots of options. Make your Python Source Files or Text files here and share them anywhere.\n\nAuthor:                      Syed Muhammad Sameer Nasir\nInitial release:           September 2021\nOperating System:    Microsoft Windows, macOS, Linux\n\n                               Keyboard Shortcuts\n                           Ctrl+A        Select All\n                           Ctrl+C        Copy\n                           Ctrl+F         Find\n                           Ctrl+I         Minimize\n                           Ctrl+G        Find and Replace\n                           Ctrl+M       Maximize\n                           Ctrl+O       Open File\n                           Ctrl+Q       Clear All Text\n                           Ctrl+R        Restore Window\n                           Ctrl+S        Save File\n                           Ctrl+T        Insert Date/Time\n                           Ctrl+X        Cut\n                           Ctrl+Y         Redo\n                           Ctrl+Z        Undo\n                           Alt+F4        Close Program (Force)\n                           F1               Open Help Box\n")
        main.destroy()
        root.focus_force()

    root.bind('<F1>', Help)

    def About():
        main = Tk()
        main.overrideredirect(1)
        main.withdraw()
        mbox.showinfo("Notepad", "Notepad by Syed Muhammad Sameer Nasir\nContact: +923009644099")
        main.destroy()
        root.focus_force()
    
    # ENTER SUBMENUS TO MENU (SUB-MENU 3)
    menu4 = Menu(menuBar, tearoff=0)
    menu4.add_command(label="Check For Updates", command=Version)
    menu4.add_command(label="Help", accelerator="F1", command=Help)
    menu4.add_separator()
    menu4.add_command(label="About Notepad", command=About)

    # PACKING SUB MENU 3 INTO MENU BAR
    menuBar.add_cascade(menu=menu4, label="Help")
    
    # -------------------------------------------------------------------------------------------    
    
    root.config(menu=menuBar)
    root.mainloop()






# LOADING SCREEN FUNCTION
def LoadingScreen():
    global win
    win = Tk()

    # -------------------------------------------------------------------------------------------

    # PLACE WINDOWS IN CENTER OF SCREEN
    windows_width = 350
    windows_height = 450
    global screen_width
    global screen_height
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()
    position_x = int((screen_width/2)-(windows_width/2))
    position_y = int((screen_height/2)-(windows_height/2))

    # -------------------------------------------------------------------------------------------

    # LOADING SCREEN GEOMETRY
    win.geometry(f"{windows_width}x{windows_height}+{position_x}+{position_y}")
    win.minsize(windows_width,windows_height)
    win.maxsize(windows_width,windows_height)
    try:
        win.tk.call('wm', 'iconphoto', win._w, PhotoImage(file='icon.png'))
    except Exception:
        pass
    
    # REMOVE THE DEFAULT WINDOWS TITLE BAR
    win.overrideredirect(True)

    # -------------------------------------------------------------------------------------------
    
    # NEW FRAME IN MIDDLE OF LOADING WINDOW
    frame = Frame(win, borderwidth=0)
    frame.place(relx=.5, rely=.4, anchor=CENTER)

    # MAKE A VIDEO PLAYER BOX WITH LABEL
    videoLabel = Label(frame, borderwidth=0)
    videoLabel.pack()

    # VIDEO FILE (.MP4) PATH
    videoPath = cwd + "\\loading.mp4"

    # ADD THE VIDEO TO LABEL AND PLAY IT
    player = tkvideo.tkvideo(videoPath, videoLabel, loop=1, size=(200,200))
    player.play()

    # -------------------------------------------------------------------------------------------

    # OPENING NOTEPAD TEXT
    text = Label(win, text="Opening Notepad", font=("Impact", 18), bg='#ba851c', fg='white')
    text.place(relx=0.5, rely=0.7, anchor=CENTER)

    # -------------------------------------------------------------------------------------------

    # CHANGING BACKGROUND OF LOADING SCREEN
    win.config(bg='#ba851c')

    # -------------------------------------------------------------------------------------------

    # WAIT FOR LOADING, THEN OPEN CALCULATOR
    win.after(5000, Notepad)
    win.mainloop()
    
    
    
    
    
    
# MAIN FUNCTION
if __name__ == "__main__":
    LoadingScreen()