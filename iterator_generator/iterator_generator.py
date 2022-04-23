x = iter([1, 2, 3, 4])

x.__next__()

print(x)
print(type(x))

print(list(x))

class Revrange:

    def __init__(self,n):
        self.n = n
        self.i = n


    def __iter__(self):
        return(self)


    def __next__(self):
        if self.n >= 0 :
            if self.i == self.n:
                self.n = self.n - 1
                return self.i

            else:
                self.i = self.n
                self.n = self.n - 1
                return self.i

        else:
            raise StopIteration


for temp in Revrange(5):
        print(temp)




### --------------------------   generator   --------------------------------##


def revrange(n):
    while n >= 0 :
        yield n
        n = n - 1


for tempo in revrange(5):
    print(tempo)