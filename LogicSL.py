def loc(a):
    lt = []
    for i in a:
        if i == "(":
            lt.append(-1)
        else:
            lt.append(1)
    total = -1
    ele = 0
    cc=lt[1:]
    while(ele < len(cc) and total != 0):
        total = total + cc[ele]
        ele += 1
    return int((ele+1)/2)
    
    

'''
cc = '(((avb)&d)>c)&f'

par_cc=[]
for y in cc:
    if y=="(" or y==")":
        par_cc.append(y)
'''

def main(x):
    if x[0]!='(':
        return x[1]
    else:   
        a=[]
        for y in x:
            if y=="(" or y==")":
                a.append(y)
        ini_str = x
        sub_str = ")"
        occurrence = loc(a)
        val = -1
        for i in range(0, occurrence):
            val = ini_str.find(sub_str, val + 1)
        return x[val+1]


print(main('(((avb)&d)>c)&f'))
print(main('avb'))
print(main('(a&b)>((cvd)&f)'))
print(main('a&((cvd)&f)'))
print(main('((avb)&(d&e))>(c&f)'))
print(main('((avb)&((d&e)&(bvk)))>(c&f)'))


def subf(x):
    c=[]
    if x[0]!='(':
        c.append(x[0])
    else:
        a=[]
        for y in x:
            if y=="(" or y==")":
                a.append(y)
        ini_str = x
        sub_str = ")"
        occurrence = loc(a)
        val = -1
        for i in range(0, occurrence):
            val = ini_str.find(sub_str, val + 1)
        e=val
        f=x[1:e]
        c.append(f)
    if x[-1:]!=')':
        c.append(x[-1:])
    else:
        a=[]
        for y in x:
            if y=="(" or y==")":
                a.append(y)
        ini_str = x
        sub_str = ")"
        occurrence = loc(a)
        val = -1
        for i in range(0, occurrence):
            val = ini_str.find(sub_str, val + 1)
        e=val+3
        f=x[e:-1]
        c.append(f)
    return c


print(subf('(((avb)&d)>c)&f'))
print(subf('((avb)&((d&e)&(bvk)))>(c&f)'))


def allsub(x):
    a=[]
    for i in x:
        if i=='v' or i=='&' or i=='>' or i=='=':
            a.append(i)
    b=len(a)+1
    d=1
    hh=subf(x)
    while d<b:
        print(hh)
        hh=subf(hh[0])
        d=d+1


print(allsub('(((avb)&d)>c)&f'))
