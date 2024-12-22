'''문자열 S를 입력받은 후에, 각 문자를 R번 반복해 새 문자열 P를 만든 후 출력하는 프로그램을 작성하시오. 즉, 첫 번째 문자를 R번 반복하고, 두 번째 문자를 R번 반복하는 식으로 P를 만들면 된다. S에는 QR Code "alphanumeric" 문자만 들어있다.

QR Code "alphanumeric" 문자는 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ\$%*+-./: 이다.

첫째 줄에 테스트 케이스의 개수 T가 주어지고 각 테스트 케이스는 반복회수 R 문자열 S 가 공백으로 구분되어 주어진다.
S의 길이는 적어도 1이며 20글자를 넘지 않는다.'''

x = int(input())
y = []*x
for i in range(x):
    a,b = input().split()
    c = '' 
    for j in range(len(b)):
        c = c + b[j]*int(a)
    y.append(c)
    
for i in range(x):
    print(y[i])