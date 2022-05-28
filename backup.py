import tkinter

def openFrame(frame):
	frame.tkraise()
    
win = tkinter.Tk();
win.geometry('500x500')
win.title('Welcome to Snake Game!!')

mainframe = tkinter.Frame(win)
modeframe = tkinter.Frame(win)
settingframe = tkinter.Frame(win)

mainframe.grid(row=0, column=0, sticky="nsew")
modeframe.grid(row=0, column=0, sticky="nsew")
settingframe.grid(row=0, column=0, sticky="nsew")

lbstart = tkinter.Label(mainframe, width=20, height=10)
lbsetting = tkinter.Label(mainframe, width=20, height=10)

lbeasy = tkinter.Label(modeframe, width=20, height=10)
lbhard = tkinter.Label(modeframe, width=20, height=10)
lbvs = tkinter.Label(modeframe, width=20, height=10)
lbboss = tkinter.Label(modeframe, width=20, height=10)
lbback1 = tkinter.Label(modeframe, width=20, height=10)
lbback2 = tkinter.Label(settingframe, width=20, height=10)

easybtn = tkinter.Button(lbeasy, text = 'EASY');
hardbtn = tkinter.Button(lbhard, text = 'HARD');
vsbtn = tkinter.Button(lbvs, text = 'VS MODE');
bossbtn = tkinter.Button(lbboss, text = 'BOSS MODE');
gotomode = tkinter.Button(lbstart, text="START",command=lambda:[openFrame(modeframe)])
gotoset = tkinter.Button(lbsetting, text="SETTING",command=lambda:[openFrame(settingframe)])
back = tkinter.Button(lbback1, text="BACK", command=lambda:[openFrame(mainframe)])
back2 = tkinter.Button(lbback2, text="BACK", command=lambda:[openFrame(mainframe)])

gotomode.place()
gotoset.place()
back.place()
back2.place()
easybtn.place()
hardbtn.place()
vsbtn.place()
bossbtn.place()

lbstart.place(x = 10, y = 10)
lbsetting.place(x = 50, y = 10)
lbeasy.place(x = 10, y = 10)
lbhard.place(x = 40, y = 10)
lbvs.place(x = 70, y = 10)
lbboss.place(x = 100, y = 10)
lbback1.place(x = 0, y = 10)
lbback2.place(x = 0, y = 10)
openFrame(mainframe) #기본메인화면

win.mainloop();




