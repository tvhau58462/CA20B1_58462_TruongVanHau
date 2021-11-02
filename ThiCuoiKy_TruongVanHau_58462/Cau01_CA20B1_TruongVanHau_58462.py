"""
Đề thi 01
Date: 27/10/2021
Trương Văn Hậu

"""

def Cau1():
    def snt(n):
        """ Check số nguyên tố """
        f = True
        for j in range(2, n):
            if n % j == 0:
                f = False
                break
        return f
    def in_snt(a=30, b=100):
        print("Danh sách số nguyên tố: ")
        """ Kiểm tra số nguyên tố trong khoảng từ a đến b"""
        for i in range(a, b + 1):
            if snt(i):
                print(i, end="  ")
    #Thực thi số nguyên tố
    in_snt(30, 100)

if __name__ == '__main__':
    Cau1()