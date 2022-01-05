class A():

    # def method01(self, i=None):
    #     if i is None:
    #         print("Sequence 01")

    #     else:
    #         print ("Sequence 02")

    def method01(self, i=None, j=1):
        if i is None and j ==1:
            print("Sequence 03")

        elif j == 3:
            print ("Sequence 04")

        else:
            print ("Sequence 05")

def main():
    obj1= A()
    obj1.method01()
    obj1.method01(5)
    obj1.method01(5,3)

if __name__ == "__main__":
    main()