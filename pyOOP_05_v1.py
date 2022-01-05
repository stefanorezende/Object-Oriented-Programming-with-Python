class A():
    
    def m(self):
        print('This is m() from Class A.')

class B():
    def m(self):
        print('This is m() from Class B.')

class C(B, A):
    pass

def main():
    x = C()
    x.m()

if __name__ == "__main__":
    main()