"""
Priority Queue
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
duyệt queue
"""


def getReturn(queue, array):
    if queue == None:
        return
    array.append(queue.value)
    getReturn(queue.next, array)


# ==========================================================================================
"""
tìm kiếm node trong queue
"""


def findWithID(queue, value):
    if queue == None:
        return None
    if queue.value["IDCode"] == value:
        return queue.value
    return findWithID(queue.next, value)


# ==========================================================================================
"""
xóa node đầu tiên của queue
"""


def removeHead(queue):
    if queue == None:
        return None
    return queue.next


# ==========================================================================================
"""
check IDCode
"""


def checkID(value1, value2):
    return value1["IDCode"] == value2["IDCode"]


# ==========================================================================================
"""
sortQueue: sắp xếp queue theo thứ tự ưu tiên
"""


def sortQueue(queue):
    if queue == None:
        return
    if checkQueue(queue):
        temp = queue.value
        queue.value = queue.next.value
        queue.next.value = temp
    sortQueue(queue.next)


# ==========================================================================================
"""
checkQueue: kiểm tra kiểm tra xem queue có đúng thứ tự ưu tiên hay không
"""


def checkQueue(queue):
    if queue == None or queue.next == None:
        return False
    if (
        queue.value["disease"]["prioritized"]
        > queue.next.value["disease"]["prioritized"]
    ):
        return True
    checkQueue(queue.next)


# ==========================================================================================
"""
remove node
"""


def removeNode(queue, value):
    if queue.next == None:
        return
    if checkID(queue.next.value, value):
        queue.next = queue.next.next
        return
    removeNode(queue.next, value)


# ==========================================================================================
"""
add node vào cuối queue
"""


def addNode(queue, value):
    if queue == None:
        return node(value)
    else:
        queue.next = addNode(queue.next, value)
        while checkQueue(queue):
            sortQueue(queue)
    return queue


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
        if self.queue == None:
            self.queue = newNode
            return
        addNode(self.queue, value)

    # ==========================================================================================
    """
    dequeue: xóa node đầu tiên của queue
    """

    def dequeue(self):
        temp = self.queue.value  # type: ignore
        self.queue = self.queue.next  # type: ignore
        return temp

    # ==========================================================================================
    """
    remove: xóa node trong queue
    """

    def remove(self, value):
        if (self.queue.value["IDCode"], value):  # type: ignore
            self.queue = self.queue.next  # type: ignore
            return
        removeNode(self.queue, value)

    # ==========================================================================================
    """
    find: tìm kiếm node trong queue
    """

    def find(self, value):
        return findWithID(self.queue, value)

    # ==========================================================================================
    """
    return: trả về mảng các node trong queue
    """

    def Return(self):
        Array = []
        getReturn(self.queue, Array)
        return Array
