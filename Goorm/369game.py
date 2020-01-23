"""
<369게임>
게임이 끝난 숫자 N이 주어졌을 때
N이전까지 박수를 친 횟수를 구하여라

input -> output
  10  ->  3
  35  ->  15
"""

# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
user_input = input() #N
count=0
for k in range(1,int(user_input)): #1-user_input까지 숫자 반복 , k=int
	a=str(k) # k를 문자열로 만들기
	for i in a:     # 문자열 순서대로 탐색
		#i자리의 값이 3의 배수이면 count 증가
		N=int(i) # 자리수 3의 배수인지 알아보려고 정수로 바꿔줌 
		if N!=0 and N%3==0: 
			count=count+1
print(count)	