'''문제
예제를 보고 규칙을 유추한 뒤에 별을 찍어 보세요.

입력
첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다. 마름모 모양으로 찍기'''

x = int(input())

for i in range(x):
    print(" " * (x-(i+1)), end='')
    print("*" * (2*i+1))
    
for j in range(x-1,0,-1):
    print(" " * (x-j), end='')
    print("*" * (2*j-1))