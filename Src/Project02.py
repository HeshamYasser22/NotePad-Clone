from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from os import system
File = 0

def DarkMode():
    MainWindow.configure(bg='black')
    TxtBox.configure(bg='black' , fg= 'white')
    Toolbar.configure(bg='black' , fg= 'white')
    FileMenu.configure(bg='black' , fg= 'white')
    EditMenu.configure(bg='black' , fg= 'white')
    ViewMenu.configure(bg='black' , fg= 'white')
    HelpMenu.configure(bg='black' , fg= 'white')
    ZoomMenu.configure(bg='black' , fg= 'white')
    ModeMenu.configure(bg='black' , fg= 'white')



def LightMode():
    MainWindow.configure(bg='white')
    TxtBox.configure(fg='black' , bg= 'white')
    Toolbar.configure(fg='black' , bg= 'white')
    FileMenu.configure(fg='black' , bg= 'white')
    EditMenu.configure(fg='black' , bg= 'white')
    ViewMenu.configure(fg='black' , bg= 'white')
    HelpMenu.configure(fg='black' , bg= 'white')
    ZoomMenu.configure(fg='black' , bg= 'white')
    ModeMenu.configure(fg='black' , bg= 'white')

def OpenFile (x):
    global File
    Return = filedialog.askopenfilename(initialdir=r'G:\Work and College\IMT LINUX\Embedded Linux\Python\Lec8' , title='OpenFile' ,filetypes=(('Text' , '*.txt') , ('Allfiles' , '*.*')) )
    File = open(Return , 'r+')
    TxtBox.insert(INSERT,File.read())
    MainWindow.title(f'{File.name.split("/")[-1].strip(".txt")} - Notepad')
    
def ExitFile(x):
    Choice = messagebox.askyesno('Exit!' , 'Sure to Exit?')
    if Choice == 1:
        MainWindow.quit()
    else :
        pass

def SaveAsfile(x):
    global File
    Return = filedialog.asksaveasfilename(defaultextension='.txt' ,  initialdir=r'G:\Work and College\IMT LINUX\Embedded Linux\Python\Lec8' , title='Save as File' ,filetypes=(('Text' , '*.txt') , ('Allfiles' , '*.*')) )   
    File = open(Return , 'w+')
    File.write(TxtBox.get(1.0 , END))
    File.flush()
    MainWindow.title(f'{File.name.split("/")[-1].strip(".txt")} - Notepad')


def NewFile(x):
    global File
    if TxtBox.get(1.0 , END)!='\n':
        SaveMessage = Toplevel()
        SaveMessage.title('Notepad')
        SaveMessage.geometry('+300+300')
        SaveMessage.resizable(False , False)
        SaveMessage.attributes('-toolwindow' , True)
        lbl_Ask = Label(SaveMessage , text= 'Do you want to save changes ?' , pady=20)
        btn_Save = Button(SaveMessage , text='Save' , command=lambda:[SaveMessage.destroy(),SaveAsfile() , TxtBox.delete(1.0 , END)] , padx=20 , pady=10)
        btn_DSave = Button(SaveMessage , text='Don\'t Save' , command=lambda:[SaveMessage.destroy() , TxtBox.delete(1.0 , END) ] , padx=20 , pady=10)
        btn_Cancel = Button(SaveMessage , text='Cancel' , command = SaveMessage.destroy ,padx=20 , pady=10)
        lbl_Ask.grid(row=0 , column= 0 , columnspan= 3)
        btn_Save.grid(row=2 , column=0)
        btn_DSave.grid(row=2 , column= 1)
        btn_Cancel.grid(row=2 , column=2)
        MainWindow.title('Untitled - Notepad')
        File = 0

def NewWindow (x):
    system('Project02.exe')

def Savefile (x):
    global File
    if File == 0:
        SaveAsfile(0)
    else :
        File.seek(0)
        File.truncate()
        File.write(TxtBox.get(1.0 , END))
        File.flush()
        MainWindow.title(f'{File.name.split("/")[-1].strip(".txt")} - Notepad')

def ChangeTitle(x):
    global File
    if File ==0:
        MainWindow.title('Untitled* - Notepad')
    else:
        MainWindow.title(f'{File.name.split("/")[-1].strip(".txt")}* - Notepad')

