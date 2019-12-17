from typing import List

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minStack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

        if self.minStack == []:
            self.minStack.append(x)
        else:
            if x <= self.minStack[-1]:
                self.minStack.append(x)
            else:
                self.minStack.append(self.minStack[-1])

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]

def main():

    obj = MinStack()
    obj.push(-2)
    obj.push(0)
    obj.push(-3)
    obj.pop()
    print(obj.top())
    print(obj.getMin())

if __name__ == "__main__":
    main()


