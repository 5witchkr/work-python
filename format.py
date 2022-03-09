
def prt(LL):
    for L in LL:
        if len(L) == 10:
            print(f'{L[1]}%{L[9]}')
            print(f'{L[3]}%{L[9]}')
            print(f'{L[5]}%{L[9]}')
            print(f'{L[7]}%{L[9]}')
        elif len(L) == 8:
            print(f'{L[1]}%{L[7]}')
            print(f'{L[3]}%{L[7]}')
            print(f'{L[5]}%{L[7]}')
        else:
            print(f'err!!!!  {L}조를 확인하세요.')

t = int(input())
LL =[]

for i in range(1,t+1):
    n = input()
    n = n.replace("(",",")
    L = n.split(",")
    L.append(i)
    LL.append(L)

prt(LL)
