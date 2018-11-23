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
        ##input_user = StringVar()
        input_user = Entry(janela, width=15)
        input_user.pack(side=BOTTOM, fill=X)
        input_field = Label(janela, text="1. Frase A \n2. Frase B \n3. Frase C \n", height=5)
        input_field.pack(side=BOTTOM, fill=X)

        def enter_pressed(event):
            opc=str(input_user.get())
            if(opc=='1'):
                falar="frase 1"
            elif(opc=='2'):
                falar="frase 2"
            elif(opc=='3'):
                falar="frase 3"
            else:
                falar="opc invalida"
            if(falar!="opc invalida"):
                input_get = "Você: " + falar
                chat.insert(END, str(input_get))
                chat.insert(END, "")
                chat.insert(END, "Ariel: Bora sair!")
                chat.itemconfig(END, fg="red")
                chat.insert(END, "")
                ##input_field.delete(0,END)
                ##input_field['text']=""
                input_user.delete(0, END)
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

        chat.insert(END, "Ariel: Olá "+nome+" Turu bom?")
        chat.itemconfig(END, fg="red")
        chat.insert(END, "")

        input_user.bind("<Return>", enter_pressed)
        ##bt=
        frame.pack()

        janela.mainloop()