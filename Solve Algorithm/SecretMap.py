"""
def solution(n, arr1, arr2):
    answer = []
    # arr을 2진수로 다 변환하기
    for i in range(n):
        ans=''
        temp1,temp2=[],[]
        num1=arr1[i]
        num2=arr2[i]
        for j in range(n):
            if (num1-2**(n-j-1))>=0: 
                temp1.append(1)
                num1-=2**(n-j-1)
            else:
                temp1.append(0)

        for k in range(n):
            if (num2-2**(n-k-1))>=0: 
                temp2.append(1)
                num2-=2**(n-k-1)
            else:
                temp2.append(0)


        for s in range(n):
            if temp1[s]==1 or temp2[s]==1:
                ans+='#'
            else:  
                ans+=' '
        answer.append(ans)
    return answer
"""
# 비트 연산자 이용해주기!! 
# bin => 2진수로 만들어주는 함수 (OUTPUT: 원래값+B+2=이진수값 이므로 슬라이싱하기)
def solution(n, arr1, arr2):
    answer = []
    for i,j in zip(arr1,arr2):
        a=str(bin(i|j)[2:])
        a=a.rjust(n,'0') #2진수로 만든숫자에 앞부분을 0으로 채워줌 
        a=a.replace('1', '#')
        a=a.replace('0', ' ')
        answer.append(a)
    return answer

n=5
arr1=[9, 20, 28, 18, 11]
arr2=[30, 1, 21, 17, 28]
print(solution(n, arr1, arr2))