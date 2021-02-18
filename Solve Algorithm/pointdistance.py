# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
"""
3개 점의 (x,y)좌표 입력 받고
삼각형이 만들어지는 지 확인 
만들어지는 경우 : 삼각형 넓이 구하기 
만들어지지 않는 경우: return 0 
"""

import math 
# 점 좌표에 대한 class 
class Point:
	def _init_(self,x,y):
		self.x=x
		self.y=y
	def setdata(self, x,y):
		self.x=x
		self.y=y
		
# 두점 사이의 거리 구하는 func
def distance(a=Point(), b=Point()):
	return math.sqrt(math.pow(a.x-b.x,2)+math.pow(a.y-b.y,2))


#point1
x1, y1= map(int, input("input").split())
#point2
x2, y2=map(int,input().split())
#point3
x3, y3=map(int,input().split())


# 객체 생성 
point1= Point()
point2= Point()
point3=Point()
point1.setdata(x1,y1)
point2.setdata(x2,y2)
point3.setdata(x3,y3)

# 3개 점의 거리 구하기
s1= distance(point1,point2)
s2= distance(point2,point3)
s3 =distance(point1,point3)

# 삼각형 되려면 => max가 나머지 두개의 합보다 작아야 함
m=max(s1, s2, s3)

# 삼각형 넓이 구하는 공식 : 헤론의 공식 이용
# 헤론의 공식 : ABC넓이= root(p(p-a)(p-b)(p-c))
p=(s1+s2+s3)/2
if m==s1:
    if m>s2+s3:
        print("0")
    else:
        print("%0.2f"% math.sqrt(p*(p-s1)*(p-s2)*(p-s3)))
elif m==s2:
    if m>s1+s3:
        print("0")
    else:
        print("%0.2f"% math.sqrt(p*(p-s1)*(p-s2)*(p-s3)))
else:
    if m>s1+s2:
        print("0")
    else:
        print("%0.2f"% math.sqrt(p*(p-s1)*(p-s2)*(p-s3)))
