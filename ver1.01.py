from encodings import utf_8
import tkinter
import snake_hard

def openFrame(frame): #프레임 변경
    frame.tkraise()

def easystart():
    end()
    snake_hard.start()
    
def hardstart():
    end()
    snake_hard.start()
    

def end():
    win.destroy()

def ranklist():
    f = open('Ranking.txt', 'r',encoding='UTF-8')
    print(f.readlines())
    ranklb.text.set("Test")
    f.close()

snackc = ['black', 'blue', 'green', 'deeppink', 'yellow']
feedc = ['yellow', 'teal', 'navy', 'black', 'green']

win = tkinter.Tk();
win.title('Welcome to Snake Game!!')
win.geometry('385x368')

win.resizable(width=False, height=False)

mainframe = tkinter.Frame(win)
modeframe = tkinter.Frame(win)
settingframe = tkinter.Frame(win)
rankingframe = tkinter.Frame(win)

mainframe.grid(row=0, column=0, sticky="nsew")
modeframe.grid(row=0, column=0, sticky="nsew")
settingframe.grid(row=0, column=0, sticky="nsew")
rankingframe.grid(row=0, column=0, sticky="nsew")


backlb1 = tkinter.Label(settingframe, text="배경색", width=11, height=2, bg = 'lightblue')
backlb1.grid(row=0, column=0,columnspan=2, pady=(0,4))



backgc1 = tkinter.Button(settingframe,width =4, height =2, bg ='aqua')
backgc1.grid(row=1, column=0,padx=2)
backgc2 = tkinter.Button(settingframe,width =4, height =2, bg ='beige')
backgc2.grid(row=1, column=1,padx=2)
backgc3 = tkinter.Button(settingframe,width =4, height =2, bg ='lightgreen')
backgc3.grid(row=1, column=2,padx=2)
backgc4 = tkinter.Button(settingframe,width =4, height =2, bg ='aquamarine')
backgc4.grid(row=1, column=3,padx=2)
backgc5 = tkinter.Button(settingframe,width =4, height =2, bg ='darksalmon')
backgc5.grid(row=1, column=4,padx=2)
backgc6 = tkinter.Button(settingframe,width =4, height =2, bg ='darksalmon')
backgc6.grid(row=1, column=5,padx=2)
backgc7 = tkinter.Button(settingframe,width =4, height =2, bg ='darksalmon')
backgc7.grid(row=1, column=6,padx=2)
backgc8 = tkinter.Button(settingframe,width =4, height =2, bg ='darksalmon')
backgc8.grid(row=1, column=7,padx=2)
backgc5 = tkinter.Label(settingframe,width =5, height =2)
backgc5.grid(row=1, column=8,padx=2)


backlb2 = tkinter.Label(settingframe, text="뱀 색", width=11, height=2, bg = 'lightblue')
backlb2.grid(row=2, column=0,columnspan=2, pady=(7,4))

backgc1 = tkinter.Button(settingframe,width =4, height =2, bg ='aqua')
backgc1.grid(row=3, column=0,padx=2)
backgc2 = tkinter.Button(settingframe,width =4, height =2, bg ='beige')
backgc2.grid(row=3, column=1,padx=2)
backgc3 = tkinter.Button(settingframe,width =4, height =2, bg ='lightgreen')
backgc3.grid(row=3, column=2,padx=2)
backgc4 = tkinter.Button(settingframe,width =4, height =2, bg ='aquamarine')
backgc4.grid(row=3, column=3,padx=2)
backgc5 = tkinter.Button(settingframe,width =4, height =2, bg ='darksalmon')
backgc5.grid(row=3, column=4,padx=2)

backlb3 = tkinter.Label(settingframe, text="먹이 색", width=11, height=2, bg = 'lightblue')
backlb3.grid(row=4, column=0,columnspan=2, pady=(7,4))

backgc1 = tkinter.Button(settingframe,width =4, height =2, bg ='aqua')
backgc1.grid(row=5, column=0,padx=2)
backgc2 = tkinter.Button(settingframe,width =4, height =2, bg ='beige')
backgc2.grid(row=5, column=1,padx=2)
backgc3 = tkinter.Button(settingframe,width =4, height =2, bg ='lightgreen')
backgc3.grid(row=5, column=2,padx=2)
backgc4 = tkinter.Button(settingframe,width =4, height =2, bg ='aquamarine')
backgc4.grid(row=5, column=3,padx=2)
backgc5 = tkinter.Button(settingframe,width =4, height =2, bg ='darksalmon')
backgc5.grid(row=5, column=4,padx=2)

backlb4 = tkinter.Label(settingframe, text="창 크기", width=11, height=2, bg = 'lightblue')
backlb4.grid(row=6, column=0,columnspan=2, pady=(7,4))

backlb4_1 = tkinter.Label(settingframe)
input_text = tkinter.Entry(backlb4_1, width=11)

backlb4_1.grid(row=7, column=0,columnspan=2)
input_text.grid(ipady=4)

backbtn = tkinter.Button(settingframe, text = '확인',width=5,bg="#00ffff")
backbtn.grid(row=7, column=2)

ranklb = tkinter.Label(rankingframe, text="",bg = 'lightblue')
ranklb.grid(row=0, column=0)

gotomode = tkinter.Button(mainframe, text="START",width =15, height =2,command=lambda:[openFrame(modeframe)], bg ='skyblue')
gotoset = tkinter.Button(mainframe, text="SETTING",width=15,height =2,command=lambda:[openFrame(settingframe)], bg = 'gray')
gotorank = tkinter.Button(mainframe, text="RANKING",width=15,height =2,command=lambda:[openFrame(rankingframe),ranklist()], bg = 'orange')

easybtn = tkinter.Button(modeframe, text = 'EASY',width=25,height = 10,bg="#00ffff",command=lambda:[easystart()])
hardbtn = tkinter.Button(modeframe, text = 'HARD',width=25,height = 10,bg="#ff9999",command=lambda:[hardstart()])
vsbtn = tkinter.Button(modeframe, text = 'VS MODE',width=25,height = 10,bg="#ffc000")
bossbtn = tkinter.Button(modeframe, text = 'BOSS MODE',width=25,height = 10,bg="lightgray")

back = tkinter.Button(modeframe, text="BACK", command=lambda:[openFrame(mainframe)],bg="#99ff99")
back2 = tkinter.Button(settingframe, text="BACK", command=lambda:[openFrame(mainframe)],bg="#99ff99")
back3 = tkinter.Button(rankingframe, text="BACK", command=lambda:[openFrame(mainframe)],bg="#99ff99")




# ranklist = open('Ranking.txt', 'r',encoding='UTF-8')



gotomode.grid(row=0, column=0,padx=(10,0), pady=(230,5),sticky="s")
gotoset.grid(row=1,column=0,padx=(10,0), pady=(0,0),sticky="s")
gotorank.grid(row=2,column=0,padx=(10,0), pady=(5,5))
easybtn.grid(row=0, column=0,padx=(5,0), pady=5)
hardbtn.grid(row=0, column=1,padx=(5,5), pady=5)
vsbtn.grid(row=1, column=0,padx=(5,0), pady=(0,5))
bossbtn.grid(row=1, column=1,padx=5, pady=(0,5))
back.grid(row= 2,columnspan = 2,sticky="nsew",padx=5)
back2.grid(row= 8,columnspan = 200,padx=2,pady=(2,0),sticky="sew")
back3.grid()





















openFrame(mainframe) #기본메인화면



win.mainloop();




