import tkinter
import os
import tkinter.messagebox
import customtkinter as ctk
def register():
    def choixrep():
        print(os.listdir)
        rep = tkinter.filedialog.askdirectory(title='Choisissez un répertoire')
        if len(rep) > 0:
            print("vous avez choisi le répertoire ",rep)
    regist= tkinter.re
fen1 = tkinter.Tk()
fen1.geometry('400x400')
fen1.title("REPERTOIRES DES SOURCES")
fen1['bg'] = 'BLACK'
fen1.resizable(height=False,width=False)
tkinter.Label(fen1, text='Répertoire des sources').pack()
champ=ctk.CTkEntry(master=fen1, placeholder_text="Entrez l'url de la video")
champ.pack(pady=12,padx=10)
tkinter.Button(fen1, text='Votre choix', command=choixrep).pack()
##tkinter.Button(fen1, text='Enregistrer', command=fen1.register).pack()
tkinter.Button(fen1, text='Quitter', command=fen1.destroy).pack()
fen1.mainloop()
