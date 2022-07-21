def sum(x,y):
    result={}
    result['s']=x['s']*y['m'] + y['s']*x['m']
    result['m']=x['m']*y['m']
    return result

def sub(x,y):
    result={}
    result['s']=x['s']*y['m'] - y['s']*x['m']
    result['m']=x['m']*y['m']
    return result

def mult(x,y):
    result={}
    result['s']= x['s']*y['s']
    result['m']= x['m']*y['m']
    return result

def div(x,y):
    result={}
    result['s']= x['s']*y['m']
    result['m']= x['m']*y['s']
    return result

def show(x):
    print(x['s'],'/',x['m'])

def show_menu():
    print('1_ Sum')
    print('2_ Subtract')
    print('3_ Multiple')
    print('4_ Divide')
    print('5_ Exit')


show_menu()
choice=input("Select an option: ")
Surat1=int(input("Enter first fraction numerator: "))
Makh1=int(input("Enter first denominator: "))

Surat2=int(input("Enter second fraction numerator: "))
Makh2=int(input("Enter second denominator: "))

a={'s':Surat1, 'm':Makh1}
b={'s':Surat2,'m':Makh2}

if choice==1:
    C=sum(a,b)
    show(C)
elif choice==2:
    D=sub(a,b)
    show(D)
elif choice==3:
    E=mult(a,b)
    show(E)
elif choice==4:
    F=div(a,b)
    show(F)
elif choice==5:
    pass