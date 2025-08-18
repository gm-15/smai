if __name__ == '__main__':
    num1 = int(input("num1을 입력하세요"))
    print(num1)
    num2 = int(input("num2을 입력하세요"))
    print(num2)
    num3 = int(input("num2을 입력하세요"))
    print(num3)

    min, max, result = 100000, -11, 0
    arr = [num1, num2, num3]

    for i in range(3):
        if min>arr[i]:
            min = arr[i]
        if max<arr[i]:
            max = arr[i]

    print(f'num1은 {num1} num2는 {num2} num3는 {num3} 최솟값은 {min} 최댓값은 {max}입니다.')

