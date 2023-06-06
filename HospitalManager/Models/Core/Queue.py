"""
Normal Queue
"""
# ==========================================================================================
"""
tạo object node
"""
class node:
    def __init__(self, value):
        self.value = value
        self.next = None
# ==========================================================================================
"""
add node vào cuối queue
"""
def addNode(queue, value):
    if(queue == None):
        return node(value)
    else:
        queue.next = addNode(queue.next, value)
    return queue
# ==========================================================================================
"""
duyệt queue
"""
def getReturn(queue, array):
    if(queue == None):
        return
    array.append(queue.value)
    getReturn(queue.next, array)
# ==========================================================================================
"""
xóa node đầu tiên của queue
"""
def removeHead(queue):
    if(queue == None):
        return None
    return queue.next
# ==========================================================================================
"""
check IDCode
"""
def checkID(value1, value2):
    return value1['IDCode'] == value2['IDCode']
# ==========================================================================================
"""
tạo thuật toán Queue với các phương thức enqueue, dequeue, find
"""
class Queue:
    """
    tạo queue
    """
    def __init__(self):
        self.queue = None
# ==========================================================================================
    """
    enqueue: thêm node vào cuối queue
    """
    def enqueue(self, value):
        newNode = node(value)
        if(self.queue == None):
            self.queue = newNode
            return
        addNode(self.queue, value)
# ==========================================================================================
    """
    dequeue: xóa node đầu tiên của queue
    """
    def dequeue(self):
        temp = self.queue.value # type: ignore
        self.queue = self.queue.next # type: ignore
        return temp
# ==========================================================================================
    """
    dequeue: xóa node đầu tiên của queue
    """
    def getLength(self):
        temp = self.queue
        count = 0
        while(temp != None):
            count += 1
            temp = temp.next
        return count
# ==========================================================================================
    """
    remove: xóa node trong queue
    """
    def remove(self, value):
        prev = None
        current = self.queue
        while not current is None:
            if(checkID(current.value, value)):
                break
            prev = current
            current = current.next
        if current is None:
            return
        if prev is None: # type: ignore
            self.queue = current.next # type: ignore
        prev.next = current.next # type: ignore
        if prev.next is None: # type: ignore
            self.queue = None
# ==========================================================================================
    """
    return: trả về mảng các node trong queue
    """
    def Return(self):
        Array = []
        getReturn(self.queue, Array)
        return Array