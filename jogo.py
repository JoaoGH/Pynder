from GlobalVariable import GlobalVariable
from tkinter import *
from time import *
import random
class jogo():
    def __init__(self, jogada, pont):
        super().__init__()
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
                        texto = "1. Sim, sempre saio, com meus amigos e amigas. \n 2. As vezes, um espécie de equilíbrio entre ficar em casa e sair. \n 3. Quase nunca sou antissocial."
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
                        texto = "1. Sim, sempre saio, com meus amigos e amigas. \n 2. As vezes, um espécie de equilíbrio entre ficar em casa e sair. \n 3. Quase nunca, sou antissocial."
                        input_field['text']=texto
                        chat.yview('end')
            elif(self.jogada==3):
                opc=str(input_user.get())
                if(opc=='1'):
                    tu="Sim, sempre saio, com meus amigos e amigas."
                    ela="nossa baladero, vai meter o loko, kkkk brinks"
                    self.pont=self.pont +1
                elif(opc=='2'):
                    tu="As vezes, um espécie de equilíbrio entre ficar em casa e sair. "
                    ela="Eu também"
                    self.pont=self.pont+2
                elif(opc=='3'):
                    tu="Quase nunca, sou antissocial."
                    ela="Bem, quase nunca não é nunca"
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
                    texto = "1. Mora onde? \n 2. Onde vosmecê reside? \n 3. Qual sua esquina? E quanto o programa?"
                    input_field['text']=texto
                    chat.yview('end')
            elif(self.jogada==4):
                opc=str(input_user.get())
                if(opc=='1'):
                    tu="Mora onde?"
                    ela="Vi aqui, é uns 3 km de você está."
                    self.pont=self.pont +1
                elif(opc=='2'):
                    tu="Onde vosmecê reside?"
                    ela="F O R M A L I D A D E, uns 3 km daí"
                    self.pont=self.pont+2
                elif(opc=='3'):
                    tu="Qual sua esquina? E quanto o programa?"
                    ela="KKKKKJ Block"
                else:
                    tu="Opção Inválida"
                if(tu!="opc invalida"):
                    if(ela=="KKKKKJ Block"):
                        exit()
                    ela1="Você trabalha com o que?"
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
                    texto = "1. Sou T.I. :( \n2. Trabalho na V.A.S.P.\n3. Sou cafetão, quer emprego?"
                    input_field['text']=texto
                    chat.yview('end')
            elif(self.jogada==5):
                opc=str(input_user.get())
                if(opc=='1'):
                    tu="Sou T.I. :("
                    ela="kkk, formatar meu pc? kkk Brinks"
                    self.pont=self.pont +1
                elif(opc=='2'):
                    tu="Trabalho na V.A.S.P."
                    ela="Sério, mds…"
                elif(opc=='3'):
                    tu="Sou cafetão, quer emprego?"
                    ela="¬¬ babaquinha."
                else:
                    tu="Opção Inválida"
                if(tu!="opc invalida"):
                    if(ela=="¬¬ babaquinha."):
                        exit()
                    ela1="Sou enfermeira"
                    input_get = "Você: " + tu
                    chat.insert(END, str(input_get))
                    chat.insert(END, "")
                    chat.insert(END, "Ariel: " + ela)
                    chat.itemconfig(END, fg="red")
                    chat.insert(END, "")
                    chat.insert(END,"Você: E você trabalha com algo?")
                    chat.insert(END, "")
                    chat.insert(END, "Ariel: "+ela1)
                    chat.itemconfig(END, fg="red")
                    chat.insert(END, "")
                    input_user.delete(0, END)
                    texto = "1. Bah tranzar com uma enfermeira deve ser foda bagari\n2. Supinpa"
                    input_field['text']=texto
                    chat.yview('end')
            elif(self.jogada==6):
                opc=str(input_user.get())
                if(opc=='1'):
                    tu="Bah tranzar com uma enfermeira deve ser foda bagari"
                    ela="Tem suas vantagens"
                elif(opc=='2'):
                    tu="Supinpa"
                    ela="Eu assisto GOT, você olha alguma série?"
                else:
                    tu="Opção Inválida"
                if(tu!="opc invalida"):
                    if(ela=="Tem suas vantagens"):
                        exit()
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
                    texto = "1. Só novela da record\n2. Assisto Bojack\n3. Não tenho tempo para isso"
                    input_field['text']=texto
                    chat.yview('end')
            elif(self.jogada==7):
                opc=str(input_user.get())
                if(opc=='1'):
                    tu="Só novela da record"
                elif(opc=='2'):
                    tu="Assisto Bojack"
                    self.pont=self.pont +1
                elif(opc=='3'):
                    tu="Não tenho tempo para isso"
                    self.pont=self.pont -1
                else:
                    tu="Opção Inválida"
                if(tu!="Opção Inválida"):
                    ela="Faço o melhor miojo do mundo"
                    input_get = "Você: " + tu
                    chat.insert(END, str(input_get))
                    chat.insert(END, "Você cozinha?")
                    chat.insert(END, "")
                    chat.insert(END, "Ariel: " + ela)
                    chat.itemconfig(END, fg="red")
                    chat.insert(END, ela1)
                    chat.itemconfig(END, fg="red")
                    chat.insert(END, ela2)
                    chat.itemconfig(END, fg="red")
                    chat.insert(END, "")
                    input_user.delete(0, END)
                    texto = "1. Poderia fazer 1 pra mim?\n2. Nissin é vida\n3. Nossa, nem segue o mulher recatada e do lar."
                    input_field['text']=texto
                    chat.yview('end')
            elif(self.jogada==8):
                opc=str(input_user.get())
                if(opc=='1'):
                    tu="Poderia fazer 1 pra mim?"
                    ela="Só quando a gente sair"
                    self.pont=self.pont +1
                elif(opc=='2'):
                    tu="Nissin é vida"
                    ela="É verdade"
                    self.pont=self.pont +2
                elif(opc=='3'):
                    tu="Nossa, nem segue o mulher recatada e do lar."
                    ela="Claro q nao, isso é frescura."
                    self.pont=self.pont -2
                else:
                    tu="Opção Inválida"
                if(tu!="Opção Inválida"):
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
                    texto = "1. Eu costumo malhar bastante, e você?\n2. Você pratica esportes?"
                    input_field['text']=texto
                    chat.yview('end')
            elif(self.jogada==9):
                opc=str(input_user.get())
                if(opc=='1'):
                    tu="Eu costumo malhar bastante, e você?"
                    ela="kk gado d++"
                    self.pont=self.pont -1
                elif(opc=='2'):
                    tu="Você pratica esportes?"
                    ela="Sim, faço ginástica"
                    self.pont=self.pont +1
                else:
                    tu="Opção Inválida"
                if(tu!="Opção Inválida"):
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
                    texto = "1. Então você deve estar em boa forma para ir\n onde eu estava pensando, vamos caminhar na praia?\n2 Nice job"
                    input_field['text']=texto
                    chat.yview('end')
            elif(self.jogada==10):
                sair=""
                opc=str(input_user.get())
                if(self.pont>9):
                        chance=random.randrange(1, 100)
                        if(chance>15):
                            sair="gg"
                        elif(self.pont>5):
                            chance=random.randrange(1, 50)
                            if(chance>15):
                                sair="gg"
                        else:
                            chance=random.randrange(1, 20)
                            if(chance>15):
                                sair="gg"
                if(opc=='1'):
                    tu="Então você deve estar em boa forma para ir onde eu estava pensando,"
                    tu2="vamos caminhar na praia?"
                    if(sair=="gg"):
                        ela="Me pega as 19h no seguinte endereço"
                        ela1="Rua dos Bobos, nº 0"
                        texto="Você conseguiu sair com Ariel."
                    else:
                        ela="Não"
                        ela1="Tchau"
                        texto="Você não conseguiu sair com Ariel."
                elif(opc=='2'):
                    tu="Nice job"
                    tu2=""
                    if(sair=="gg"):
                        ela="Já que você nao me convidou para sair eu faço isso."
                        ela1="Vamos sair pra comer algo?"
                        ela2="Sim"
                        texto="Você conseguiu sair com Ariel."
                    else:
                        ela="vou indo então,"
                        ela1="tchau"
                        texto="Você não conseguiu sair com Ariel."
                else:
                    tu="Opção Inválida"
                if(tu!="Opção Inválida"):
                    input_get = "Você: " + tu
                    chat.insert(END, str(input_get))
                    chat.insert(END, tu2)
                    chat.insert(END, "Ariel: " + ela)
                    chat.itemconfig(END, fg="red")
                    chat.insert(END, ela1)
                    chat.itemconfig(END, fg="red")
                    chat.insert(END, "")
                    chat.insert(END, "Você: "+ela2)
                    chat.insert(END, "")
                    input_user.delete(0, END)
                    input_field['text']=texto
                    chat.yview('end')
            self.jogada=self.jogada+1
            print(self.pont)
            return "break"

        frame = Frame(janela, width=400, height=700)
        frame.pack_propagate(False)  # prevent frame to resize to the labels size

        scrollbar = Scrollbar(frame)
        scrollbar.pack(side=RIGHT, fill=Y)
        chat = Listbox(frame, yscrollcommand=scrollbar.set, selectmode=EXTENDED)
        scrollbar.config(command=chat.yview)
        scrollbar.pack(side=RIGHT, fill=Y)
        chat.pack(side=LEFT, fill=BOTH, expand=1)

        chat.insert(END, "Ariel: Olá! Turu bom?")
        chat.itemconfig(END, fg="red")
        chat.insert(END, "")
        input_user.bind("<Return>", enter_pressed)
        frame.pack()

        janela.mainloop()