class A():
    
    def m(self):
        print('This is m() from Class A.')

class B(A):
    def m(self):
        print('This is m() from Class B.')
        super().m()

class C(A):
    def m(self):
        print('This is m() from Class C.')
        super().m()

class D(B, C):
    def m(self):
        print ('This is m() from Class D.')
        super().m()


def main():
    x = D()
    x.m()

if __name__ == "__main__":
    main()