import pandas as pd
import datetime as dt


class IDcard:

    def __init__(self):
        while True:
            print("< ID카드 발급양식 작성기 >\n")
            print("사용방법")
            print("1.파일명 입력 ex)전체회원명부.xlsx")
            print("2.라이선스 발급년도 작성 ex)2022")
            print("3.라이선스 갯수에 입력할 라이선스 갯수입력 후 엔터 ex)100")
            print("4.라이선스번호를 갯수만큼 입력하세요 ex)#K2000\n")
            self.filename = input("파일명 :")
            print("...로딩중...\n")
            self.load()
            print("...로딩 완료!...\n")
            self.get_list = ['라이선스','영문','생년월일','이름']
            self.input_list = []
            self.year = int(input("발급년도:"))
            Num = int(input("라이선스 갯수 :"))
            for _ in range(Num):
                self.input_lic = input()
                self.input_list.append(self.input_lic)    
            self.Lic_set()

    def load(self):
        self.path = '.\\'
        filename = self.filename
        self.df = pd.read_excel(filename,sheet_name='회원관리자료')
    
    def Lic_set(self):
        month_list = [0,"January","February","March","April","May","June","July","August","September","October","November","December"]
        for i in self.input_list:
            L = self.df.loc[self.df['라이선스'] == i,self.get_list]
            val_list = L.values.tolist()
            n_lic = str(val_list[0][0])
            n_eng = str(val_list[0][1])
            n_brt = str(val_list[0][2])
            n_name = str(val_list[0][3])
            if n_lic[:3] == "#KM":
                n_pro = "Master Golf"
            else:
                n_pro = "Certified Golf"
            year = n_brt[0:4]
            month = n_brt[5:7]
            month = month_list[int(month)]
            day = n_brt[8:10]
            print(n_name+"%"+"Lic. "+n_lic+"%"+n_pro+"%"+"Teaching Professional"+"%"+"Name : "+n_eng+"%"+"D.O.B : "+month,day+", "+year+"%"+"Exp.12/"+str(self.year)+"%"+n_lic[1:]+"%"+n_lic[0:])

if __name__ == '__main__':
 
    Example = IDcard()
