from GlobalVariable import GlobalVariable
from tkinter import *
class fase1():
    def __init__(self, nome):
        janela = Tk()
        janela.title("Pynder")
        janela.geometry("400x700")
        texto = "Olá "+nome+ ", Tqqquru bom?"
        Label(janela, text=texto).place(x=100,y=100)
        janela.mainloop()
