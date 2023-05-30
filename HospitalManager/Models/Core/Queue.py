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
xoa node đầu tiên của queue
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
remove node
"""
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
        while not self.queue == None:
            if(checkID(self.queue.value, value)):
                temp = self.queue.value
                self.queue = self.queue.next
                return temp
            self.queue = self.queue.next
        return None
# ==========================================================================================
    """
    return: trả về mảng các node trong queue
    """
    def Return(self):
        Array = []
        getReturn(self.queue, Array)
        return Array