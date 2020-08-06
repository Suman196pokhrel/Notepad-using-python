from tkinter import *
from PIL import ImageTk,Image
import tkinter.messagebox as tmsg
import tkinter.filedialog as fldg
import os
import threading
import tkinter.font as tkFont


root = Tk()
global b
root.geometry('760x500')
root.configure(bg="white")
root.title("Notepad(Pokhrel_Softwares)")

ac = Image.open("2.png")
img_logo = ImageTk.PhotoImage(ac)
root.iconphoto(False, img_logo)
x = root.winfo_screenwidth()
y = root.winfo_screenheight()

# Variables
var = StringVar()
var_11 = StringVar()


# Tkinter Font
fontStyle = tkFont.Font(family="comic sans ms", size=15)


def find_text():

    top_win = Toplevel()
    top_win.geometry("400x200")
    top_win.maxsize(height=200,width=400)
    top_win.title("Find Text")
    photo = ImageTk.PhotoImage(Image.open("2.png"))
    top_win.iconphoto(False,photo)
    top_win.configure(bg="#00A98A")

    # Required Functions

    def search_text():
        data_entry_text = entry_text.get()
        # print(data_entry_text)
        total_data_text = text_wid.get('1.0','end')
        # print(total_data_text)
        # result_search_text=total_data_text.find(data_entry_text)
        result_search_text = total_data_text.count(data_entry_text)
        label_number_of_text_data.configure(text=result_search_text)





    # Labels and Required Widgets for tpo_win Window

    label_text = Label(top_win,text="Enter The Text :: ")
    entry_text = Entry(top_win)
    label_number_of_text = Label(top_win, text="Number Of Searched Item :: ")
    label_number_of_text_data=Label(top_win,text="")
    btn_1 = Button(top_win,text="Search",command=search_text)

    # Packing All elements

    label_text.grid(row=0,column=0,pady=5)
    entry_text.grid(row=0,column=1)
    btn_1.grid(row=0,column=2,padx=5)
    label_number_of_text.grid(row=1,column=0,pady=5,padx=5)
    label_number_of_text_data.grid(row=1,column=1)


def replace_text():
    top_win = Toplevel()
    top_win.geometry("400x200")
    # top_win.maxsize(height=200, width=400)
    top_win.title("Find Text")
    photo = ImageTk.PhotoImage(Image.open("2.png"))
    top_win.iconphoto(False, photo)
    top_win.configure(bg="#00A98A")

    # Required Functions

    def search_text():
        data_entry_text = entry_text.get()
        # print(data_entry_text)
        total_data_text = text_wid.get('1.0', 'end')
        # print(total_data_text)
        # result_search_text=total_data_text.find(data_entry_text)
        result_search_text = total_data_text.count(data_entry_text)
        label_number_of_text_data.configure(text=result_search_text)

    def search_and_replace_text():
        data_entry_text = entry_text.get()
        # print(data_entry_text)
        total_data_text = text_wid.get('1.0', 'end')
        # print(total_data_text)
        new_text = label_replace_entry.get()
        # result_search_text=total_data_text.find(data_entry_text)
        replaced_data = total_data_text.replace(data_entry_text,new_text)
        text_wid.delete('1.0',END)
        text_wid.insert(INSERT,replaced_data)




    # Labels and Required Widgets for tpo_win Window

    label_text = Label(top_win, text="Enter The Text You wanna search First :: ")
    entry_text = Entry(top_win)
    label_number_of_text = Label(top_win, text="Number Of Searched Item :: ")
    label_number_of_text_data = Label(top_win, text="")
    btn_1 = Button(top_win, text="Search", command=search_text)
    label_replace = Label(top_win,text="Replace With ::")
    label_replace_entry = Entry(top_win)
    btn2 = Button(top_win,text="Replace",command = search_and_replace_text)

    # Packing All elements

    label_text.grid(row=0, column=0, pady=5,padx=2)
    entry_text.grid(row=0, column=1)
    btn_1.grid(row=0, column=2, padx=5)
    label_number_of_text.grid(row=1, column=0, pady=5, padx=5)
    label_number_of_text_data.grid(row=1, column=1)
    label_replace.grid(row=2,column=0)
    label_replace_entry.grid(row=2,column=1)
    btn2.grid(row=2,column=2)


def default_theme():
    text_wid.configure(bg="white", fg="black")
    File_menu.configure(bg="white", fg="black")
    Edit_menu.configure(bg="white", fg="black")
    view_menu.configure(bg="white", fg="black")
    help_menu.configure(bg="white", fg="black")
    Format_menu.configure(bg="white", fg="black")
    Zoom_menu.configure(bg="white", fg="black")


def clear_all():
    text_wid.delete('1.0',END)


def zoomin_1():
    fontsize=fontStyle['size']
    fontStyle.configure(size=fontsize+5)


def zoomout_1():
    fontsize = fontStyle['size']
    fontStyle.configure(size=fontsize - 5)


def default_1():
    fontStyle.configure(size=10)


def dark_mode():
    text_wid.configure(bg="#233357",fg="#F29B18")
    File_menu.configure(bg="#233357",fg="white")
    Edit_menu.configure(bg="#233357", fg="white")
    view_menu.configure(bg="#233357", fg="white")
    help_menu.configure(bg="#233357", fg="white")
    Format_menu.configure(bg="#233357", fg="white")
    Zoom_menu.configure(bg="#233357", fg="white")


