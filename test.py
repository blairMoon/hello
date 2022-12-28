
# x= {'name':'leo','age':31}

# print(type(x))

# a = 'Act as thoygh \n it is impossible'
# print(a)

# b= "\"Failure is simply the opportunity to begin again.\" he says.\""
# print(b)

# i = 'l'
# j = 'i'
# k = 'f'
# e = 'e'
# print(len(b))

# q = 'hello python!'
# print(q[-7:-1])

# w = 'TitanicJames'
# title = w[:7]
# directory =w[-5:]
# print(title,directory)

# x= set([5,2,1])
# print(x)

# a = int(input("숫자를 입력하세요"))
# if a < 5 :
#   print("실행")
# elif a > 5 : 
#   print('실행2')
# else:
#   print('실행3')

# money = int(input('얼마가 있으신가요?'))

# if money >= 70000:
#   print('비행기 타러 가즈아 ')
# elif 50000 <= money < 70000:
#   print('기차타러 가즈아 ')
# elif 30000 <= money < 50000:
#   print('버스타러 가즈아 ')
# else: print('걸어가즈아아아아 ')  
# weight = int(input('무게를 입력하세요'))

# if weight >= 100:
#   print('대형')
# elif 80 <= weight <100:
#   print('중형')
# elif 60 <= weight < 80:
#   print('소형') 
# else: print('초소형')
# a = 'python'  
  
# cities = ['seoul','busun','daegu'] 
# # for i in cities:
# #   print(i)  
  
# for city in cities:
#   if city == "seoul":
#     print('제 고향은' +city+'입니당당당')   
  
    
# # while a < 5: 
# #   a+= 1
#   print(a)    
  
# a = 0   
# for i in range(5):
#   a += 1
#   print(a)  

# a = 0
# for i in range(1,5):
#   a+= i  
# print(a) 

# c= 0
# b = 0 
# while c < 4:
#   c += 1
#   b += c 
  
# print(b)  


# 반복문을 사용하여 마름모를 만들어보시오 
# for i in range(1,6):
#   print(10*' '+' '*(6-i) + '*'*(2*i-1))
# for i in range(1,5):
#   print(' '* i + '*'*(2*(6-i)-1)+'*'*(2*i-1)+'*'*(2*(6-i)-1)+'*'*(2*i-1)+'*'*(2*(6-i)-1))


# for i in reversed(range(1,6)):
#   print(' '* i + '*'*(2*(6-i)-1)+'*'*(2*i-1)+'*'*(2*(6-i)-1)+'*'*(2*i-1)+'*'*(2*(6-i)-1))
# for i in reversed(range(1,5)):
#   print(10*' '+' '*(6-i) + '*'*(2*i-1))


# 구구단 만들기 

# num = int(input('구구단 프로그램 '))
# for i in range(2,10):
#   print(i,'단')
#   for j in range(1,10):
#     print(i,"x",j ,'=', i*j)

# 성적과 이름을 입력하고. 
# 성적에 따른 등급을 알려주는 프로그램을 만드시오 
# def score(score,name): 
#   if score >= 90:
#     print(name + '은 a등급입니다')
#   elif score >= 80: 
#     print(name + '은 B등급입니다')  
#   else:
#     print(name + "은 C등급입니다")  
    
    
# score(90,'수빈')

import random 
print(random.randint(1,6))