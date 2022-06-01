import tkinter
import tkinter.messagebox

def showRanking(snake):
    global ranking
    ranking = tkinter.Tk();
    ranking.title('랭킹')

    rankframe = tkinter.Frame(ranking)
    rankframe.grid(row=0, column=0, sticky="nsew")   

    rankinf = tkinter.Label(rankframe, text="닉네임을 입력해 주십시오.(특수문자 X)", width=30, height=2, bg = 'lightblue')

    rankEntlb = tkinter.Label(rankframe)
    global rankEnt
    rankEnt = tkinter.Entry(rankEntlb, width=20)

    okbtn = tkinter.Button(rankframe, text = '확인',width=5,bg="#00ffff", command=
    lambda:[getinp(snake)])

    rankinf.grid(row=0, column=0, columnspan=2,sticky="nsew")

    rankEntlb.grid(row=1, column=0)
    rankEnt.grid()
    okbtn.grid(row=1, column=1 ,sticky="e")

    ranking.mainloop()

def warningMsg():
    tkinter.messagebox.showwarning("경고","특수문자는 입력할 수 없습니다!")

def successMsg():
    tkinter.messagebox.showinfo("알림","정상적으로 랭킹에 입력되었습니다!")    

def getinp(snake):
    global nickname
    nickname = rankEnt.get()
    if (nickname.isalnum()):
        successMsg()
        f = open("Ranking.txt", 'a')
        f.write("\n" + nickname + "," + str(len(snake)))
        f.close()
        print("Ranking.txt에 추가되었습니다.")
        ranking.destroy()
    else:
        warningMsg()


