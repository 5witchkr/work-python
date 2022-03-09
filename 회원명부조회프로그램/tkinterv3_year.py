from tkinter import *
import pandas as pd
import tkinter.font

print("1.파일명을 입력해주세요. ex)전체회원명부.xlsx")
fileName = input("파일명 :")
print("...로딩중...\n")
path = '.\\'
filename = fileName
df = pd.read_excel(filename,sheet_name='회원관리자료')
print("...로딩완료...!!\n")



def all_del():
    entry_Name.delete(0,"end")
    entry_Num.delete(0,"end")
    entry_Lic.delete(0,"end")
    entry_Adres.delete(0,"end")
    entry_Eng.delete(0,"end")
    textExample.delete(0,"end")
    entry_Li.delete(0,"end")
    entry_Nam.delete(0,"end")
    entry_enter.delete(0,"end")
    entry_2013.delete(0,"end")
    entry_2014.delete(0,"end")
    entry_2015.delete(0,"end")
    entry_2016.delete(0,"end")
    entry_2017.delete(0,"end")
    entry_2018.delete(0,"end")
    entry_2019.delete(0,"end")
    entry_2020.delete(0,"end")
    entry_2021.delete(0,"end")
    entry_2022.delete(0,"end")
    entry_2023.delete(0,"end")


get_list = ['라이선스','이름','전화번호1','주소','영문','생년월일','성별','발급일',2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023]


def Lic_set():
    L = df.loc[df['라이선스'] == '#'+entry_Li.get(),get_list]
    val_list = L.values.tolist()
    all_del()
    entry_Name.insert(0,val_list[0][1])
    entry_Num.insert(0,val_list[0][2])
    entry_Lic.insert(0,val_list[0][0])
    entry_Adres.insert(0,val_list[0][3])
    entry_Eng.insert(0,val_list[0][4])
    entry_enter.insert(0,val_list[0][7])
    entry_2013.insert(0,val_list[0][8])
    entry_2014.insert(0,val_list[0][9])
    entry_2015.insert(0,val_list[0][10])
    entry_2016.insert(0,val_list[0][11])
    entry_2017.insert(0,val_list[0][12])
    entry_2018.insert(0,val_list[0][13])
    entry_2019.insert(0,val_list[0][14])
    entry_2020.insert(0,val_list[0][15])
    entry_2021.insert(0,val_list[0][16])
    entry_2022.insert(0,val_list[0][17])
    entry_2023.insert(0,val_list[0][18])


def Nam_set():
    L = df.loc[df['이름'] == entry_Nam.get(),get_list]
    val_list = L.values.tolist()
    if len(val_list) == 1:
        all_del()
        entry_Name.insert(0,val_list[0][1])
        entry_Num.insert(0,val_list[0][2])
        entry_Lic.insert(0,val_list[0][0])
        entry_Adres.insert(0,val_list[0][3])
        entry_Eng.insert(0,val_list[0][4])
        entry_enter.insert(0,val_list[0][7])
        entry_2013.insert(0,val_list[0][8])
        entry_2014.insert(0,val_list[0][9])
        entry_2015.insert(0,val_list[0][10])
        entry_2016.insert(0,val_list[0][11])
        entry_2017.insert(0,val_list[0][12])
        entry_2018.insert(0,val_list[0][13])
        entry_2019.insert(0,val_list[0][14])
        entry_2020.insert(0,val_list[0][15])
        entry_2021.insert(0,val_list[0][16])
        entry_2022.insert(0,val_list[0][17])
        entry_2023.insert(0,val_list[0][18])

    else:
        all_del()
        for i in val_list:
            textExample.insert(END,i[0:4])

def list_set():
    L_B = textExample.get(textExample.curselection())[0]
    L = df.loc[df['라이선스'] == L_B,get_list]
    val_list = L.values.tolist()
    all_del()
    entry_Name.insert(0,val_list[0][1])
    entry_Num.insert(0,val_list[0][2])
    entry_Lic.insert(0,val_list[0][0])
    entry_Adres.insert(0,val_list[0][3])
    entry_Eng.insert(0,val_list[0][4])
    entry_enter.insert(0,val_list[0][7])
    entry_2013.insert(0,val_list[0][8])
    entry_2014.insert(0,val_list[0][9])
    entry_2015.insert(0,val_list[0][10])
    entry_2016.insert(0,val_list[0][11])
    entry_2017.insert(0,val_list[0][12])
    entry_2018.insert(0,val_list[0][13])
    entry_2019.insert(0,val_list[0][14])
    entry_2020.insert(0,val_list[0][15])
    entry_2021.insert(0,val_list[0][16])
    entry_2022.insert(0,val_list[0][17])
    entry_2023.insert(0,val_list[0][18])

# def SAVE_set():
#     df.loc[df['라이선스'] == entry_Lic.get(),['주소']] = entry_Adres.get()
#     df.loc[df['라이선스'] == entry_Lic.get(),['영문']] = entry_Eng.get()
#     df.loc[df['라이선스'] == entry_Lic.get(),['전화번호1']] = entry_Num.get()
#     df.loc[df['라이선스'] == entry_Lic.get(),['이름']] = entry_Name.get()
#     all_del()


