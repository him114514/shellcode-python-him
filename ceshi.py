class nm:
    def __init__(self,ss):
        self.ss=ss
    def __call__(self,*aa,**a):
        self.ss.__call__(*aa,**a)
def js(a):
    print(a)

js=nm(js)
js(1112)



def a(func):    
    def nmsl(*j,**jj):
        func(*j,**jj)
    return nmsl

def nm(a):
    print(a)

nm=a(nm)

nm(99)


class LJ:
    def __init__(self, func):
        self.func = func
    def __get__(self,exp,owner):
        return self.func.__get__(exp,owner)

class e:
    @LJ
    def nm(self):
        print(111)

e=e()
e.nm()
