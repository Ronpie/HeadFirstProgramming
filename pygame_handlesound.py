import pygame.mixer
from tkinter import *
import sys


def wait_finish(channel):
    while channel.get_busy():
        pass

def correct_answer_button():
    num_correct.set(num_correct.get()+1)
    correct_sound.play()

def wrong_answer_button():
    num_wrong.set(num_wrong.get()+1)
    wrong_sound.play()
def end_program():
    print("Ending program now")
    exit()
    

sounds = pygame.mixer
sounds.init()

correct_sound = sounds.Sound("./data/hfprog_sounds/correct.wav")
wrong_sound = sounds.Sound("./data/hfprog_sounds/wrong.wav")

app = Tk()
app.title("GUI for announcing correct/wrong answer by sound")
app.geometry('720x480+200+100')#window cooridinates and size values
#sde 'left','right','top','bottom'
l1 = Label(app,text='when you are ready, click on the buttons!',height=3)
l1.pack()

num_correct= IntVar()
num_wrong= IntVar()
num_correct.set(0)
num_wrong.set(0
)

l2 = Label(app,textvariable=num_correct)
l2.pack(side='right')
l2.pack(expand=2)
l2_text = Label(app,text='Correct answer:')
l2_text.pack(side='right')
l3_text = Label(app,text='Wrong answer:')
l3_text.pack(side='left')
l3 = Label(app,textvariable=num_wrong)
l3.pack(side='left')


b1 = Button(app,text="Correct",width=10,borderwidth=20,background='green',command=correct_answer_button)
b1.pack(side='right',padx=10,pady=10)
b2 = Button(app,text="Wrong",width=10,borderwidth=20,background='gray', command=wrong_answer_button) #default relief="raised"
b2.pack(side='left',padx=10,pady=10)
b3 = Button(app,text="End",width=10,background='red',activebackground='red',borderwidth=20,command=end_program)
b3.pack(side='bottom',padx=10,pady=10)
app.mainloop()

# number_asked =0
# number_correct=0
# number_wrong=0


# host_response = input('press 1 for correct answer, 2 for incorrect or 0 to end ')
# while host_response != '0':
#     if host_response == '1':
#         number_asked += 1
#         number_correct += 1
#         wait_finish(correct_sound.play())
#     else:
#         number_asked += 1
#         number_wrong += 1
#         wait_finish(wrong_sound.play())
#     host_response = input('press 1 for correct answer, 2 for incorrect or 0 to end ')