# def SAVE2_set():
#     df.to_excel('전체명부테스트용.xlsx',sheet_name = '회원관리자료',index=False)



window = Tk()
window.title("USGTF-KOREA")
window.geometry('1100x400')
window.resizable(False, False)

font = tkinter.font.Font(size=10,weight="bold")

##라이선스로 찾기
label_Li = Label(window, text="라이선스로 찾기 :", font=font)
label_Li.place(x=10,y=30)

entry_Li = Entry(window, width=6)
entry_Li.place(x=120,y=30)

B1 = Button(text = "찾기", font=font, command = Lic_set)
B1.place(x=180,y=25)


##이름으로 찾기
label_Nam = Label(window, text="이름으로 찾기 :", font=font)
label_Nam.place(x=10,y=70)

entry_Nam = Entry(window, width=6)
entry_Nam.place(x=120,y=70)

B2 = Button(text = "찾기", font=font, command = Nam_set)
B2.place(x=180,y=65)



##라이선스
label_Lic = Label(window, text="라이선스", font=font)
label_Lic.place(x=510,y=10)

entry_Lic = Entry(window, width=7)
entry_Lic.place(x=570,y=10)

##성함
label_Name = Label(window, text="성함", font=font)
label_Name.place(x=510,y=40)

entry_Name = Entry(window, width=6)
entry_Name.place(x=570, y=40)

##영문
label_Eng = Label(window, text="영문이름", font=font)
label_Eng.place(x=510,y=70)

entry_Eng = Entry(window, width=20)
entry_Eng.place(x=570,y=70)

##전화번호
label_Num = Label(window, text="전화번호", font=font)
label_Num.place(x=510,y=100)

entry_Num = Entry(window, width=14)
entry_Num.place(x=570,y=100)


##주소
label_Adres = Label(window, text="주소", font=font)
label_Adres.place(x=510,y=130)

entry_Adres = Entry(window, width=70)
entry_Adres.place(x=570,y=130)


##상태창
label_textExample = Label(window, text="상태창", font=font)
label_textExample.place(x=10,y=170)

textExample = Listbox(window, selectmode="single", width=70)
textExample.place(x=10, y=200)

B3 = Button(window, text="찾기", font=font,command=list_set)
B3.place(x=70,y=165)

##입회일
label_enter = Label(window,text = "입회일", font=font)
label_enter.place(x=510, y=160)

entry_enter = Entry(window, width=10)
entry_enter.place(x=570, y=160)
##연회비2013~2022
label_2013 = Label(window,text="2013년 :", font=font)
label_2013.place(x=510, y=190)
entry_2013 = Entry(window, width=4)
entry_2013.place(x=570, y=190)

label_2014 = Label(window,text="2014년 :", font=font)
label_2014.place(x=630, y=190)
entry_2014 = Entry(window, width=4)
entry_2014.place(x=690, y=190)

label_2015 = Label(window,text="2015년 :", font=font)
label_2015.place(x=750, y=190)
entry_2015 = Entry(window, width=4)
entry_2015.place(x=810, y=190)

label_2016 = Label(window,text="2016년 :", font=font)
label_2016.place(x=870, y=190)
entry_2016 = Entry(window, width=4)
entry_2016.place(x=930, y=190)

label_2017 = Label(window,text="2017년 :", font=font)
label_2017.place(x=990, y=190)
entry_2017 = Entry(window, width=4)
entry_2017.place(x=1050, y=190)

label_2018 = Label(window,text="2018년 :", font=font)
label_2018.place(x=510, y=210)
entry_2018 = Entry(window, width=4)
entry_2018.place(x=570, y=210)

label_2019 = Label(window,text="2019년 :", font=font)
label_2019.place(x=630, y=210)
entry_2019 = Entry(window, width=4)
entry_2019.place(x=690, y=210)

label_2020 = Label(window,text="2020년 :", font=font)
label_2020.place(x=750, y=210)
entry_2020 = Entry(window, width=4)
entry_2020.place(x=810, y=210)

label_2021 = Label(window,text="2021년 :", font=font)
label_2021.place(x=870, y=210)
entry_2021 = Entry(window, width=4)
entry_2021.place(x=930, y=210)

label_2022 = Label(window,text="2022년 :", font=font)
label_2022.place(x=990, y=210)
entry_2022 = Entry(window, width=4)
entry_2022.place(x=1050, y=210)

label_2023 = Label(window,text="2023년 :", font=font)
label_2023.place(x=510, y=230)
entry_2023 = Entry(window, width=4)
entry_2023.place(x=570, y=230)

# ###refresh 버튼
# refresh_B = Button(text = "새로고침",font=font, command = refresh())
# refresh_B.place(x=1020,y=10)

# ###SAVE 버튼
# SAVE_B = Button(text = "저장하기", command = SAVE_set)
# SAVE_B.place(x=900,y=370)

# ###엑셀파일로 SAVE
# SAVE_B2 = Button(text = "엑셀에 저장", command = SAVE2_set)
# SAVE_B2.place(x=1000,y=370)

window.mainloop()
