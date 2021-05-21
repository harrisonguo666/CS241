class Binary_Search_Tree:
  # TODO.I have provided the public method skeletons. You will need
  # to add private methods to support the recursive algorithms
  # discussed in class

  class __BST_Node:
    # TODO The Node class is private. You may add any attributes and
    # methods you need. Recall that attributes in an inner class 
    # must be public to be reachable from the the methods.

    def __init__(self, value):
      self.value = value
      self.height = 1
      self.right = None
      self.left = None
      # TODO complete Node initialization



  def __init__(self):
    self.__root = None
  
  def __height(self, subroot):
    if (subroot.left is not None) and (subroot.right is not None):
      subroot.height = max(subroot.left.height, subroot.right.height) + 1 
    elif (subroot.left is not None):
      subroot.height = subroot.left.height + 1 
    elif (subroot.right is not None): 
      subroot.height = subroot.right.height + 1
    else: subroot.height = 1
  

  def __balance(self, subroot):
    if subroot is None:
      return subroot 

    #left-heavy by 2
    elif self.__checkbalance(subroot) == -2:
      #left child is left-heavy by 1, rotate right
      if (self.__checkbalance(subroot.left) == -1) or (self.__checkbalance(subroot.left) == 0):
          subroot = self.__rotateright(subroot)
      #left child is right-heavy by 1 
      elif self.__checkbalance(subroot.left) == 1: 
          #first rotation, rotate left around left child
          subroot.left = self.__rotateleft(subroot.left)
          #second rotation, rotate right 
          subroot = self.__rotateright(subroot)

    #right-heavy by 2
    elif self.__checkbalance(subroot) == 2:
      #right child is right-heavy by 1, rotate left
      if (self.__checkbalance(subroot.right) == 1) or (self.__checkbalance(subroot.right) == 0):
          subroot = self.__rotateleft(subroot)
      #right child is left-heavy by 1 
      elif self.__checkbalance(subroot.right) == -1:
          #first rotation, rotate right around right child
          subroot.right = self.__rotateright(subroot.right)
          #second rotation, rotate left
          subroot = self.__rotateleft(subroot)

    return subroot

  def __checkbalance(self, subroot):
    if (subroot.left is None) and subroot.right is None:
      return 0
    elif subroot.left is None:
      return subroot.right.height
    elif subroot.right is None:
      return 0 - subroot.left.height
    else:
      return subroot.right.height - subroot.left.height


  def __rotateleft(self, subroot):
    a = subroot.right.left 
    b = subroot 
    subroot = subroot.right
    subroot.left = b
    subroot.left.right = a
    self.__height(subroot)
    self.__height(subroot.left)
    return subroot
  
  def __rotateright(self, subroot):
    x = subroot.left.right
    y = subroot
    subroot = subroot.left
    subroot.right = y
    subroot.right.left = x
    self.__height(subroot)
    self.__height(subroot.right)
    return subroot

    # TODO complete initialization
  def __rinsert(self, value, subroot):
    if subroot is None:
      subroot = self.__BST_Node(value)
    elif subroot.value == value:
      raise ValueError
    elif value < subroot.value:
      subroot.left = self.__rinsert(value, subroot.left)
    elif value > subroot.value:
      subroot.right = self.__rinsert(value, subroot.right)
    #check balance & height
    subroot = self.__balance(subroot)
    self.__height(subroot)
    
    return subroot



  def insert_element(self, value):
    # Insert the value specified into the tree at the correct
    # location based on "less is left; greater is right" binary
    # search tree ordering. If the value is already contained in
    # the tree, raise a ValueError. Your solution must be recursive.
    # This will involve the introduction of additional private
    # methods to support the recursion control variable.
    self.__root = self.__rinsert(value, self.__root)


  def __rremove(self, value, subroot):
    if subroot is None:
      raise ValueError
    elif value == subroot.value:
      # two children
      if (subroot.left is not None) and (subroot.right is not None):
        original = subroot.right
        while original.left is not None:
          original = original.left
        m = original.value
        subroot.value = m
        subroot.right = self.__rremove(m, subroot.right)
      # one and zero child
      elif subroot.left is None:
        subroot = subroot.right
      else:
        subroot = subroot.left
    elif value < subroot.value:
      subroot.left = self.__rremove(value, subroot.left)
      # change the height 
    elif value > subroot.value:
      subroot.right = self.__rremove(value, subroot.right)

    # check balance & height
    subroot = self.__balance(subroot)
    if subroot is not None: self.__height(subroot)

    return subroot
     
  def remove_element(self, value):
    # Remove the value specified from the tree, raising a ValueError
    # if the value isn't found. When a replacement value is necessary,
    # select the minimum value to the from the right as this element's
    # replacement. Take note of when to move a node reference and when
    # to replace the value in a node instead. It is not necessary to
    # return the value (though it would reasonable to do so in some 
    # implementations). Your solution must be recursive. 
    # This will involve the introduction of additional private
    # methods to support the recursion control variable.
    self.__root = self.__rremove(value, self.__root)
  
  def __rto_list(self, parent):
    to_list = []
    if parent is None:
      return to_list
      
    if parent.left is not None:
      to_list.extend(self.__rto_list(parent.left))

    to_list.append(parent.value)

    if parent.right is not None:
      to_list.extend(self.__rto_list(parent.right))

    return to_list


  def to_list(self):
    return self.__rto_list(self.__root)

  def __rinorder(self, parent):
    in_order_string = ''
    if parent is None:
      return ''
    if parent.left is not None:
      in_order_string += self.__rinorder(parent.left) + ','
    else: 
      in_order_string += self.__rinorder(parent.left)
    in_order_string += ' ' + str(parent.value)
    if parent.right is not None:
      in_order_string += ',' + self.__rinorder(parent.right)
    else:
      in_order_string += self.__rinorder(parent.right)
    return in_order_string
    
  def in_order(self):
    # Construct and return a string representing the in-order
    # traversal of the tree. Empty trees should be printed as [ ].
    # Trees with one value should be printed as [ 4 ]. Trees with more
    # than one value should be printed as [ 4, 7 ]. Note the spacing.
    # Your solution must be recursive. This will involve the introduction
    # of additional private methods to support the recursion control 
    # variable.
    in_order_string = '['
    in_order_string += self.__rinorder(self.__root)
    in_order_string += ' ]'
    return in_order_string

  def __rpreorder(self, parent):
    pre_order_string = ''
    if parent is None:
      return ''
    pre_order_string += ' ' + str(parent.value)
    if parent.left is not None:
      pre_order_string += ',' + self.__rpreorder(parent.left)
    else: 
      pre_order_string += self.__rpreorder(parent.left)
    if parent.right is not None:
      pre_order_string += ',' + self.__rpreorder(parent.right)
    else:
      pre_order_string += self.__rpreorder(parent.right)
    return pre_order_string

  def pre_order(self):
    # Construct and return a string representing the pre-order
    # traversal of the tree. Empty trees should be printed as [ ].
    # Trees with one value should be printed in as [ 4 ]. Trees with
    # more than one value should be printed as [ 4, 7 ]. Note the spacing.
    # Your solution must be recursive. This will involve the introduction
    # of additional private methods to support the recursion control 
    # variable.
    pre_order_string = '['
    pre_order_string += self.__rpreorder(self.__root)
    pre_order_string += ' ]'
    return pre_order_string

  def __rpostorder(self, parent):
    post_order_string = ''
    if parent is None:
      return ''
    if parent.left is not None:
      post_order_string += self.__rpostorder(parent.left) + ','
    else: 
      post_order_string += self.__rpostorder(parent.left)
    if parent.right is not None:
      post_order_string += self.__rpostorder(parent.right) + ','
    else:
      post_order_string += self.__rpostorder(parent.right)
    post_order_string += ' ' + str(parent.value)
    return post_order_string


  def post_order(self):
    # Construct an return a string representing the post-order
    # traversal of the tree. Empty trees should be printed as [ ].
    # Trees with one value should be printed in as [ 4 ]. Trees with
    # more than one value should be printed as [ 4, 7 ]. Note the spacing.
    # Your solution must be recursive. This will involve the introduction
    # of additional private methods to support the recursion control 
    # variable.
    post_order_string = '['
    post_order_string += self.__rpostorder(self.__root)
    post_order_string += ' ]'
    return post_order_string

  def get_height(self):
    # return an integer that represents the height of the tree.
    # assume that an empty tree has height 0 and a tree with one
    # node has height 1. This method must operate in constant time.
    if self.__root is None:
      return 0
    else: return self.__root.height

  def __str__(self):
    return self.in_order()

if __name__ == '__main__':
  pass #unit tests make the main section unnecessary.

