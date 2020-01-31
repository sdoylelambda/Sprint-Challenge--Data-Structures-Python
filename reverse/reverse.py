class Node:
  def __init__(self, value=None, next_node=None):
    # the value at this linked list node
    self.value = value
    # reference to the next node in the list
    self.next_node = next_node

  def get_value(self):
    return self.value

  def get_next(self):
    return self.next_node

  def set_next(self, new_next):
    # set this node's next_node reference to the passed in node
    self.next_node = new_next

class LinkedList:
  def __init__(self):
    # reference to the head of the list
    self.head = None

  def add_to_head(self, value):
    node = Node(value)
    if self.head is not None:
      node.set_next(self.head)
    
    self.head = node

  def contains(self, value):
    if not self.head:
      return False
    # get a reference to the node we're currently at; update this as we traverse the list
    current = self.head
    # check to see if we're at a valid node 
    while current:
      # return True if the current value we're looking at matches our target value
      if current.get_value() == value:
        return True
      # update our current node to the current node's next node
      current = current.get_next()
    # if we've gotten here, then the target node isn't in our list
    return False

  def reverse_list(self):
    # 3 pointers: prev as null, curr as head and next as null - Next, current, previous, current
    prev = None
    current = self.head
    while current: # Time Complexity: O(n) -- just while loop every thing else is constant
      # Before moving next, store it
      next_node = current.next_node
      # Move next
      current.next_node = prev
      # Reverse happens here
      prev = current
      # Move current
      current = next_node
    self.head = prev





























    # TO BE COMPLETED
    # if len(self.value) == 0:
    #   return self.value
    # else:
    #   print(self.head)
      # return reverse_list(self.value)

  # def reverse(self.head):
  #   if len(self.head) == 0:
  #     return string
  #   else:
  #     print(string)
  #     return reverse(string[1:]) + string[0]