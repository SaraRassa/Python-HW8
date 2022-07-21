def menu():
    print('1_ sum')
    print('2_ sub')
    print('3_ multiple')
    print('4_ divide')
    print('5_ exit')

def sum(x,y):
    result={}
    result['R']= x['R'] + y['R']
    result['I']= x['I'] + y ['I']
    return result

def sub(x,y):
    result={}
    result['R']= x['R'] - y['R']
    result['I']= x['I'] - y ['I']
    return result

def mult(x,y):
    result={}
    result['R']= x['R']*y['R'] - x['I']*y['I']
    result['I']= x['I']*y['R'] + x['R']*y['I']
    return result

def div(x,y):
    result={}
    result['R']= (x['R']*y['R'] + x['I']*y['I']) / (y['R']**2 + y['I']**2)
    result['I']= (x['I']*y['R'] - x['R']*y['I']) / (y['R']**2 + y['I']**2)
    return result

def show(x):
    print('C=',x['R'],'+',x['I'],'i')
    

while True:
    menu()
    choice=int(input("Select an option: "))

    if choice==5:
        exit()
    else:
        r1=float(input("Real1: "))
        i1=float(input("Imag1: "))
        r2=float(input("Real2: "))
        i2=float(input("Imag2: "))
        a={'R':r1,'I':i1}
        b={'R':r2,'I':i2}
        
        if choice==1:
            s=sum(a,b)
            show(s)
        elif choice==2:
            u=sub(a,b)
            show(u)
        elif choice==3:
            m=mult(a,b)
            show(m)
        elif choice==4:
            d=div(a,b)
            show(d)