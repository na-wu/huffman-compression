class MinHeap:

  # Min Heap Class designed specifically for a Huffman Node
  # Features Peek and getMin 
  # Self maintaining Min Heap
  def __init__(self):
    self.items = []
    self.size = 0
  
  # Int --> Int
  def getLeftChildIndex(self, parentIndex):
    return (2 * parentIndex) + 1

  def getRightChildIndex(self, parentIndex):
    return (2 * parentIndex) + 2
  
  def getParentIndex(self, childIndex):
    return (childIndex - 1) // 2
  
  # Int --> Node
  def getLeftChild(self, index):
    return self.items[self.getLeftChildIndex(index)]

  def getRightChild(self, index):
    return self.items[self.getRightChildIndex(index)]

  def getParent(self, index):
    return self.items[self.getParentIndex(index)]
  
  # Int --> Boolean
  def hasLeftChild(self, index):
    return self.getLeftChildIndex(index) < self.size
  
  def hasRightChild(self, index):
    return self.getRightChildIndex(index) < self.size

  def hasParent(self, index):
    return self.getParentIndex(index) >= 0

  
  def swap(self, index1, index2):
    temp = self.items[index1]
    self.items[index1] = self.items[index2]
    self.items[index2] = temp

  def peek(self):
    if not self.items:
      return "Empty"
    else:
      return self.items[0]

  def getMin(self):
    if self.size == 0:
      raise ValueError
      
    minNode = self.items[0]
    lastItem = self.items[self.size - 1]
    self.items[0] = lastItem
    self.size -= 1
    self.heapifyDown()
    return minNode

  def addNode(self, node):
    self.items.append(node)
    self.size += 1
    self.heapifyUp()

  def heapifyDown(self):
    index = 0

    while self.hasLeftChild(index):
      indexOfSmallerChild = self.getLeftChildIndex(index)
      
      if self.hasRightChild(index) and self.getRightChild(index).freq < self.getLeftChild(index).freq:
        indexOfSmallerChild = self.getRightChildIndex(index)

      if self.items[index].freq > self.items[indexOfSmallerChild].freq:
        self.swap(index, indexOfSmallerChild)

      else: 
        break # Stop immediately when heap property is restored
      index = indexOfSmallerChild

  def heapifyUp(self):
    index = self.size - 1

    while self.hasParent(index) and self.getParent(index).freq > self.items[index].freq:
      self.swap(self.getParentIndex(index), index)
      index = self.getParentIndex(index)