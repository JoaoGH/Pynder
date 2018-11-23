from tkinter import *

janela = Tk()
janela.title("Pynder")
janela.geometry("400x700")
##input_user = StringVar()
input_field = Label(janela, text="1. Frase A abcdefghijklmnopqrstuvwxyz abcdefghijklmnopqrstuvwxyz \n2. Frase B abcdefghijklmnopqrstuvwxyz abcdefghijklmnopqrstuvwxyz \n3. Frase C abcdefghijklmnopqrstuvwxyz abcdefghijklmnopqrstuvwxyz\n", height=5)
input_field.pack(side=BOTTOM, fill=X)


def enter_pressed(event):
    input_get = "Você: "+input_field['text']
    chat.insert(END, str(input_get))
    chat.insert(END, "")

    chat.insert(END, "Ariane: Let's go fuck!")
    chat.itemconfig(END, fg="red")
    chat.insert(END, "")
    ##input_user.set('')
    chat.yview('end')
    return "break"

frame = Frame(janela, width=400, height=700)
frame.pack_propagate(False) # prevent frame to resize to the labels size

scrollbar = Scrollbar(frame)
scrollbar.pack(side=RIGHT, fill=Y)
chat = Listbox(frame, yscrollcommand=scrollbar.set, selectmode=EXTENDED)
scrollbar.config(command=chat.yview)
scrollbar.pack(side=RIGHT, fill=Y)
chat.pack(side=LEFT, fill=BOTH, expand=1)
for i in range(30):
    chat.insert(END, "Ariane: Olá, Turu bom?")
    chat.itemconfig(END, fg="red")
    chat.insert(END, "")

input_field.bind("<Return>", enter_pressed)
frame.pack()

janela.mainloop()