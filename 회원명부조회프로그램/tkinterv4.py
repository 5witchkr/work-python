from tkinter import *
import pandas as pd
import tkinter.font
from tkinter import messagebox
# import time
import tkinter.ttk


class tkgui:


    def __init__(self):
        print("로딩중...")
        self.load()
        print("로딩완료...!")
        self.window = Tk()
        self.window.title("USGTF-KOREA")
        self.window.geometry('1100x400')
        self.window.resizable(False, False)

        font = tkinter.font.Font(size=10,weight="bold")

        self.get_list = ['적용연도','라이선스','성명','영문','직책','입회일','생년월일','연령','성별','전화번호1','주소','주소','입금일자']

        ##라이선스로 찾기
        self.label_Li = Label(self.window, text="라이선스로 찾기 :", font=font)
        self.label_Li.place(x=210,y=30)

        self.entry_Li = Entry(self.window, width=6)
        self.entry_Li.place(x=320,y=30)

        B1 = Button(text = "찾기", font=font, command = self.Lic_set)
        B1.place(x=380,y=25)

        ##콤보박스
        self.values=[i for i in range(2022,2023)] 
        self.combobox=tkinter.ttk.Combobox(self.window, height=8, values=self.values)
        self.combobox.place(x=20, y=30)
        self.combobox.set("년도 선택")


        # ###프로그레스바
        # self.p_var2 = DoubleVar()
        # self.progressbar2 = ttk.Progressbar(self.window, maximum=100, length=150, variable=self.p_var2)
        # self.progressbar2.place(x=900,y=50)


        ##이름으로 찾기
        self.label_Nam = Label(self.window, text="이름으로 찾기 :", font=font)
        self.label_Nam.place(x=210,y=70)

        self.entry_Nam = Entry(self.window, width=6)
        self.entry_Nam.place(x=320,y=70)

        B2 = Button(text = "찾기", font=font, command = self.Nam_set)
        B2.place(x=380,y=65)



        ##라이선스
        self.label_Lic = Label(self.window, text="라이선스", font=font)
        self.label_Lic.place(x=510,y=10)

        self.entry_Lic = Entry(self.window, width=7)
        self.entry_Lic.place(x=570,y=10)

        ##성함
        self.label_Name = Label(self.window, text="성함", font=font)
        self.label_Name.place(x=510,y=40)

        self.entry_Name = Entry(self.window, width=6)
        self.entry_Name.place(x=570, y=40)

        ##영문
        self.label_Eng = Label(self.window, text="영문이름", font=font)
        self.label_Eng.place(x=510,y=70)

        self.entry_Eng = Entry(self.window, width=20)
        self.entry_Eng.place(x=570,y=70)

        ##전화번호
        self.label_Num = Label(self.window, text="전화번호", font=font)
        self.label_Num.place(x=510,y=100)

        self.entry_Num = Entry(self.window, width=14)
        self.entry_Num.place(x=570,y=100)

        ##생년월일
        self.label_br = Label(self.window, text="생년월일", font=font)
        self.label_br.place(x=700,y=100)

        self.entry_br = Entry(self.window, width=10)
        self.entry_br.place(x=760,y=100)

        ##주소
        self.label_Adres = Label(self.window, text="주소", font=font)
        self.label_Adres.place(x=510,y=130)

        self.entry_Adres = Entry(self.window, width=74)
        self.entry_Adres.place(x=570,y=130)


        ##상태창
        self.label_textExample = Label(self.window, text="상태창", font=font)
        self.label_textExample.place(x=10,y=170)

        self.textExample = Listbox(self.window, selectmode="single", width=70)
        self.textExample.place(x=10, y=200)

        B3 = Button(self.window, text="찾기", font=font,command=self.list_set)
        B3.place(x=70,y=165)

        # ##입회일
        # self.label_enter = Label(self.window,text = "입회일", font=font)
        # self.label_enter.place(x=510, y=160)

        # self.entry_enter = Entry(self.window, width=10)
        # self.entry_enter.place(x=570, y=160)

        ###load버튼
        self.load_B = Button(text = "새로고침",font=font, command = self.load)
        self.load_B.place(x=1020,y=10)


        # ###SAVE 버튼
        # SAVE_B = Button(text = "저장하기", command = self.SAVE_set)
        # SAVE_B.place(x=900,y=370)

        # ###엑셀파일로 SAVE
        # SAVE_B2 = Button(text = "엑셀에 저장", command = self.SAVE2_set)
        # SAVE_B2.place(x=1000,y=370)

        self.window.mainloop()

    def load(self):
        self.path = '.\\'
        filename = '★★★전체회원관리자료1.xlsb'
        self.df = pd.read_excel(filename,sheet_name='회원관리자료')
        self.message1()
        



    def all_del(self):
        self.entry_Name.delete(0,"end")
        self.entry_Num.delete(0,"end")
        self.entry_Lic.delete(0,"end")
        self.entry_Adres.delete(0,"end")
        self.entry_Eng.delete(0,"end")
        self.textExample.delete(0,"end")
        self.entry_Li.delete(0,"end")
        self.entry_Nam.delete(0,"end")
        self.entry_br.delete(0,"end")

