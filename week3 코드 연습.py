"화면 입출력"

'표준 입력 함수 input()'

###코드 3-1

print("enter your name")
somebody=input()
print("hi", somebody,"how are you today?")

#변수(자료형, 문자형)에 상관없이 연결 가능. 한칸 띄고 연결 출력
print("heollo world!","hello again!")


###코드 3-2


temperature=float(input("온도를 입력하세요: "))
print(temperature)

###코드3-3
print("섭씨에서 화씨변경 프로그램")
print("섭씨온도를 입력하세요")

celsius=input()
fahrenheit=(float(celsius)*1.8)+32 #문자형을 실수형으로 변환

print("섭씨온도:", celsius)
print("화씨온도: ",fahrenheit)

'리스트의 이해'
#코드 3-4
colors=['red','blue','green']
print(colors[0])
print(colors[1])
print(len(colors))

#슬라이싱
#변수명[시작 인덱스:마지막 인덱스]
cities = ['서울', '부산', '인천', '대구', '대전', '광주', '울산', '수원']
#           0       1       2      3       4       5      6       7
#          -8       -7      -6    -5      -4      -3      -2     -1

print(cities[0])

print(cities[-8])

print(cities[-8:])  #['서울', '부산', '인천', '대구', '대전', '광주', '울산', '수원']

print(cities[:])

#증가값
#변수명[시작 인덱스:마지막 인덱스:증가값]

#2칸 단위로 
print(cities[::2])  #['서울', '인천', '대전', '울산']

#역으로 슬라이싱
print(cities[::-1]) #['수원', '울산', '광주', '대전', '대구', '인천', '부산', '서울']

#리스트의 연산 

#덧셈 연산 

color1=['red','blue','green']
color2=['orenge','black','white']
print(color1+color2)   #['red', 'blue', 'green', 'orenge', 'black', 'white']

len(color1)

total_color=color1+color2
print(total_color)


apple=color1*3
print(apple)


v='blue' in color2
print(v)


#리스트 추가 및 삭제 

#append( ) 함수 
color=['red','blue','green']
color.append('white')
print(color)

#extent() 함수 
color=['red','blue','green']
color.extend(['black','purple'])
print(color)

#insert() 함수 
color=['red','blue','green']
color.insert(0,'orenge')
print(color)

#remove( ) 함수 
color=['red','blue','green']
color.remove('red')
print(color)

#인덱스의 재할당과 삭제 
#재할당: 원하는 자리에 새로운 값으로 대체
color=['red','blue','green']
color[0]='orenge'
print(color)  #['orenge', 'blue', 'green']

#삭제: 삭제하고 싶은 자리 지정 
del color[0]
print(color)  #['blue', 'green']


#패킹과 언패킹 
#패킹 

t=[1,2,3]
a,b,c=t
print(t,a,b,c)  #[1, 2, 3] 1 2 3

#이차원 리스트 
kor_score= [0,1, 2, 3, 4]
math_score=[5,6, 7, 8, 9]
eng_score=[10,11,12,13,14]
midtern_score=[kor_score,math_score,eng_score]

print(midtern_score[0],[2])  #[0, 1, 2, 3, 4] [2]

print(midtern_score[0][2])  #2

'리스트의 메모리 관리 방식'


kor_score= [0,1, 2, 3, 4]
math_score=[5,6, 7, 8, 9]
eng_score=[10,11,12,13,14]
midtern_score=[kor_score,math_score,eng_score]

math_score[0]=100000
print(midtern_score)  #[[0, 1, 2, 3, 4], [100000, 6, 7, 8, 9], [10, 11, 12, 13, 14]]


#값과 메모리 주소값의 차이 
#일반적으로 -5에서 256 사이의 정수는 항상 동일한 객체를 참조

##1)
a=300
b=300

#is는 메모리 주소를 비교하는 연산자 
a is b  #False

#==는 값을 비교하는 연산자 
a==b   #True

##2)?????????????????????????????????????????
a=1
b=1

a is b  # True

a==b   # True


#메모리 구조로 인한 리스트 특징 
##1) 하나의 리스트에 다양한 자료형 포함 가능 
a=["color",1,0.2]
color=['yellow','blue','green','black','purple']

a[0]=color
print(a)  #[['yellow', 'blue', 'green', 'black', 'purple'], 1, 0.2]

###2) 리스트의 저장 방식 
a=[5,4,3,2,1]
b=[1,2,3,4,5]
b=a               #b에 a를 할당
print(b)          #b를 출력하면 a와 변수와 같은 값 출력됨 

####3) a만 정렬하고 b를 출력하는 경우 
    #sort()함수는 리스트에 있는 값들의 순서를 오름차순으로 변환 
a=[5,4,3,2,1]
b=[1,2,3,4,5]

a.sort()
print(b)     #[1, 2, 3, 4, 5]


####4)b에 새로운 값을 할당할 시 
    # b에 새로운 값을 할당하면 a와b는 같은 메모리 주소와 연결되지 않음 
      ## b는 새로운 메모리 주소에 새로운 값을 할당 가능 
        ### b=a, 어떤 리스트값을 하나의 변수에 할당하는 순간, 
         #### 두 변수는 같은 메모리 주소에 연걸된다. 
          #### '='의 의미는 같다가 아닌, 메모리 주소에 해당 값을 할당(연결)한다는 의미 
a=[5,4,3,2,1]
b=[1,2,3,4,5]

a.sort()
print(b)     #[1, 2, 3, 4, 5]

b=[6,7,8,9,10]
print(a,b)     #[1, 2, 3, 4, 5] [6, 7, 8, 9, 10]

 






























