from tkinter import *
from tkinter.ttk import *
import csv
import random
import threading
import time

def rps_func():
    global rock
    global sci
    global paper
    global point_p
    global point_s
    l=['r','p','s']
    player_move=None
    point_p=0
    point_s=0
    rps=Toplevel(sp)
    sp.iconify()
    comprock=PhotoImage(file='comprock.png', master=rps)
    comppaper=PhotoImage(file='comppaper.png', master=rps)
    compsci=PhotoImage(file='compsci.png', master=rps)
    one=PhotoImage(file='1.png', master=rps)
    two=PhotoImage(file='2.png', master=rps)
    three=PhotoImage(file='3.png', master=rps)
    rock=PhotoImage(file='rock n.png', master=rps)
    paper=PhotoImage(file='paper n.png', master=rps)
    sci=PhotoImage(file='sci n.png', master=rps)
    
    def main_menu_rps():
        rps.destroy()
        sp.deiconify()
    
    def randfunc(l1,canv,player_move):
        global point_p
        global point_s
        no=random.randint(0,2)
        move=l1[no]
        if move=='r':
            canv.create_image(26,140,anchor=NW,image=comprock)
            if player_move=='p1':
                point_p+=1
                score_p(point_p)
            elif player_move=='s1':
                point_s+=1
                score_s(point_s)
        elif move=='p':
            canv.create_image(26,140,anchor=NW,image=comppaper)
            if player_move=='s1':
                point_p+=1
                score_p(point_p)
            elif player_move=='r1':
                point_s+=1
                score_s(point_s)
        elif move=='s':
            canv.create_image(26,140,anchor=NW,image=compsci)
            if player_move=='r1':
                point_p+=1
                score_p(point_p)
            elif player_move=='p1':
                point_s+=1
                score_s(point_s)
                
    def score_p(point_p):
        if point_p==1:
            canv.create_image(500,510,anchor=NW,image=one)
        elif point_p==2:
            canv.create_image(500,510,anchor=NW,image=two)
        elif point_p==3:
            canv.create_image(500,510,anchor=NW,image=three)
            rockbutton.destroy()
            paperbutton.destroy()
            scibutton.destroy()
            canv.delete('all')
            canv.create_text(300, 250, text='YOU WIN', font=("Times New Roman", 30), fill='white')
            main_menu_but=Button(canv, text="\nMAIN MENU\n", command=main_menu_rps)
            main_menu_but.place(x=260, y=300)
            
    def score_s(point_s):
        if point_s==1:
            canv.create_image(1,510,anchor=NW,image=one)
        elif point_s==2:
            canv.create_image(1,510,anchor=NW,image=two)
        elif point_s==3:
            canv.create_image(1,510,anchor=NW,image=three)
            rockbutton.destroy()
            paperbutton.destroy()
            scibutton.destroy()
            canv.delete('all')
            canv.create_text(300, 250, text='YOU LOSE', font=("Times New Roman", 30), fill='white')
            main_menu_but=Button(canv, text="\nMAIN MENU\n", command=main_menu_rps)
            main_menu_but.place(x=260, y=300)
            
    def sciplay():
        canv.create_image(326,140,anchor=NW,image=compsci)
        player_move='s1'
        randfunc(l,canv,player_move)
        
    def rockplay():
        canv.create_image(326,140,anchor=NW,image=comprock)
        player_move='r1'
        randfunc(l,canv,player_move)
        
    def paperplay():
        canv.create_image(326,140,anchor=NW,image=comppaper)
        player_move='p1'
        randfunc(l,canv,player_move)
        
    rps.geometry('600x600')
    rps.title('ROCK PAPER SCISSOR')
    canv=Canvas(rps, bg='dark blue', height='600', width='600')
    canv.create_text(400,20,text="YOU", font=('Brush Script MT', 30), fill='white')
    canv.create_text(150,20,text="AMNesia", font=('Brush Script MT', 30), fill='white')
    line=canv.create_line(1,500,599,500,fill="white")
    line1=canv.create_line(300,1,300,499,fill="white")
    rockbutton=Button(canv,image=rock,command=rockplay)
    paperbutton=Button(canv,image=paper,command=paperplay)
    scibutton=Button(canv,image=sci,command=sciplay)
    rockbutton.place(x=150,y=510)
    paperbutton.place(x=250,y=510)
    scibutton.place(x=350,y=510)
    canv.pack()

