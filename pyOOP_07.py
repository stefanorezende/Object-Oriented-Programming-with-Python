class A():

    def __init__(self):
        self.a = "Public"
        self._b = "Internal Use"
        self.__c = "Name Mangling in action"

def main():
    x = A()
    print (x.a)
    print (x._b)
    print (x._A__c) #se print(x.__c) -> erro nenhum objeto atribuido.

if __name__ == "__main__":
    main()