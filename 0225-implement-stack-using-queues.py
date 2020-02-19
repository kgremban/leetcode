from collections import deque

class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = deque()
        

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        temp = deque()
        temp.append(x)
        while self.queue:
            temp.append(self.queue.popleft())

        self.queue = temp

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.queue.popleft()

    def top(self) -> int:
        """
        Get the top element.
        """
        if len(self.queue) > 0:
            return self.queue[0]

        else:
            return 0

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.queue) == 0

def main():
    obj = MyStack()
    obj.push(2)
    param_2 = obj.pop()
    param_3 = obj.top()
    param_4 = obj.empty()

    print("Results:\n\n")
    print("param_2: {}", param_2)
    print("param_3: {}", param_3)
    print("param_4: {}", param_4)

if __name__ == "__main__":
    main()