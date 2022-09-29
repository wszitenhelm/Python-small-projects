#  Author: Wiktoria Szitenhelm
#  Date: 4 March 2021
#  Assessment 1:  

import sys

class Full(Exception):
    pass


class Empty(Exception):
    pass

class MyLeakyStack():
    """Leaky stack implementation using a Python circular array."""
    def __init__(self, maxlen, capacity):
        self._maxlen = maxlen      
        self._capacity = capacity  
        self._storage = [None] * capacity
        self._first = 0
        self._last = 0

    def __len__(self):
        """Return the number of elements in the stack."""
        return (self._capacity + self._first - self._last) % self._capacity

    def push(self, element):
        """Add element to the top of the stack.
        Raise Full exception if the stack is full.
        Creating this function I re-used and modified variables names of valbuxvb's code
        https://stackoverflow.com/questions/48765572/leaky-stack-function
        """
        self._storage[self._first] = element
        self._first = (self._first + 1) % self._capacity
        if len(self) > self._maxlen:
            leaked = self._storage[self._last]
            self._storage[self._last] = None
            self._last = (self._last + 1) % self._capacity
            raise Full(f"Reached stack limit, forget element {leaked}")

    def pop(self):
        """Remove and return the element from the top of the stack.
        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty("Stack is empty")
        pop = self._storage[self._first - 1]
        self._storage[self._first - 1] = None
        self._first = (self._first - 1) % self._capacity
        return pop

    def is_empty(self):
        """Return True if the stack is empty."""
        return self._first == self._last

    def menu(self):
        """ Either end or change the maxlen of the inner array """
        if input("Enter 1 to exit or 2 to change the array size\n") == "2":
            new_maxlen = input("Enter a number for the new maxlen of the inner array:\n")  
            self._maxlen = int(new_maxlen)
            if input("Enter 1 to exit or 2 to rerun the script\n") == "2":
                while len(self) > self._maxlen:
                    S.pop()
                S.run()
        sys.exit()
        


    ####### don't edit between here and the comment below ########
    def run(self):
        for i in range(12):
            try:
                S.push(i)
                print("after push "+str(i), S._storage)
            except Exception as e:
                print(e, "\n after push "+str(i), S._storage)

        for i in range(6):
            try:
                a=S.pop()
                print("after pop "+str(a), S._storage)
            except Exception as e:
                print(e, S._storage)

        for i in range(5):
            try:
               S.push(i+100)
               print("after push " + str(i+100), S._storage)
            except Exception as e:
               print(e, S._storage)
        ###### don't edit the above lines - add anything below as you with
        S.menu()
      

#### don't add anything below here
if __name__ == '__main__':
    S = MyLeakyStack(5, 10)   # stack size should be 5 and the capacity of the array should be 10
    S.run()
    


