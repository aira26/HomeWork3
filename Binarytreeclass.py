class TreeNode:
    def __init__(self,key,val,left=None,right=None,parent=None):
        self.key = key
        self.payload = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent

    def hasLeftChild(self):
        return self.leftChild

    def hasRightChild(self):
        return self.rightChild

    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self

    def isRightChild(self):
        return self.parent and self.parent.rightChild == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.rightChild or self.leftChild)

    def hasAnyChildren(self):
        return self.rightChild or self.leftChild

    def hasBothChildren(self):
        return self.rightChild and self.leftChild

    def findmin(self):
        current = self
        while current.hasLeftChild():
            current = current.leftChild
        return current

    def findmax(self):
        current = self
        while current.hasRightChild():
            current = current.rightChild
        return current


class BinarySearchTree:

    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def put(self,key,val):
        if self.root:
            self._put(key,val,self.root)
        else:
            self.root = TreeNode(key,val)
        self.size = self.size + 1

    def _put(self,key,val,currentNode):
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                   self._put(key,val,currentNode.leftChild)
            else:
                   currentNode.leftChild = TreeNode(key,val,parent=currentNode)
        else:
            if currentNode.hasRightChild():
                   self._put(key,val,currentNode.rightChild)
            else:
                   currentNode.rightChild = TreeNode(key,val,parent=currentNode)

    def __setitem__(self,k,v):
       self.put(k,v)

    def get(self,key):
       if self.root:
           res = self._get(key,self.root)
           if res:
                  return res.payload
           else:
                  return None
       else:
           return None

    def _get(self,key,currentNode):
       if not currentNode:
           return None
       elif currentNode.key == key:
           return currentNode
       elif key < currentNode.key:
           return self._get(key,currentNode.leftChild)
       else:
           return self._get(key,currentNode.rightChild)

    def __getitem__(self,key):
       return self.get(key)

    def __contains__(self,key):
       if self._get(key,self.root):
           return True
       else:
           return False


    def get_max(self):
      current = self.root
      while current.hasRightChild():
          current = current.rightChild
      return current

    def get_min(self):
      current = self.root
      while current.hasLeftChild():
          current = current.leftChild
      return current



mytree = BinarySearchTree()
mytree[3]="red"
mytree[4]="blue"
mytree[6]="yellow"
mytree[2]="at"

print(mytree[6])
print(mytree[2])
import random
import matplotlib.pyplot as plt
for r in range(100):
    num = random.randint(0,1000)
    my_min = mytree.get_min()
    my_max = mytree.get_max()

import time
def measure_time(a, this_list):
    tot_time_add = 0
    tot_time_min = 0
    tot_time_max = 0

    for num in this_list:
        start = time.time()
        a.put("",num)
        tot_time_add += (time.time() - start)

        start = time.time()
        min = a.get_min()
        tot_time_min += (time.time() - start)

        start = time.time()
        max = a.get_max()
        tot_time_max += (time.time() - start)

    return tot_time_add, tot_time_min, tot_time_max

if __name__ == '__main__':
    m = BinarySearchTree()
    m.put("",5)
    print(m.get_min(), m.get_max())
    m.put("",7)
    print(m.get_min(), m.get_max())
    m.put("",3)
    print(m.get_min(), m.get_max())
    m.put("",9)
    print(m.get_min(), m.get_max())

    repetitions = 3
    max_operations = 500
    step= 100

    values_bubble, values_bubble_min, values_bubble_max = [], [], []
    for rounds in range(step, max_operations, step):
        this_list = []
        for r in range(rounds):
            this_list.append(random.randint(0, 500))

        tot_time_add, tot_time_min, tot_time_max = 0, 0, 0
        for repetition in range(5):
            a = BinarySearchTree()
            my_add, my_min, my_max = measure_time(a, this_list)
            tot_time_add += my_add
            tot_time_min += my_min
            tot_time_max += my_max

        tot_time_add /= 5
        tot_time_min /= 5
        tot_time_max /= 5

        values_bubble.append(tot_time_add * 1000)
        values_bubble_min.append(tot_time_min * 1000)
        values_bubble_max.append(tot_time_max * 1000)

    xlabels = range(step, max_operations, step)
    plt.plot(xlabels, values_bubble, label='Add')
    plt.plot(xlabels, values_bubble_min, label='Get Min')
    plt.plot(xlabels, values_bubble_max, label='Get Max')
    plt.legend()
    plt.xlabel("Number of Operations")
    plt.ylabel("Execution time (msec)")
    plt.title("Performance of binary tree's Solution")
    plt.show()
