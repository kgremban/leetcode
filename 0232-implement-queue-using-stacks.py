from collections import deque

class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = deque()

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        temp = deque()
        while self.queue:
            temp.appendleft(self.queue.popleft())

        self.queue.appendleft(x)

        while temp:
            self.queue.appendleft(temp.popleft())

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        return self.queue.popleft()       

    def peek(self) -> int:
        """
        Get the front element.
        """
        if len(self.queue) == 0:
            return None

        return self.queue[0]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.queue) == 0

def main():

    # Your MyQueue object will be instantiated and called as such:
    obj = MyQueue()
    obj.push(1)
    obj.push(2)
    obj.push(3)

    param_2 = obj.peek()
    param_3 = obj.pop()
    param_4 = obj.empty()

    print(param_2, param_3, param_4)

if __name__ == "__main__":
    main()