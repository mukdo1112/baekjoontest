'''문제
알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 단, 대문자와 소문자를 구분하지 않는다.

입력
첫째 줄에 알파벳 대소문자로 이루어진 단어가 주어진다. 주어지는 단어의 길이는 1,000,000을 넘지 않는다.

출력
첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다. 단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.'''


x = input().upper()
count_x = []
del_x = list(set(x))
y = 0
for i in del_x:
    count_x.append(x.count(i))
    
if count_x.count(max(count_x)) > 1:
    print('?')
    
else :
    for i in range(len(del_x)):
        if max(count_x) == count_x[i]:
            y = i
            
    print(del_x[y])
    
    
    
    
'''index 함수를 쓰면 다른 배열의 몇 번째 값인지 알 수 있다
    수정 ver'''
x = input().upper()
count_x = []
del_x = list(set(x))
y = 0
for i in del_x:
    count_x.append(x.count(i))
    
if count_x.count(max(count_x)) > 1:
    print('?')
    
else :
    print(del_x[count_x.index(max(count_x))])