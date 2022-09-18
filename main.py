#-----------------------------------
#BOUNCE game by- Sanoj kumar pradhan
#-----------------------------------

import time
from tkinter import*
import random
import tkinter.messagebox


main=Tk()
main1=Tk()
main1.geometry("350x370")
main1.title("Bounce!")
main.title("Bounce!")
main.resizable(0,0)
main.wm_attributes()
x=0

file=open("text.txt","r")
pscore= file.read()
file.close()
print(pscore)
canvas=Canvas(main,width=500,height=500,bd=0,highlightthickness=0)
canvas.configure(bg="light yellow")
canvas.create_text(230,470,text="SCORE:")
canvas.create_text(230,490,text="PREV SCORE:")
var=StringVar()
widget = Label(canvas, textvariable= var,bg="light yellow")
widget2 = Label(canvas, text= pscore,bg="light yellow")
widget.pack()
widget2.pack()
q=1
canvas.create_window(300, 470, window=widget)
canvas.create_window(300, 490, window=widget2)
canvas.pack()
main.update()

class Ball:
    def __init__(self,canvas,P,score,color):
        self.canvas=canvas
        self.P=P
        self.score=score
        self.id=canvas.create_oval(10,10,25,25,fill=color)
        self.canvas.move(self.id,245,100)
        start=[-3,-2,-1,1,2,3]
        random.shuffle(start)
        self.x=start[0]
        self.y=-1
        self.canvas_height=self.canvas.winfo_height()
        self.canvas_width=self.canvas.winfo_width()
        self.i=0
        self.chance=0
        self.h=0

    def hit_paddle(self,pos):
        paddle_pos=self.canvas.coords(self.P.id)
        if pos[2]>=paddle_pos[0] and pos[0]<=paddle_pos[2]:
            if pos[3]>=paddle_pos[1] and pos[1]<=paddle_pos[3]:
                return True
            return False
    def hit_score(self,pos):
        score_pos=self.canvas.coords(self.score.id)
        if pos[2]>=score_pos[0] and pos[0]<=score_pos[2]:
            if pos[3]>=score_pos[1] and pos[1]<=score_pos[3]:
               self.i+=1
               return True

    def score_updater(self):
        global var
        global x
        for i in range(self.i+1):
            x=self.i*100
            var.set(str(x))

    def draw(self):
        self.canvas.move(self.id,self.x,self.y)
        pos= self.canvas.coords(self.id)
        if pos[0]<=0:
            self.x=q
        if pos[1]<=0:
            self.y=q
        if pos[2]>=self.canvas_width:
            self.x=-q
        if pos[3]>=self.canvas_height:
            self.y=-q
            global main
            while True:
                if self.chance==0:
                    ans=tkinter.messagebox.askquestion("c","2 chances left!,do you want to continue?")
                    if ans=="yes":
                        self.chance+=1
                        break
                    else:
                        main.destroy()
                        break
                if self.chance==1:
                    ans = tkinter.messagebox.askquestion("c", "1 chance left!,do you want to continue?")
                    if ans == "yes":
                        self.chance += 1
                        break
                    else:
                        main.destroy()
                        break
                if self.chance==2:
                    global file
                    global x
                    file = open("text.txt", "w")
                    file.write(str(x))
                    file.close()
                    ans=tkinter.messagebox.showinfo("c", "chances exhausted :(, Hope to see you soon,take care!")
                    if ans=="ok":
                        main.destroy()
                        break
        if self.hit_paddle(pos)==True:
            self.y=-q
        if self.hit_score(pos)==True:
            self.y=q
            self.score_updater()

class paddle:
    def __init__(self,canvas,color):
        self.canvas=canvas
        self.id=self.canvas.create_rectangle(0,0,100,10,fill=color)
        self.canvas.move(self.id,200,350)
        self.x=0
        self.canvas_width=self.canvas.winfo_width()
        self.canvas.bind_all("<KeyPress-Left>",self.turn_left)
        self.canvas.bind_all("<KeyPress-Right>",self.turn_right)

    def draw(self):
        self.canvas.move(self.id,self.x,0)
        pos= self.canvas.coords(self.id)
        if pos[0]<=0:
            self.x=0
        if pos[2]>=self.canvas_width:
            self.x=0
    def turn_left(self,evt):
        self.x=-2
    def turn_right(self,evt):
        self.x=2

class Score:
    def __init__(self,canvas,x1,y1,x2,y2,color):
        self.canvas=canvas
        self.id=canvas.create_rectangle(x1,y1,x2,y2,fill=color)


score=Score(canvas,230,0,270,5,"Blue")
P=paddle(canvas,"Blue")
ball=Ball(canvas,P,score,"Red")

def Easy(event):
    global q
    q=3
    easybut = Button(main1, text="Easy")
    easybut.place(x=40, y=210)

    main1.destroy()
    while True:
        ball.draw()
        P.draw()
        P.draw()
        main.update_idletasks()
        time.sleep(0.01)
        main.update()

def Hard(event):
    global q
    q=6
    hardbut = Button(main1, text="Hard")
    hardbut.place(x=200, y=210)

    main1.destroy()
    while True:
        ball.draw()
        P.draw()
        P.draw()
        main.update_idletasks()
        time.sleep(0.01)
        main.update()
def instruction(event):

    plabel = Label(main1, text= "\nBOUNCE is a solo game in which a player needs to hit the ball to "
                                "\nthe Blue bar at the top and score a 100 for each successful hit."
                                "\nSo, to rebound the ball a paddle is provided.In order to move "
                                "\nthe paddle towards the left, 'Left arrow key' needs to be pressed "
                                "\nand to move right,'Right arrow key'.Player will get 3 CHANCES in total"
                                "\nto score as much as he/she can and set the target for the next player."
                                "\n Happy Gaming! and All the best!", fg="Blue",font=("Helvetica", 10))


    plabel.place(x=10, y=240)




inst=Button(main1,text="INSTRUCTION",font=("Helvetica",10))
inst.bind("<Button-1>",instruction)
inst.pack(side=BOTTOM)
pong=Label(main1,text="BOUNCE",font=("Futura 60 underline"),fg="Red")
pong.place(x=45,y=0)
label=Label(main1,text="By-" "\n Sanoj kumar pradhan" ,font=("Helvetica",20))
label1=Label(main1,text="Select Level" ,font=("Helvetica Bold",20),fg="Black")
label1.place(x=110,y=180)
label.place(x=70,y=90)
easybut=Button(main1,text="Easy")
easybut.place(x=50,y=210)
easybut.bind("<Button-1>",Easy)
hardbut=Button(main1,text="Hard")
hardbut.place(x=230,y=210)
hardbut.bind("<Button-1>",Hard)

main1.mainloop()
main.mainloop()