def print_1():
    tmsg.showinfo("Printing Your Document","Sorry, It seems that your System is not connected \nto any kind of Printing Device.\nTry Again by Connecting a printer.")


def open_1():
    my_program = fldg.askopenfilename()
    #Opens the program
    os.system('"%s"'%my_program)


def save_1():
    f= fldg.asksaveasfile(mode = 'w',filetypes=(('All Files', '*.*'),('Python Files', '*.py'), ('Text Document', '*.txt')),defaultextension =".txt")
    f.write(text_wid.get("1.0", "end-1c"))
    f.close()


def exit_1():
    root.quit()


def test_fun():
    print("IT's Working")


def v_help():
    tmsg.showinfo("Help","Please visit out webiste\n www.notepad@suman.com")


def feedback():
    a = tmsg.askquestion("FeedBack","Was our Software Convinient for use?")
    if a == "yes" or a == "no":
        tmsg.showinfo("FeedBack","Your FeedBack is valuable,Thanks for helping")


def helpp():
    tmsg.showinfo("Descritpion","Microsoft introduced Multi-Tool Notepad,\n "
                                "a mouse-based text editor written by Richard\n "
                                "Brodie, with the $195 Microsoft Mouse in May 1983 \n"
                                "at the Spring COMDEX computer expo in Atlanta. Also \n"
                                "introduced at that COMDEX was Multi-Tool Word, designed\n"
                                " by Charles Simonyi to work with the mouse.[1][2][3] Most \n"
                                "watching Simonyi's demonstration had never heard of a mouse\n"
                                " Microsoft released the Microsoft Mouse in June 1983, and the\n "
                                "boxed mouse and Multi-Tool Notepad began shipping in July.\n")


def update(event):
    var.set(str(len(text_wid.get("1.0", "end-1c"))))


thread_open = threading.Thread(target=open_1, daemon=True)
thread_save = threading.Thread(target=save_1, daemon=True)


mainmenu = Menu(root)
File_menu = Menu(mainmenu, tearoff = False)
File_menu.add_command(label="Open", command= thread_open.start)
File_menu.add_command(label="Save As", command= save_1)
File_menu.add_command(label="Print", command= print_1)
File_menu.add_command(label="Exit", command=exit_1)
root.config(menu = mainmenu)

mainmenu.add_cascade(label="File", menu = File_menu)


Edit_menu = Menu(mainmenu, tearoff = False)
Edit_menu.add_command(label="Clear All", command= clear_all)
Edit_menu.add_command(label="Find Number of text", command= find_text)
Edit_menu.add_command(label="Replace text", command= replace_text)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="Edit", menu=Edit_menu)


Format_menu = Menu(mainmenu, tearoff = False)
Format_menu.add_command(label="Default Theme", command= default_theme)
Format_menu.add_command(label="Dark Theme", command= dark_mode)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="Format", menu=Format_menu)


view_menu = Menu(mainmenu,tearoff = False)
Zoom_menu = Menu(view_menu,tearoff=False)
Zoom_menu.add_command(label="Zoom In",command =zoomin_1)
Zoom_menu.add_command(label="Zoom Out",command =zoomout_1)
Zoom_menu.add_command(label="Restore To Default",command =default_1)
view_menu.add_cascade(label="Zoom",menu=Zoom_menu)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="View",menu=view_menu)

help_menu = Menu(mainmenu,tearoff = False)
help_menu.add_command(label="View Help",command= v_help)
help_menu.add_command(label="Send Feedback",command= feedback)
help_menu.add_command(label="About Notepad",command= helpp)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="Help",menu=help_menu)


# Bottom Area where the Info's are gonna be Shown
bottom_bar = Frame(root, bg = "#2C3539")
bottom_bar.pack(side=BOTTOM,expand=True,fill=BOTH)

bottom_bar_content = Label(bottom_bar,text = f"Number Of Characters :: ",bg="#9118C4",height=1,
                           font=("comic sans ms", 10, "italic"),fg="black")
bottom_bar_content.pack(side=LEFT,expand=False,anchor="n")

bottom_bar_content_1 = Label(bottom_bar,textvariable=var,bg="#9118C4",height=1,
                           font=("comic sans ms", 10, "italic"),fg="black")
bottom_bar_content_1.pack(side=LEFT,expand=False,anchor="n")

# Scroll_Bar widget
scrollbar_x = Scrollbar(root, orient=HORIZONTAL)
scrollbar_x.pack(side=BOTTOM,fill=X)


scrollbar_y = Scrollbar(root)
scrollbar_y.pack(side=RIGHT,fill=Y)


# Central Area where the Text will be typed
text_wid = Text(root,wrap=NONE,bg="white",borderwidth = 5,relief = "sunken",font=fontStyle,height = 37,yscrollcommand=scrollbar_y.set,xscrollcommand=scrollbar_x.set)
text_wid.pack(fill=X,expand=True)


# Linking the scrollbars
scrollbar_y.config(command=text_wid.yview)
scrollbar_x.config(command=text_wid.xview)

text_wid.bind('<KeyRelease>',update)


root.mainloop()
