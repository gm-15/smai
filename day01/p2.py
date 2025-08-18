a = 10
b = 10.1
c = 'a'
d = "'aaa'"
e = True
ff = 0
num1 = "100"
num2 = "200"
result = num1+num2

if __name__ == '__main__':
    print(f'num1은 {num1} num2는 {num2} 결과는 {result}')
    print(f'결과는{d}')
    print(type(b))
    print(type(a))
    print('결과값:%d 이고 %.3f'%(a,b))
    print(f'결과는 {a}{b}{e}입니다.')