# self.get_list = ['적용연도','라이선스','성명','영문','직책','입회일','생년월일','연령','성별','전화번호1','전화번호2','주소','입금일자']
    def Lic_set(self):
        L = self.df.loc[(self.df['적용연도'] == 2022) & (self.df['라이선스'] == self.entry_Li.get()),self.get_list]
        val_list = L.values.tolist()
        if len(val_list) == 1:
            self.all_del()
            self.entry_Name.insert(0,val_list[0][2])
            self.entry_Num.insert(0,val_list[0][9])
            self.entry_Lic.insert(0,val_list[0][1])
            self.entry_Adres.insert(0,val_list[0][11])
            self.entry_Eng.insert(0,val_list[0][3])
            self.entry_br.insert(0,val_list[0][6])


    def Nam_set(self):
        # thisyear = self.combobox.get()
        L = self.df.loc[(self.df['적용연도'] == 2022) & (self.df['성명'] == self.entry_Nam.get()),self.get_list]
        val_list = L.values.tolist()
        if len(val_list) == 1:
            self.all_del()
            self.entry_Name.insert(0,val_list[0][2])
            self.entry_Num.insert(0,val_list[0][9])
            self.entry_Lic.insert(0,val_list[0][1])
            self.entry_Adres.insert(0,val_list[0][11])
            self.entry_Eng.insert(0,val_list[0][3])
            self.entry_br.insert(0,val_list[0][6])

        else:
            self.all_del()
            for i in val_list:
                self.textExample.insert(END,i[0:11])

    def list_set(self):
        L_B = self.textExample.get(self.textExample.curselection())[1]
        L = self.df.loc[(self.df['적용연도'] == 2022) & (self.df['라이선스'] == L_B), self.get_list]
        val_list = L.values.tolist()
        self.all_del()
        self.entry_Name.insert(0,val_list[0][2])
        self.entry_Num.insert(0,val_list[0][9])
        self.entry_Lic.insert(0,val_list[0][1])
        self.entry_Adres.insert(0,val_list[0][11])
        self.entry_Eng.insert(0,val_list[0][3])
        self.entry_br.insert(0,val_list[0][6])


    def message1(self):
        messagebox.showinfo('안내','데이터 로딩이 완료되었습니다.')

    # def SAVE_set():
    #     df.loc[df['라이선스'] == entry_Lic.get(),['주소']] = entry_Adres.get()
    #     df.loc[df['라이선스'] == entry_Lic.get(),['영문']] = entry_Eng.get()
    #     df.loc[df['라이선스'] == entry_Lic.get(),['전화번호1']] = entry_Num.get()
    #     df.loc[df['라이선스'] == entry_Lic.get(),['이름']] = entry_Name.get()
    #     all_del()



    # def SAVE2_set():
    #     df.to_excel('전체명부테스트용.xlsx',sheet_name = '회원관리자료',index=False)

if __name__ == '__main__':
 
    Example = tkgui()
