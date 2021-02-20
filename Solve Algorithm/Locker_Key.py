"""
[ 카카오 - 자물쇠와 열쇠 ]
고고학자인 튜브는 고대 유적지에서 보물과 유적이 가득할 것으로 추정되는 비밀의 문을 발견하였습니다. 
그런데 문을 열려고 살펴보니 특이한 형태의 자물쇠로 잠겨 있었고 문 앞에는 특이한 형태의 열쇠와 함께 
자물쇠를 푸는 방법에 대해 다음과 같이 설명해 주는 종이가 발견되었습니다.

잠겨있는 자물쇠는 격자 한 칸의 크기가 1 x 1인 N x N 크기의 정사각 격자 형태이고 특이한 모양의 열쇠는 M x M 크기인 정사각 격자 형태로 되어 있습니다.

자물쇠에는 홈이 파여 있고 열쇠 또한 홈과 돌기 부분이 있습니다. 
열쇠는 회전과 이동이 가능하며 열쇠의 돌기 부분을 자물쇠의 홈 부분에 딱 맞게 채우면 자물쇠가 열리게 되는 구조입니다. 
자물쇠 영역을 벗어난 부분에 있는 열쇠의 홈과 돌기는 자물쇠를 여는 데 영향을 주지 않지만, 자물쇠 영역 내에서는 
열쇠의 돌기 부분과 자물쇠의 홈 부분이 정확히 일치해야 하며 열쇠의 돌기와 자물쇠의 돌기가 만나서는 안됩니다. 
또한 자물쇠의 모든 홈을 채워 비어있는 곳이 없어야 자물쇠를 열 수 있습니다.

열쇠를 나타내는 2차원 배열 key와 자물쇠를 나타내는 2차원 배열 lock이 매개변수로 주어질 때, 
열쇠로 자물쇠를 열수 있으면 true를, 열 수 없으면 false를 return 하도록 solution 함수를 완성해주세요.

[ 제한사항 ]
key는 M x M(3 ≤ M ≤ 20, M은 자연수)크기 2차원 배열입니다.
lock은 N x N(3 ≤ N ≤ 20, N은 자연수)크기 2차원 배열입니다.
M은 항상 N 이하입니다.
key와 lock의 원소는 0 또는 1로 이루어져 있습니다.
0은 홈 부분, 1은 돌기 부분을 나타냅니다.

"""
# 90' 회전하는 Function
def rotate(key):
    m=len(key)
    newkey=[[0]*m for _ in range(m)]
    # key[i][j] -> newkey[j][m-i-1]로 이동
    for i in range(m):
        for j in range(m):
            newkey[j][m-i-1]=key[i][j]
    return newkey
# key+lock의 원소를 해본 결과가 모두 1인지(들어맞는지) check
def check(newlock):
    onelock=len(newlock)//3
    #가운데 부분만 의미
    for i in range(onelock,onelock*2):
        for j in range(onelock,onelock*2):
            if newlock[i][j]!=1: # 1이 아닌경우
                return False
    return True

def solution(key, lock):
    m=len(key)
    n=len(lock)
    # lock보다 3배 큰 list만들기 
    lock3=[[0]*(n*3) for _ in range(n*3)]
    # 가운데에 lock넣어주기 
    for i in range(n):
        for j in range(n):
            lock3[n+i][n+j]=lock[i][j]
    # 4가지 회전 방향에 대해서 모두확인하기
    for k in range(4):
        key=rotate(key)
        # 새로운 lock의 모든(x,y)에 대해 확인
        for x in range(n*2):
            for y in range(n*2):
                # 열쇠 끼어넣고 더해보기
                for i in range(m):
                    for j in range(m):
                        lock3[x+i][y+j]+=key[i][j]
                # 더한값이 모두 1인지 check (가운데 부분)
                if check(lock3): return True
                # 다시 원상태로  돌아가기
                for i in range(m):
                    for j in range(m):
                        lock3[x+i][y+j]-=key[i][j]

    return False



key=[[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock=[[1, 1, 1], [1, 1, 0], [1, 0, 1]]
print(solution(key,lock))
