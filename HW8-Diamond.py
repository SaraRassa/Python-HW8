Rows=int(input('Enter number of rows: '))
n=Rows-1
d=1

for i in range(n):
    for j in range(n-i):
        print(' ',end='')
    for k in range(d):
        print('*', end='')
    d += 2
    print()
for i in range(n+1):
    for j in range(i):
        print(" ", end='')
    for k in range(d):
        print('*', end='')
    d -= 2
    print()