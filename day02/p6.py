#pickle 형식으로 저장하기. 내 파이썬 타입으로 저장하고 가져올 수 있다.
import pickle

if __name__ == '__main__':
    sts = [
        {'name':'이말숙', 'age':21, 'major':'sw'},
        {'name':'김말숙', 'age':22, 'major':'sw'},
        {'name':'박말숙', 'age':23, 'major':'sw'},
        {'name':'홍말숙', 'age':24, 'major':'sw'}
    ]

    pickle.dump(sts, open('data/sts.pkl','wb'))
    result = pickle.load(open('data/sts.pkl','rb'))
    print(type(result))
    print(result)