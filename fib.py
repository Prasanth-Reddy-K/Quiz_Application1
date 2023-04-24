n= int(input())
def fib(n):
    c=0
    if(n<3):
        print(0,1,1)
    else:
        print(0,1, end= " ")
        a=0
        b=1
        while(c+3<=n):
            t= a+b
            print(t, end= " ")
            a=b
            b= t
            c+=1
fib(n)