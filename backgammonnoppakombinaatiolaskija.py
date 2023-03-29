from tkinter import *
import tkinter as tk
import time
root = Tk() 
root.title('backgammonnoppakombinaatiolaskija') 
# Initialize tkinter window with dimensions 300 x 250 
name_label = tk.Label(root, text = 'Sinun nappuloitten sijainti:', font=('calibre',10, 'bold'))
name_label.place(x=100,y=0)     
name_label2 = tk.Label(root, text = 'Vastustajan nappuloitten sijainnit:', font=('calibre',10, 'bold'))
name_label2.place(x=100,y=90)
root.geometry("400x500")

name_var = tk.StringVar()
name_var2 = tk.StringVar()

player_name = Entry(root,textvariable = name_var, font=('calibre',10,'normal'))
player_name.pack(pady=30)
player_name2 = Entry(root,textvariable = name_var2, font=('calibre',10,'normal'))
player_name2.pack(pady=60)

maara = 0
musta = 0
valkoinen = 0
name_label22 = tk.Label(root)
name_label222 = tk.Label(root)
luvut = []
yp = 0
def nay():
    global luvut
    global yp
    global kl
    yp = 25
    xxs = 1
    if len(kl) > 140:
        fon = 7
        up = 15
        xup = 200
    else:
        fon = 10
        up = 20
        xup = 340    
    window = tk.Toplevel(root)
    canvas = tk.Canvas(window, height=800, width=1400)
    canvas.pack()
    lukuw = tk.Label(window, text = 'Käyvät:', font=('calibre',10, 'bold'))
    lukuw.place(x=10,y=0)    
    for x in kl:
        luku = tk.Label(window, text = f'{x}', font=('calibre',fon, 'bold'))
        luku.place(x=xxs,y=yp)
        yp += up
        if yp == 745:
            xxs += xup
            yp = 25   
    luvut = []
    kl = []    

def sau():
    global eiluvut
    windows = tk.Toplevel(root)
    canvass = tk.Canvas(windows, height=800, width=200)
    canvass.pack()
    yp = 25
    lukuww = tk.Label(windows, text = 'EI käyvät:', font=('calibre',10, 'bold'))
    lukuww.place(x=10,y=0)
    for x in eiluvut:
        lukua = tk.Label(windows, text = f'{x}', font=('calibre',10, 'bold'))
        lukua.place(x=10,y=yp)
        yp += 20
    eiluvut = []        

    

