from GlobalVariable import GlobalVariable
from tkinter import *
class jogo():
    def __init__(self, nome):
        # janela = Tk()
        # janela.title("Pynder")
        # janela.geometry("400x700")
        # texto = "Olá "+nome+ ", Turu bom?"
        # Label(janela, text=texto).place(x=100,y=100)
        # janela.mainloop()
        janela = Tk()
        janela.title("Pynder")
        janela.geometry("400x700")
        input_user = StringVar()
        input_field = Entry(janela, text=input_user)
        input_field.pack(side=BOTTOM, fill=X)

        def enter_pressed(event):
            input_get = "Você: " + input_field.get()
            chat.insert(END, str(input_get))
            chat.insert(END, "")
            chat.insert(END, "Ariane: Bora fuder!")
            chat.itemconfig(END, fg="red")
            chat.insert(END, "")
            input_field.delete(0,END)
            chat.yview('end')
            return "break"

        frame = Frame(janela, width=400, height=700)
        frame.pack_propagate(False)  # prevent frame to resize to the labels size

        scrollbar = Scrollbar(frame)
        scrollbar.pack(side=RIGHT, fill=Y)
        chat = Listbox(frame, yscrollcommand=scrollbar.set, selectmode=EXTENDED)
        scrollbar.config(command=chat.yview)
        scrollbar.pack(side=RIGHT, fill=Y)
        chat.pack(side=LEFT, fill=BOTH, expand=1)

        chat.insert(END, "Ariane: Olá "+nome+" Turu bom?")
        chat.itemconfig(END, fg="red")
        chat.insert(END, "")

        input_field.bind("<Return>", enter_pressed)
        frame.pack()

        janela.mainloop()