if __name__ == '__main__':
    #set
    t1 = {1,2,3,4,5}
    print(type(t1))
    print(t1)
    t1.add(6)
    t1.add(5)
    print(t1)

    #tuple
    t1 = (1,2,3,4,5)
    print(type(t1))
    print(t1)

    #dictionary
    d1 = {'a':1,'b':2,'c':3}
    print(type(d1))
    print(d1)

    d2 = {'name':'이말숙', 'age':21, 'major':'sw'}
    print(d2['name'])
    print(d2['age'])

    #응용
    sts = [
        {'name':'이말숙', 'age':21, 'major':'sw'},
        {'name': '김말숙', 'age': 22, 'major': 'sw'},
        {'name': '박말숙', 'age': 23, 'major': 'sw'},
        {'name':'홍말숙', 'age':24, 'major':'sw'}
    ]

    #sw 학과 학생들의 나이합과 평균 출력
    sum=0
    count=0
    for data in sts:
        if data['major']=='sw':
            sum += data['age']
            count = count +1
    print(f'결과 합은{sum} 평균은{sum/count}')