kl = []
eiluvut = []
jooluvut = ["1,1","1,2","1,3","1,4","1,5","1,6","2,1","2,2","2,3","2,4","2,5","2,6","3,1","3,2","3,3","3,4","3,5","3,6","4,1","4,2","4,3","4,4","4,5","4,6","5,1","5,2","5,3","5,4","5,5","5,6","6,1","6,2","6,3","6,4","6,5","6,6"]
def laske():
    global kl
    global name_label22
    global name_label222
    global luvut
    global eiluvut
    name_label22.destroy()
    name_label222.destroy()
    global musta
    global valkoinen
    name = name_var.get()
    name2 = name_var2.get()
    musta = eval("["+name2+"]")
    valkoinen = eval("["+name+"]")
    testi = []
    valkoinen = sorted(valkoinen)
    for s in valkoinen:
        if valkoinen.count(s) > 1:
            testi.append(s)
            list(filter(lambda a: a != s, valkoinen))    
    print(testi)
    valkoinen = set(valkoinen) - set(testi)
    valkoinen = list(valkoinen)
    print(valkoinen)
    global maara
    x = 0
    noppak = [1,1,1,2,1,3,1,4,1,5,1,6,2,1,2,2,2,3,2,4,2,5,2,6,3,1,3,2,3,3,3,4,3,5,3,6,4,1,4,2,4,3,4,4,4,5,4,6,5,1,5,2,5,3,5,4,5,5,5,6,6,1,6,2,6,3,6,4,6,5,6,6]
    for s in musta:
        x = 0
        while x < len(noppak):
            if x != len(noppak)-1:
                if noppak[x] == noppak[x+1]:
        		#tupla
                    if s + noppak[x] in valkoinen or s + noppak[x] * 2 in valkoinen or s + noppak[x] * 3 in valkoinen or s + noppak[x] * 4 in valkoinen:
                        if s + noppak[x] not in valkoinen:
                            if s + noppak[x] * 2 in valkoinen:
                                if s + noppak[x] not in testi:
                                    maara += 1                                       
                                    luvut.append("{},{}".format(noppak[x],noppak[x+1]))
                                    if "Nopat: {},{}    V-nappula: {}    S-nappula: {}".format(noppak[x],noppak[x+1],s,s + noppak[x] * 2) not in kl: 
                                        kl.append("Nopat: {},{}    V-nappula: {}    S-nappula: {}".format(noppak[x],noppak[x+1],s,s + noppak[x] * 2))                                        
                            if s + noppak[x] * 3 in valkoinen:
                                if s + noppak[x] not in testi and s + noppak[x] * 2 not in testi:
                                    luvut.append("{},{}".format(noppak[x],noppak[x+1]))
                                    maara += 1
                                    if "Nopat: {},{}    V-nappula: {}    S-nappula: {}".format(noppak[x],noppak[x+1],s,s + noppak[x] * 3) not in kl:
                                        kl.append("Nopat: {},{}    V-nappula: {}    S-nappula: {}".format(noppak[x],noppak[x+1],s,s + noppak[x] * 3))                                         
                            if s + noppak[x] * 4 in valkoinen:
                                if s + noppak[x] not in testi and s + noppak[x] * 2 not in testi and s + noppak[x] * 3 not in testi:
                                    luvut.append("{},{}".format(noppak[x],noppak[x+1]))
                                    maara += 1
                                    if "Nopat: {},{}    V-nappula: {}    S-nappula: {}".format(noppak[x],noppak[x+1],s,s + noppak[x] * 4) not in kl:
                                        kl.append("Nopat: {},{}    V-nappula: {}    S-nappula: {}".format(noppak[x],noppak[x+1],s,s + noppak[x] * 4))                                         
                        else:    
                            luvut.append("{},{}".format(noppak[x],noppak[x+1]))
                            maara += 1
                            if "Nopat: {},{}    V-nappula: {}    S-nappula: {}".format(noppak[x],noppak[x+1],s,s + noppak[x]) not in kl:
                                kl.append("Nopat: {},{}    V-nappula: {}    S-nappula: {}".format(noppak[x],noppak[x+1],s,s + noppak[x]))
                else:
               #ei tupla
                    if s + noppak[x] in valkoinen or s + noppak[x+1] in valkoinen or s + noppak[x] + noppak[x+1] in valkoinen:
                        if s + noppak[x] not in valkoinen and s + noppak[x+1] not in valkoinen:
                            if s + noppak[x] not in testi or s + noppak[x+1] not in testi:
                                luvut.append("{},{}".format(noppak[x],noppak[x+1]))
                                maara += 1
                                if "Nopat: {},{}    V-nappula: {}    S-nappula: {}".format(noppak[x],noppak[x+1],s,s + noppak[x] + noppak[x+1]) not in kl:
                                    kl.append("Nopat: {},{}    V-nappula: {}    S-nappula: {}".format(noppak[x],noppak[x+1],s,s + noppak[x] + noppak[x+1]))                                                                        
                        else:    
                            luvut.append("{},{}".format(noppak[x],noppak[x+1]))
                            maara += 1
                            if s + noppak[x] not in valkoinen:
                                if "Nopat: {},{}    V-nappula: {}    S-nappula: {}".format(noppak[x],noppak[x+1],s,s + noppak[x+1]) not in kl:
                                    kl.append("Nopat: {},{}    V-nappula: {}    S-nappula: {}".format(noppak[x],noppak[x+1],s,s + noppak[x+1]))
                            else:
                                if "Nopat: {},{}    V-nappula: {}    S-nappula: {}".format(noppak[x],noppak[x+1],s,s + noppak[x]) not in kl:
                                    kl.append("Nopat: {},{}    V-nappula: {}    S-nappula: {}".format(noppak[x],noppak[x+1],s,s + noppak[x]))    
            x += 2
    time.sleep(0.1)
    omo = sorted(luvut)
    for g in omo:
        if luvut.count(g) > 1:
            luvut.remove(g)                     
    name_label22 = tk.Label(root, text = f"Mahdollisuus: {len(luvut)}/36", font=('calibre',10, 'bold'))
    name_label22.place(x=100,y=290)
    name_label222 = tk.Label(root, text = f"Prosenteissa: {100 / 36 * len(luvut)}%", font=('calibre',10, 'bold'))
    name_label222.place(x=100,y=320)
    time.sleep(0.1)
    maara = 0
    for f in jooluvut:
        if f not in luvut:
            eiluvut.append(f)
    print(eiluvut)        
    nay()
    sau()



# musta on syövä
# valkoinen syötävä
def ohjeet():
    window2 = tk.Toplevel(root)
    canvas2 = tk.Canvas(window2, height=400, width=1300)
    canvas2.pack()
    luku = tk.Label(window2, text = 'Huom! jos katsot vastustajan nappuloitten mahdollisuuksia syödä sinua, niin varmista, että kotipesäsi on oikea-alakulmassa. \nJos katsot sinun mahdollisuuksia syödä vastustajaa, niin käännä lautaa 180 astetta ja varmista että kotipesäsi on oikea-alakulmassa\n Huom! jos käänsit lautaa 180 astetts, niin tee seuraava vastustajan perspektiivistä!\nEli pistä "sinun nappulat" kaikki sinun nappulat sijainnin mukaan eli kotipesäsi eka on 1 toka 2  ja vastustajan kotipesän vika on 24 jne\nSitten pistä kaikki vastustajan nappulat samanlailla "vastustajan nappulat" kenttään, sitten paina laske, Kohteessa käyvät näät heitot joilla vastustaja voi sinut syödä "Nopat = heitto ja\n S- nappulat tarkoittaa Syötävä ja V nappulat vastustajan nappulaa"\n ja ei käyvissä naet heitot jolla vastustaja ei voi sinua syödä', font=('calibre',10, 'bold'))
    luku.place(x=0,y=0)            


sub_btn = tk.Button(root,text = 'Laske', command = laske)
sub_btn.pack()
sub = tk.Button(root,text = 'Käyttöopas', command = ohjeet)
sub.place(x=20,y=0)
root.mainloop() 