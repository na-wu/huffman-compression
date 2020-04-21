class Node:
    
  def __init__(self, char, freq):
    self.char = char
    self.freq = freq
  
  def incrementFreq(self):
    self.freq += 1