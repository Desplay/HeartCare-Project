"""
heap Tree
"""

"""
tạo object node
"""
class node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        


"""
trả về node có giá trị lớn nhất
"""
def maxValue(root):
    max = root.value
    while(root.right != None):
        root = root.right
        max = root.value
    return max


"""
duyệt cây theo thứ tự NLR
"""
def RNL(root, Array):
    if(root == None):
        return
    RNL(root.right)
    Array.append(root.value)
    RNL(root.left)


"""
Kiểm tra IDCode doctor đầu vào có đúng với IDCode doctor của node không
"""
def checkID(value, IDCode):
    return value.IDCode == IDCode


"""
duyệt cây theo thứ tự NRL
"""
def NRL(root, Array, valueID):
    if(root != None):
        if(checkID(root.value, valueID)):
            Array.append(root.value)
        NRL(root.right, Array, valueID)
        NRL(root.left, Array, valueID)


"""
tạo thuật toán MaxHeap (cây nhị phân) với các phương thức enqueue, dequeue, find
"""
class MaxHeap:
    """
    Tạo heap với root là None
    """
    def __init__(self):
        self.root = None
    """
    function enqueue: thêm node vào cây
    """
    def enqueue(self, value):
        newNode = node(value)
        if(self.root == None):
            self.root = newNode
            return self
        current = self.root
        """
        addSide: thêm node vào cây theo thứ tự ưu tiên
        """
        def addSide(side):
            if(current[side] == None):
                current[side] = newNode
                return self
            current = current[side]
        while True:
            if(value == current.value):
                current.count += 1
                return self
            if(value.disease.prioritized > current.value.disease.prioritized):
                addSide('left')
            elif(value.disease.prioritized == current.value.disease.prioritized):
                addSide('right')
            else:
                addSide('right')
    """
    Return: trả về mảng các node trong cây
    """
    def Return(self):
        Array = []
        RNL(self.root, Array)
        return Array
    """
    find: tìm kiếm node theo IDCode
    """
    def find(self, valueID):
        data = self.Return()
        for i in data:
            if(i.IDCode == valueID):
                return i
    """
    remove: xóa node theo IDCode
    """
    def remove(self, valueID):
        if(self.find(valueID) != None):
            data = []
            temp = self.find(valueID)
            NRL(self.root, data, valueID)
            self.root = None
            for i in data:
                if(i.IDCode != valueID):
                    self.enqueue(i)
        return temp
    """
    dequeue: xóa node có giá trị lớn nhất
    """
    def dequeue(self):
        self.remove(maxValue(self.root).IDCode)