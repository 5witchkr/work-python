import pandas as pd


class dib:
    def __init__(self):
        while True:
            print("< 배송주소 발급양식 작성기 >\n")
            print("사용방법")
            # print("1.적용연도에 숫자로 해당연도를 작성 후 엔터를 누르세요. ex)2022")
            print("1.파일명을 입력해주세요. ex)전체회원명부.xlsx")
            print("2.라이선스 갯수에 입력할 라이선스 갯수입력 후 엔터 ex)100")
            print("3.라이선스번호를 갯수만큼 입력하세요 ex)#K2000\n")
            self.filename = input("파일명 :")
            print("...로딩중...\n")
            self.load()
            print("...로딩 완료!...\n")
            self.get_list = ['라이선스','이름','전화번호1','주소']
            self.input_list = []
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
        for i in self.input_list:
            L = self.df.loc[self.df['라이선스'] == i,self.get_list]
            val_list = L.values.tolist()
            n_lic = str(val_list[0][0])
            n_name = str(val_list[0][1])
            n_call = str(val_list[0][2])
            n_adr = str(val_list[0][3])
            if 'KM' in n_lic:
                n_user = "마스터프로"
            else:
                n_user = "정회원"
            print(n_lic+"%"+n_name+"%"+n_call+"%"+n_adr+"%"+n_user)


if __name__ == '__main__':
 
    Example = dib()
