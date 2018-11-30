# python 3.7.1
# -*- coding: utf-8 -*-
import random
from tkinter import *
from GlobalVariable import GlobalVariable
from jogo import jogo
import speech_recognition as sr
import pyttsx3

janela = Tk()
janela.title("Pynder")
janela.geometry("400x700")
xx=400
yy=700
fontGrande = ('',30)
fontePequena = ('',15)

def falar():
    engine = pyttsx3.init()
    engine.say("Qual seu nome?")
    microfone = sr.Recognizer()
    with sr.Microphone() as source:
        microfone.adjust_for_ambient_noise(source)
        engine.runAndWait()
        # print("Diga alguma coisa: ")
        audio = microfone.listen(source)
    try:
        frase = microfone.recognize_google(audio,language='pt-BR')
        nome.insert(0,frase)
    except sr.UnknownValueError:
        engine.say("Desculpe! Não consegui te entender")
        engine.runAndWait()

def login():
    g = GlobalVariable("","")
    g.setNome(nome.get())
    # p=random.randrange(1, 4)
    # if(p==1):
    #     ##daniela
    # elif(p==2):
    #     ##laura
    # else:
    #     ##sofia
    # print(g.getNome())
    # jogo(g.getNome(),0,0)
    jogo(0,0)


lb = Label(janela, text="Bem vindo", font=fontGrande).place(x=125, y=100)
lb = Label(janela, text="Nome:", font=fontePequena).place(x=65, y=300)
nome = Entry(janela, width=15, font=fontePequena, fg='blue')
nome.place(x=125, y=300)
voice = Button (janela, text="Falar", command=falar)
voice.place(x=320, y=300)
bt = Button (janela, text="Entrar", font=fontePequena, command=login)
bt.place(x=180, y=500)

janela.mainloop()