def nm_func():
    global numstart
    global numend
    global count
    nm=Toplevel(sp)
    sp.iconify()
    nm.title('Number Memory')
    nm.geometry('700x600')
    numstart=0
    numend=10
    count=1
    sub=PhotoImage(file='sub.png')
        
    def numgen():
        global numstart
        global numend
        global num_str
        global count
        num=0
        num=random.randint(numstart, numend)
        numstart+=10**count
        numend+=10**(count+1)
        num_str=str(num)
        num=canv2.create_text(200, 200)
        canv2.itemconfig(num, text=num_str, fill='white', font=("Times New Roman", 32))
        nm.after(5000, lambda: canv2.itemconfig(num, text=''))
        nm.after(6000, lambda: enter_value())
        count+=1
    def enter_value():
        global num_enter
        global info
        global submit
        info=canv2.create_text(200, 100)
        canv2.itemconfig(info, text='ENTER THE NUMBER', fill='black', font=("Times New Roman", 20))
        num_enter=Entry(nm, font=('Times New Roman', 24))
        canv2.create_window(200, 200, window=num_enter,width=382)
        submit=Button(canv2, image=sub, command=lambda: process())
        submit.place(x=120, y=300)

    def process():
        value=num_enter.get()
        if value==num_str:
            nm.after(5, lambda: canv2.delete('all'))
            nm.after(10, lambda: submit.destroy())
            nm.after(15, lambda: numgen())
        else:
            canv2.delete('all')
            submit.destroy()
            canv2.create_text(200, 100, text="The Number", fill='black', font=("Times New Roman", 20))
            canv2.create_text(200, 150, text=num_str, fill='dark green', font=("Times New Roman", 20))
            canv2.create_text(200, 200, text="Your Answer", fill='black', font=("Times New Roman", 20))
            canv2.create_text(200, 250, text=value, fill='red', font=("Times New Roman", 20))
            nm.after(3000, lambda: nm.destroy())
            nm.after(1000, lambda: sp.deiconify())
    canv2=Canvas(nm, bg='light blue', height='400', width='400')
    canv2.pack()
    numgen()   

def tt_func():
    import tkinter as tk
    sp.iconify()
    class TypeSpeedGUI:
        def __init__(self):
            self.root = Toplevel(sp)
            self.root.title ("Typing Speed Test")
            self.root.geometry("800x600")
            self.root.configure(bg='light blue')
            
            self.texts = open("texts.txt" , "r").read().split("\n")

            self.frame=tk.Frame(self.root)
                        
            self.sample_label = tk.Label(self.frame, text=random.choice(self.texts), font=("Helvetica", 18))
            self.sample_label.grid(row=0, column=0, columnspan=2, padx=5, pady=10)
            
            self.input_entry = tk.Entry(self.frame, width=40, font=("Helvetica", 24))
            self.input_entry.grid(row=1, column=0, columnspan=2, padx=5, pady=10)
            self.input_entry.bind("<KeyPress>", self.start)
            
            self.speed_label = tk.Label(self.frame, text="Speed: \n0.00 Characters Per Second\n0.00 Characters Per Minute", font=("Helvetica", 18))
            self.speed_label.grid(row=2, column=0, columnspan=2, padx=5, pady=10)

            self.frame.pack(expand=True)
                
            self.counter=0
            self.running=False
            self.root.mainloop()
            
        def start(self, event):
            if not self.running:
                if not event.keycode in [16, 17, 18]:
                    self.running = True
                    t=threading.Thread(target=self.time_thread)
                    t.start()
            if not self.sample_label.cget('text').startswith(self.input_entry.get()):
                self.input_entry.config(fg="red")
            else:
                self.input_entry.config(fg="black")
            if self.input_entry.get() == self.sample_label.cget("text")[:-1]:
                self.running=False
                self.input_entry.config(fg="green")
                self.root.after(8000, lambda: self.root.destroy())
                self.root.after(1000, lambda: sp.deiconify())

        def time_thread(self):
            while self.running:
                time.sleep(0.1)
                self.counter+=0.1
                cps=len(self.input_entry.get()) / self.counter
                cpm=cps*60
                self.speed_label.config(text=f"Speed: \n{cps:.2f} Characters Per Second\n{cpm:.2f} Characters Per Minute")

    TypeSpeedGUI()

