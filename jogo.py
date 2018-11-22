from GlobalVariable import GlobalVariable
from tkinter import *
import pyttsx3
class jogo():
    def __init__(self, nome):
        en = pyttsx3.init()
        janela = Tk()
        janela.title("Pynder")
        janela.geometry("400x700")
        texto = "Olá "+nome+ ", Turu bom?"
        Label(janela, text=texto).place(x=100,y=100)
        en.say(texto)
        janela.mainloop()
        en.runAndWait()
