class Point():

    def __init__(self, x, y, z):
        self.assign(x, y, z)

    def assign (self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def printPoint (self):
        print(self.x, self.y, self.z)

    def __add__ (self, other):
        x = self.x + other.x
        y = self.y + other.y
        z = self.z + other.z

        return Point(x, y, z)

    def __str__(self):
        return ("({0},{1},{2})".format(self.x, self.y, self.z))


def main():
    p1 = Point (1, 2, 4)
    p2 = Point (4, 5, 6)

    # print(p1+p2)
    print (Point.__add__(p1,p2))

if __name__ == "__main__":
    main()