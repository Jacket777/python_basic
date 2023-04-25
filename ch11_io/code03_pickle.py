#测试序列化与反序列化
import pickle

#序列化
def test01():
    # 序列化
    with open(r"data.data", "wb") as f:
        a1 = "Jack"
        a2 = 234
        a3 = [20, 30, 40]

        pickle.dump(a1, f)
        pickle.dump(a2, f)
        pickle.dump(a3, f)
    # 反序列化
    with open(r"data.data", "rb") as f:
        b1 = pickle.load(f)
        b2 = pickle.load(f)
        b3 = pickle.load(f)
        print(b1)
        print(b2)
        print(b3)
        print(id(a1), id(b1))









