class CyclicIterator:
    def __init__(self, qty):
        self.qty = qty
        self.index = 0
    def __next__(self):
        if self.index >= len(self.qty):
            self.index = 0
        try:
            char = self.qty[self.index]
        except TypeError:
            self.qty = list(self.qty)
            char = self.qty[self.index]
        self.index += 1
        return char
    def __iter__(self):
        return self
    
my_list = [1, 2, 3, 4]
my_tuple = (1, 2, 3, 4,)
my_set = {1, 2, 3, 4, '2'}
my_frozenset = frozenset('qwer')
      
if __name__ == '__main__':
    cyclic_iterator = CyclicIterator(my_frozenset)
    for i in cyclic_iterator:
        print(i)