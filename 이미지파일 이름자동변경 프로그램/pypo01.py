import tkinter.messagebox as msgbox
from tkinter import *
import os
import re

text = open('.\\xxlname.txt', 'rt', encoding='UTF8')
path = '.\\'

def save_data():
    names = os.listdir(path)
    lines = text.readlines()
    L = []

    for o in lines:
        o = re.split('\W+', o)
        o = o[0] + " " + o[3] + '.jpg'
        L.append(o)

    for idx, i in enumerate(L, start=int(address.get())):
        if i in names:
            dst = path + str(description.get()) + str(idx) + '.jpg'
            os.rename(i, dst)
            print(i, dst)
        else:
            msgbox.showinfo("알림",str(description.get()) + str(idx) + "_또는_" + str(i) + "가 없습니다.\n 파일 확장명이나 파일명을 확인해주세요.\n 작업을 중단합니다.")
            app.destroy()

    if not False:
        msgbox.showinfo("알림", "작업이 끝났습니다.")
        app.destroy()


app = Tk()
app.title('KOREA')
app.geometry('300x200')

Label(app, text = "면허알파벳:").pack()
description = Entry(app)
description.pack()


Label(app, text = "면허숫자:").pack()
address = Entry(app)
address.pack()


Button(app, text = "실행", command = save_data).pack()
app.mainloop()
