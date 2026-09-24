numb_1=int(input('введите первое число'))
numb_2=int(input('введите второе число'))
res=0
op=input('введите операцию')
while numb_2!=0:
    if op=='+':
        res=numb_1+numb_2
        print(res)
    elif op=='-':
        res=numb_1-numb_2
        print(res)
    elif op=='*' and numb_2==0:
        print('на ноль делить нельзя')
    elif op=='/':
        res=numb_1/numb_2
        print(res)
    elif op=='^':
        res=numb_1**numb_2
        print(res)
    elif op=='*' and numb_2!=0:
        res=numb_1*numb_2
        print(res)
    else:
        print('такой операции не существует')
    break

