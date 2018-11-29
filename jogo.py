from GlobalVariable import GlobalVariable
from tkinter import *
from time import *
class jogo():
    def __init__(self, nome, jogada, pont):
        self.jogada=jogada
        self.pont=pont
        janela = Tk()
        janela.title("Pynder")
        janela.geometry("400x700")
        input_user = Entry(janela, width=15)
        input_user.pack(side=BOTTOM, fill=X)
        input_field = Label(janela, text="1. Olá, tudo e contigo? \n2. Suavo e tu? \n3. Melhor agora gostosa kkj \n", height=5)
        input_field.pack(side=BOTTOM, fill=X)

        def enter_pressed(event):
            ela=""
            ela1=""
            ela2=""
            if(self.jogada==0):
                opc=str(input_user.get())
                if(opc=='1'):
                    tu="Olá, tudo e contigo?"
                    ela="Bom, vi você aqui no Pynder e te achei"
                    ela1="interessante, vamos conversar um pouco?"
                    self.pont=self.pont +1
                elif(opc=='2'):
                    tu="Suavo e tu?"
                    ela="kkkkj, to muito bem, você é engraçado,"
                    ela1="vi você aqui no Pynder e te achei interessante,"
                    ela2="vamos conversar um pouco"
                    self.pont=self.pont+2
                elif(opc=='3'):
                    tu="Melhor agora gostosa kkj"
                    ela="Nossa tinha visto você achei que seria"
                    ela1="legal conversar, estava errada"
                    self.pont = self.pont-2
                else:
                    tu="Opção Inválida"
                if(tu!="opc invalida"):
                    input_get = "Você: " + tu
                    chat.insert(END, str(input_get))
                    chat.insert(END, "")
                    chat.insert(END, "Ariel: " + ela)
                    chat.itemconfig(END, fg="red")
                    chat.insert(END, ela1)
                    chat.itemconfig(END, fg="red")
                    chat.insert(END, ela2)
                    chat.itemconfig(END, fg="red")
                    chat.insert(END, "")
                    print(self.pont)
                    texto="1. Você gosta de música? Qual gênero?\n 2. Quais seus hobbies?\n 3. Manda nudes kkj"
                    input_user.delete(0, END)
                    input_field['text']=texto
                    chat.yview('end')
            elif(self.jogada==1):
                opc=str(input_user.get())
                if(opc=='1'):
                    tu="Você gosta de música? Qual gênero?"
                    ela="Adoro, toco piano e curto todos os gêneros. E você?"
                    self.pont=self.pont +1
                elif(opc=='2'):
                    tu="Quais seus hobbies?"
                    ela="Eu toco piano, pinto quadros e faço yoga. E você?"
                    self.pont=self.pont+1
                elif(opc=='3'):
                    tu="Manda nudes kkj"
                    ela="Você foi bloqueado"
                else:
                    tu="Opção Inválida"
                if(tu!="opc invalida"):
                    input_get = "Você: " + tu
                    chat.insert(END, str(input_get))
                    chat.insert(END, "")
                    chat.insert(END, "Ariel: " + ela)
                    chat.itemconfig(END, fg="red")
                    chat.insert(END, ela1)
                    chat.itemconfig(END, fg="red")
                    chat.insert(END, ela2)
                    chat.itemconfig(END, fg="red")
                    chat.insert(END, "")
                    if(ela=="Você foi bloqueado"):
                        sleep(3)
                        exit(0)
                    elif(ela=="Adoro, toco piano e curto todos os gêneros. E você?"):
                        texto="1. Nossa que legal, acho foda quem toca piano\n 2. Não curto música\n 3. Um ou dois gêneros"
                    else:
                        texto="1.Faço corrida\n 2. Ando de bicicleta\n 3. Que massa! Eu faço apenas artesanato"
                    input_user.delete(0, END)
                    input_field['text']=texto
                    chat.yview('end')
            elif(self.jogada==2):
                if(ela=="Adoro, toco piano e curto todos os gêneros. E você?"):
                    opc=str(input_user.get())
                    if(opc=='1'):
                        tu="Nossa que legal, acho foda quem toca piano"
                        ela="Nice"
                        ela1="Você costuma sair para ir em festas?"
                        self.pont=self.pont +2
                    elif(opc=='2'):
                        tu="Não curto música"
                        ela="Nice"
                        ela1="Você costuma sair para ir em festas?"
                        self.pont=self.pont-1
                    elif(opc=='3'):
                        tu="Um ou dois gêneros"
                        ela="Nice"
                        ela1="Você costuma sair para ir em festas?"
                    else:
                        tu="Opção Inválida"
                    if(tu!="opc invalida"):
                        input_get = "Você: " + tu
                        chat.insert(END, str(input_get))
                        chat.insert(END, "")
                        chat.insert(END, "Ariel: " + ela)
                        chat.itemconfig(END, fg="red")
                        chat.insert(END, ela1)
                        chat.itemconfig(END, fg="red")
                        chat.insert(END, ela2)
                        chat.itemconfig(END, fg="red")
                        chat.insert(END, "")
                        input_user.delete(0, END)
                        input_field['text']=texto
                        chat.yview('end')
                else:
                    opc=str(input_user.get())
                    if(opc=='1'):
                        tu="Faço corrida"
                        ela="Nice"
                        ela1="Você costuma sair para ir em festas?"
                    elif(opc=='2'):
                        tu="Ando de bicicleta"
                        ela="Nice"
                        ela1="Você costuma sair para ir em festas?"
                    elif(opc=='3'):
                        tu="Que massa! Eu faço apenas artesanato"
                        ela="Nice"
                        ela1="Você costuma sair para ir em festas?"
                        self.pont=self.pont+1
                    else:
                        tu="Opção Inválida"
                    if(tu!="opc invalida"):
                        input_get = "Você: " + tu
                        chat.insert(END, str(input_get))
                        chat.insert(END, "")
                        chat.insert(END, "Ariel: " + ela)
                        chat.itemconfig(END, fg="red")
                        chat.insert(END, ela1)
                        chat.itemconfig(END, fg="red")
                        chat.insert(END, ela2)
                        chat.itemconfig(END, fg="red")
                        chat.insert(END, "")
                        input_user.delete(0, END)
                        input_field['text']=texto
                        chat.yview('end')
            self.jogada=self.jogada+1
            return "break"

        frame = Frame(janela, width=400, height=700)
        frame.pack_propagate(False)  # prevent frame to resize to the labels size

        scrollbar = Scrollbar(frame)
        scrollbar.pack(side=RIGHT, fill=Y)
        chat = Listbox(frame, yscrollcommand=scrollbar.set, selectmode=EXTENDED)
        scrollbar.config(command=chat.yview)
        scrollbar.pack(side=RIGHT, fill=Y)
        chat.pack(side=LEFT, fill=BOTH, expand=1)

        chat.insert(END, "Ariel: Olá "+self.nome+" Turu bom?")
        chat.itemconfig(END, fg="red")
        chat.insert(END, "")
        input_user.bind("<Return>", enter_pressed)
        ##bt=
        frame.pack()

        janela.mainloop()