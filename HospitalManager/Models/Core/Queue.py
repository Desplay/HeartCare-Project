"""
Normal Queue
"""

"""
tạo object node
"""
class node:
    def __init__(self, value):
        self.value = value
        self.next = None


"""
add node vào cuối queue
"""
def addNode(queue, value):
    if(queue == None):
        return node(value)
    else:
        queue.next = addNode(queue.next, value)
    return queue


"""
duyệt queue
"""
def getReturn(queue, array):
    if(queue == None):
        return
    array.append(queue.value)
    getReturn(queue.next, array)


"""
xoa node đầu tiên của queue
"""
def removeHead(queue):
    if(queue == None):
        return None
    return queue.next


"""
check IDCode
"""
def checkID(value1, value2):
    return value1.IDCode == value2.IDCode


"""
remove node
"""
def removeNode(queue, value):
    if(queue.next == None):
        return
    if(checkID(queue.next.value, value)):
        queue.next = queue.next.next
        return;
    removeNode(queue.next, value)


"""
tạo thuật toán Queue với các phương thức enqueue, dequeue, find
"""
class Queue:
    """
    tạo queue
    """
    def __init__(self):
        self.queue = None
    """
    enqueue: thêm node vào cuối queue
    """
    def enqueue(self, value):
        newNode = node(value)
        if(self.queue == None):
            self.queue = newNode
            return
        addNode(self.queue, value)
    """
    dequeue: xóa node đầu tiên của queue
    """
    def dequeue(self):
        temp = self.queue.value
        self.queue = self.queue.next
        return temp
    """
    remove: xóa node trong queue
    """
    def remove(self, value):
        if(checkID(self.queue.value, value)):
            self.queue = self.queue.next
            return
        removeNode(self.queue, value)
    """
    return: trả về mảng các node trong queue
    """
    def Return(self):
        Array = []
        getReturn(self.queue, Array)
        return Array