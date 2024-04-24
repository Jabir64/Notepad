import tkinter as tk
from tkinter import filedialog
window = tk.Tk()
window.geometry("700x700")


text_area = tk.Text(window)
text_area.pack(side=tk.LEFT,fill=tk.BOTH,expand=True)

scroll = tk.Scrollbar(window,command=text_area.yview)
scroll.pack(side=tk.RIGHT,fill=tk.Y)
text_area.config(yscrollcommand=scroll.set)
def open_file():
    file = filedialog.askopenfilename(initialdir="/",title="Select File",filetypes=(("Text Files","*.txt"),("All Files","*.*")))
    if file:
        text_area.delete(1.0,tk.END)
        with open(file, "r") as f:
            text_area.insert("1.0", f.read())
        window.title(file + " - Python Notepad")

def save_file():
    file = filedialog.asksaveasfilename(title="Select File",defaultextension=".txt",filetypes=(("Text Files", "*.txt"), ("All Files", "*.*")))
    if file:
        f = open(file, "w")
        f.write(text_area.get(1.0,tk.END))
def exit():
    window.destroy()

menu_bar = tk.Menu(window)

options = tk.Menu(menu_bar, tearoff=0)
options.add_command(label="New")
options.add_command(label="New Window")
options.add_command(label="Open",command=open_file)
options.add_command(label="Save",command=save_file)
options.add_command(label="Save As")
options.add_separator()
options.add_command(label="Page Setup")
options.add_command(label="Print")
options.add_separator()
options.add_command(label="Exit",command=exit)

options_2 = tk.Menu(menu_bar, tearoff=0)
options_2.add_command(label="Zoom in")
options_2.add_command(label="Zoom out")

menu_bar.add_cascade(label="File",menu=options)
menu_bar.add_cascade(label="Edit",menu=options_2)

window.config(menu=menu_bar)



window.mainloop()

