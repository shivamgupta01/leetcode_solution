'''
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
Example:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.
'''


class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.prev_min = []
        self.head = len(self.stack) - 1
        self.min = None
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if self.min == None:
            self.min = x
            self.prev_min.append(None)
        else:
            if x < self.min:
                self.prev_min.append(self.min)
                self.min = x
            else:
                self.prev_min.append(self.min)


                
        self.stack.append(x)
        self.head = self.head+1

        

    def pop(self):
        """
        :rtype: void
        """
        if self.head > -1:
            del self.stack[-1]
            self.min = self.prev_min[-1]
            del self.prev_min[-1]
            self.head = self.head -1
    

    def top(self):
        """
        :rtype: int
        """
        if self.head != -1:
            return self.stack[self.head]

    def getMin(self):
        """
        :rtype: int
        """
        if self.min != None:
            return self.min
        


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
obj.push(-9)
obj.push(10)
obj.push(11)
obj.pop()
obj.pop()
obj.pop()
obj.pop()
obj.pop()
obj.pop()
print(obj.prev_min)
print(obj.stack)
print(obj.getMin())