MainWindow = Tk()
MainWindow.geometry(f'400x400+{int(MainWindow.winfo_screenwidth()/2)-200}+{int(MainWindow.winfo_screenheight()/2)-200}')
MainWindow.title ('Untitled - NotePad')
MainWindow.iconbitmap (r'G:\Work and College\IMT LINUX\Embedded Linux\Python\Project3\notepad.ico')
TxtBox = Text(undo=True )
Toolbar = Menu(MainWindow)
FileMenu = Menu(Toolbar , tearoff=False)
EditMenu = Menu(Toolbar, tearoff=False)
ViewMenu = Menu(Toolbar, tearoff=False)
HelpMenu = Menu(Toolbar , tearoff=False)
ZoomMenu = Menu(ViewMenu , tearoff=False)
ModeMenu = Menu(ViewMenu , tearoff=False)
FileMenu.add_command(label='New' , command=lambda:NewFile(0) , accelerator='Ctrl+N')
FileMenu.add_command(label='New Window' , command=lambda:NewWindow(0) ,accelerator='Ctrl+Shift+N')
FileMenu.add_command(label='Open' , command=lambda:OpenFile(0) , accelerator='Ctrl+O')
FileMenu.add_command(label='Save' , command=lambda:Savefile(0) , accelerator='Ctrl+S')
FileMenu.add_command(label='Save As' , command=lambda:SaveAsfile(0) , accelerator='Ctrl+Shift+S')
FileMenu.add_command(label='Exit' , command=lambda:ExitFile(0) , accelerator='Ctrl+Q')
EditMenu.add_command(label='Undo',accelerator='Ctrl+Z' )
EditMenu.add_command(label='Cut',accelerator='Ctrl+X' )
EditMenu.add_command(label='Copy' ,accelerator='Ctrl+C')
EditMenu.add_command(label='Paste' ,accelerator='Ctrl+V')
EditMenu.add_command(label='Delete' ,accelerator='Del')
EditMenu.add_command(label='Search with Bing…' ,accelerator='Ctrl+E')
EditMenu.add_command(label='Find…' ,accelerator='Ctrl+F')
EditMenu.add_command(label='Find Next',accelerator='F3' )
EditMenu.add_command(label='Find Previous',accelerator='Shift+F3' )
EditMenu.add_command(label='Replace' ,accelerator='Ctrl+H')
EditMenu.add_command(label='Go To..' ,accelerator='Ctrl+G')
EditMenu.add_command(label='Select All',accelerator='Ctrl+A' )
EditMenu.add_command(label='Time/Data',accelerator='F5' )
ZoomMenu.add_command(label='Zoom in')
ZoomMenu.add_command(label='Zoom Out')
ModeMenu.add_command(label='Dark mode' , command= DarkMode)
ModeMenu.add_command(label='Light mode' , command= LightMode)
ViewMenu.add_cascade(label = 'Zoom' , menu=ZoomMenu)
ViewMenu.add_command(label='Status Bar')
ViewMenu.add_cascade(label='Mode' , menu=ModeMenu)
HelpMenu.add_command(label='View Help')
HelpMenu.add_command(label='Send Feedback')
HelpMenu.add_command(label='About Notepad')

Toolbar.add_cascade(label="File" , menu=FileMenu)
Toolbar.add_cascade(label='Edit' , menu= EditMenu)
Toolbar.add_cascade(label='View' , menu= ViewMenu)
Toolbar.add_cascade(label='Help' , menu= HelpMenu)
MainWindow.config(menu=Toolbar)
TxtBox.place(x=0 , y= 0 , relheight=1 , relwidth= 1)
MainWindow.bind('<Control-n>' ,NewFile)
MainWindow.bind('<Control-N>' ,NewFile)
MainWindow.bind('<Control-Shift-N>' ,NewWindow)
MainWindow.bind('<Control-o>' ,OpenFile)
MainWindow.bind('<Control-O>' ,OpenFile)
MainWindow.bind('<Control-q>' ,ExitFile)
MainWindow.bind('<Control-Q>' ,ExitFile)
MainWindow.bind('<Control-S>' ,Savefile)
MainWindow.bind('<Control-s>' ,Savefile)
MainWindow.bind('<Control-Shift-S>' ,SaveAsfile)
MainWindow.bind('<Key>' , ChangeTitle)
MainWindow.minsize(300 , 300)
MainWindow.mainloop()
