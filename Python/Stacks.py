class Stack:
    NumOfStacks = 0

    def __init__ (self):
        self.items = []
        Stack.NumOfStacks += 1

    def pop(self):
        poppeditem = self.items[-1]
        del(self.items[-1])
        return poppeditem

    def push(self, *item):
        self.items.append(item)

    def peak(self):
        if len(self.items) == 0:
            return 'empty'
        else:
            return self.items[-1]

    def isEmpty(self):
        if len(self.items) == 0:
            return True 
        else:
            return False

    def size(self):
        return len(self.items) 
    
    def showAll(self):
        return self.items
    
    def showOne(self, n):
        if len(self.items) <= (n):
            return 'empty'
        else:
            return self.items[n]
        
    @staticmethod
    def NumOfStacks():
        return Stack.NumOfStacks 

