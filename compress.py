import sys
import node as huffman_node
import minheap
import json


def createFTable(filein, fileout):
  table = dict()
  with open(str(filein),'r') as file:
    f = file.readlines()[0]
    for char in f:
      if char in table:
        node = table[char]
        node.incrementFreq()
      else:
        node = huffman_node.Node(char, 1)
        table[char] = node
  with open(str(fileout), 'w') as fileout:
      fileout.writelines(table)

    

# table = createFTable()
# nodes = table.values()
# print(table)

# for i in table:
#   print(i.char, i.freq)

# freqList = sorted([node for node in table.values()])
# print(freqList[0])

if __name__ == "__main__":
    print(f"Arguments count: {len(sys.argv)}")
    if len(sys.argv) != 2:
        raise ValueError("Usage: 'python compress.py [file_in] [file_out]")
    createFTable(sys.argv[1], sys.argv[2])