def enter():
     global username
     global pswd
     un=username.get()
     pw=pswd.get()
     if un!="" and pw!="":
         fileobj=open("Amnesia Game Emporium.csv", "r")
         robj=csv.reader(fileobj)
         for rec in robj:
             if rec!=[]:
                 if rec[0]==un:
                     if rec[1]==pw:
                         canvas.destroy()
                         canvas1=Canvas(sp, bg='white', height='900', width='900')
                         rps_button=Button(canvas1, image=rps_image, command=rps_func)
                         nm_button=Button(canvas1, image=nm_image, command=nm_func)
                         tt_button=Button(canvas1, image=tt_image, command=tt_func)
                         logout_button=Button(canvas1, image=logout_image, command=logout_func)
                         rps_button.place(x=100, y=100)
                         nm_button.place(x=100, y=300)
                         tt_button.place(x=100, y=500)
                         logout_button.place(x=700, y=15)
                         canvas1.pack()
                     else:
                        canvas.create_text(720, 485, text="Invalid Username or Password.", fill='red', font=('Times New Roman', 20))
         else:
             canvas.create_text(720, 485, text="Invalid Username or Password.", fill='red', font=('Times New Roman', 20))
     else:
        canvas.create_text(720, 485, text="Invalid Username or Password.", fill='red', font=('Times New Roman', 20))

def logout_func():
    sp.destroy()
        
def signup_new():
    username_str=username1.get()
    pswd_str=pswd1.get()
    if username_str !="" and pswd_str!="":
        rec=[username_str, pswd_str]
        filobj=open("Amnesia Game Emporium.csv", "a")
        wobj=csv.writer(filobj)
        wobj.writerow(rec)
        filobj.close()
        canvas.destroy()
        canvas1=Canvas(sp, bg='white', height='900', width='900')
        rps_button=Button(canvas1, image=rps_image, command=rps_func)
        nm_button=Button(canvas1, image=nm_image, command=nm_func)
        tt_button=Button(canvas1, image=tt_image, command=tt_func)
        logout_button=Button(canvas1, image=logout_image, command=logout_func)
        rps_button.place(x=100, y=100)
        nm_button.place(x=100, y=300)
        tt_button.place(x=100, y=500)
        logout_button.place(x=700, y=15)
        canvas1.pack()
    else:
        canvas.create_text(720, 485, text="Invalid Username or Password.", fill='red', font=('Times New Roman', 20))
        
def signup():
    global username1
    global pswd1
    username.destroy()
    pswd.destroy()
    login_button.destroy()
    signup_button.destroy()
    username1=Entry(sp, width=15, font=('Times New Roman', 24))
    canvas.create_window(720, 400, window=username1)
    pswd1=Entry(sp, width=15, font=('Times New Roman', 24))
    canvas.create_window(720, 450, window=pswd1)
    login_button1=Button(canvas, text='\nSIGN UP\n', width=20,  command=signup_new)
    login_button1.place(x=750, y=500)

sp=Tk()
sp.title('Amnesia Game Emporium')
sp.geometry('1000x1000')
logo=PhotoImage(file='logo.png')
login=PhotoImage(file='login.png')
rps_image=PhotoImage(file='rps_image.png', master=sp)
nm_image=PhotoImage(file='nm_image.png', master=sp)
tt_image=PhotoImage(file='tt_image.png', master=sp)
logout_image=PhotoImage(file='logout.png', master=sp)
canvas=Canvas(sp, bg='white', height='900', width='900')
canvas.create_image(290, 400, image=logo)
canvas.create_image(710, 250, image=login)
canvas.create_text(600, 600, text="Don't have an account yet?", fill='black', font=('Times New Roman', 20))
signup_button=Button(canvas, text='Sign Up', command=signup)
signup_button.place(x=780, y=585)
username=Entry(sp, width=15, font=('Times New Roman', 24))
canvas.create_text(500, 400, text="Enter Username:", fill='black', font=('Times New Roman', 20))
canvas.create_window(720, 400, window=username)
pswd=Entry(sp, width=15, font=('Times New Roman', 24))
canvas.create_text(535, 450, text="Password:", fill='black', font=('Times New Roman', 20))
canvas.create_window(720, 450, window=pswd)
login_button=Button(canvas, text='\nLOGIN\n', width=20,  command=enter)
login_button.place(x=750, y=500)
canvas.pack()


