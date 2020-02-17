"""
지민이는 자신의 저택에서 MN개의 단위 정사각형으로 나누어져 있는 M*N 크기의 보드를 찾았다. 
어떤 정사각형은 검은색으로 칠해져 있고, 나머지는 흰색으로 칠해져 있다.
 지민이는 이 보드를 잘라서 8*8 크기의 체스판으로 만들려고 한다.

체스판은 검은색과 흰색이 번갈아서 칠해져 있어야 한다. 
구체적으로, 각 칸이 검은색과 흰색 중 하나로 색칠되어 있고, 변을 공유하는 두 개의 사각형은 다른 색으로 칠해져 있어야 한다. 
따라서 이 정의를 따르면 체스판을 색칠하는 경우는 두 가지뿐이다. 
하나는 맨 왼쪽 위 칸이 흰색인 경우, 하나는 검은색인 경우이다.

보드가 체스판처럼 칠해져 있다는 보장이 없어서, 지민이는 8*8 크기의 체스판으로 잘라낸 후에 몇 개의 정사각형을 다시 칠해야겠다고 생각했다. 
당연히 8*8 크기는 아무데서나 골라도 된다. 지민이가 다시 칠해야 하는 정사각형의 최소 개수를 구하는 프로그램을 작성하시오.

[INPUT]

첫째 줄에 N과 M이 주어진다. 
N과 M은 8보다 크거나 같고, 50보다 작거나 같은 자연수이다.
둘째 줄부터 N개의 줄에는 보드의 각 행의 상태가 주어진다.
B는 검은색이며, W는 흰색이다.


[OUTPUT]
첫째 줄에 지민이가 다시 칠해야 하는 정사각형 개수의 최솟값을 출력한다.


[Solution]
1. [0][0]=> 흰색으로 시작하는 체스판 or 검정으로 시작하는 체스판을 만들때 
           얼마나 본래 list를 변경해야하는지에 대한 list를 새로 만들기

본래)      => 흰색으로 시작하는 체스판   => 검정색으로 시작하는 체스판
wbwbwb           000000                        111111
bwbwbw           000000                        111111
bwwbwb           100000                        011111


2. 큰 판을 8*8로 잘라보는것을 모두 반복해서 1의 갯수 세기

"""

N,M=map(int,input().split( ))
total=[]
# Data입력하면서 W=1, B=0으로 바꾸기
for i in range(N):
    string=input()
    total.append(string)    

#White로 시작하는 체스판을 만들 때 변경 할 것
w_chess=[]
def MakeWhitechess(A):
    whitechess=[]
    for index, rowstring in enumerate(A):
        white=[]
        if index%2==0:
            current_color='W'
        else:
            current_color='B'

        for value in rowstring:
            if value==current_color: 
                white.append(0)
            else:
                white.append(1)

            if current_color=='W':
                current_color='B'
            else:
                current_color='W'
        whitechess.append(white)
    return whitechess
w_chess=MakeWhitechess(total)

#Black으로 시작하는 체스판만들 때 변경할 것 
b_chess=[]
def MakeBlackchess(A):
    blackchess=[]
    for index, rowstring in enumerate(A):
        black=[]
        if index%2==0:
            current_color='B'
        else:
            current_color="W"

        for value in rowstring:
            if value==current_color:
                black.append(0)
            else:
                black.append(1)
            if current_color=='W':
                current_color='B'
            else:
                current_color='W' 
        blackchess.append(black)
    return blackchess
b_chess=MakeBlackchess(total)


"""
8*8개씩 checking해보기 
checking할 때의 합이 min값보다 작으면 계속 바꿈 
"""


min_count=2500
# white로만드는 경우 다시 paint해야하는 최소한의 수
for i in range(N-8+1):
    rows=w_chess[i:i+8]
    for j in range(M-8+1):
        paint=0
        for row in rows:
            paint +=sum(row[j:j+8])
        if paint<min_count:
            min_count=paint
#Black으로 만드는 경우 다시 pain해야하는 최소한의 수 
for i in range(N-8+1):
    rows=b_chess[i:i+8]
    for j in range(M-8+1):
        paint=0
        for row in rows:
            paint +=sum(row[j:j+8])
        if paint<min_count:
            min_count=paint
print(min_count)


