import tkinter as tk


root=tk.Tk()
root.geometry('400x400')
root.title("Sistema de Restaurante")

menu=tk.Menu(root, tearoff=False,
             font=('Bold', 12),
             activeborderwidth='10')
menu.add_command(label='Opciones')
menu.add_separator()
menu.add_command(label='')

def popup_menu(e):
    print(e.x_root, e.y_root)

    menu.tk_popup(x=e.x_root, y=e.y_root)

root.bind("<Button-3>", popup_menu)

root.mainloop()
