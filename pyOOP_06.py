from abc import ABC, abstractmethod

class Animal():
    
    @abstractmethod
    def move(self):
        pass

class Human (Animal):
    def move(self):
        print('I Walk')

class Snake (Animal):
    def move(self):
        print('I Crawl')

def main():
    a = Human()
    b = Snake()
    a.move()
    b.move()

if __name__ == "__main__":
    main()