from math import floor
def sum(x,y):
    result={}
    result['h']=x['h']+y['h']
    result['m']=x['m']+y['m']
    result['s']=x['s']+y['s']
    if result['s'] >= 60:
        result['s'] -= 60
        result['m'] += 1
    if result['m'] >= 60:
        result['m'] -= 60
        result['h'] += 1
    return result

def sub(x,y):
    result={}
    result['h']=x['h']-y['h']
    result['m']=x['m']-y['m']
    result['s']=x['s']-y['s']
    if result['s'] < 0:
        result['s'] += 60
        result['m'] -= 1
    if result['m'] < 0:
        result['m'] += 60
        result['h'] -= 1
    return result

def time2sec(h,m,s):
    a=h*3600 + m*60 + s
    print('Total time1=',a,'seconds')
    
def sec2time(T):
    x={}
    x['h']=floor(T/3600)
    x['m']=floor((T-x['h']*3600) / 60)
    x['s']=T - x['h']*3600 - x['m']*60
    return x

def show(x):
    print(x['h'],':',x['m'],':',x['s'])

def show_menu():
    print('1_ Add times')
    print('2_ subtract times')
    print('3_ Convert time to seconds')
    print('4_ Convert seconds to time')

while True:
    show_menu()
    choice=int(input("Please select an option: "))
    if choice==4:
        t1=int(input("Enter number of seconds: "))
        t6=sec2time(t1)
        show(t6)
    elif choice==3:
        h=int(input('h: '))
        m=int(input('m: '))
        s=int(input('s: '))
        time2sec(h,m,s) 
        
    else:
        h1=int(input("Enter first time hour: "))
        m1=int(input("Enter first time minuts: "))
        s1=int(input("Enter first time seconds: "))
        h2=int(input("Enter second time hour: "))
        m2=int(input("Enter second time minuts: "))
        s2=int(input("Enter second time seconds: "))
        t1={'h':h1,'m':m1,'s':s1}
        t2={'h':h2,'m':m2,'s':s2}

        if choice==1:
            t3=sum(t1,t2)
            show(t3)
        elif choice==2:
            t4=sub(t1,t2)
            show(t4)   