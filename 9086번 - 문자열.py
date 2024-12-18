'''x = int(input()) #x는 몇 번 받을지

a = [0,0,0,0,0,0,0,0,0,0] #왜 a=[]으로 칸수지정 안하고 배열 하면 오류나

for i in range(x):
    y = input()
    a[i] = y[0]+y[-1]
    
    
for j in range(x):
    print(a[j])'''
    
   
x = int(input()) #x는 몇 번 받을지

a = [] #왜 a=[]으로 칸수지정 안하고 배열 하면 오류나

for i in range(x):
    y = input()
    a.append(y[0]+y[-1])
    
    
for j in range(x):
    print(a[j])
    

