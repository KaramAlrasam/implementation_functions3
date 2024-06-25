def count_element(item, m_list:list)->int:
  """It is in charge to count element in the m_list"""
  def flatting_list(m_list:list)->list:
    if not m_list:
      return
    res=[]
    

    stack= [list(m_list)]
    while stack:
      c_num=stack.pop()
      next=c_num.pop()
      if c_num:
        stack.append(c_num)
      if isinstance(next,list):
        if next:
          stack.append(next)
      else:
        res.append(next)
    return res
  n_list=flatting_list(m_list)
  return n_list.count(item)
a=[[['A', 'B'], ['A', 'C']], [['A', 'D', 'E'], ['B', 'C', 'D']]]
print(count_element("E",a))

Define a function 'count_element_in_list' that counts the occurrences of element 'x' in 'input_list'
def count_element_in_list(input_list, x):
    ctr = 0
    for i in range(len(input_list)):
        if x in input_list[i]:
            ctr += 1
    return ctr

# Create a list 'list1' containing sublists of elements
list1 = [[[1, 3], [5, 7]], [[1, 11], [1, 15, 7]]]

# Print a message indicating the original list
print("Original list:")
# Print the contents of 'list1'
print(list1)

# Print a message indicating the count of the element '1' in the list
print("\nCount 1 in the said list:")
# Call the 'count_element_in_list' function with 'list1' and the element '1', then print the result
print(count_element_in_list(list1, 1))

# Print a message indicating the count of the element '7' in the list
print("\nCount 7 in the said list:")
# Call the 'count_element_in_list' function with 'list1' and the element '7', then print the result
print(count_element_in_list(list1, 7))

# Create a list 'list1' containing sublists of characters
list1 = [['A', 'B'], ['A', 'C'], ['A', 'D', 'E'], ['B', 'C', 'D']]

# Print a message indicating the original list
print("\nOriginal list:")
# Print the contents of 'list1'
print(list1)

# Print a message indicating the count of the character 'A' in the list
print("\nCount 'A' in the said list:")
# Call the 'count_element_in_list' function with 'list1' and the character 'A', then print the result
print(count_element_in_list(list1, 'A'))

# Print a message indicating the count of the character 'E' in the list
print("\nCount 'E' in the said list:")
# Call the 'count_element_in_list' function with 'list1' and the character 'E', then print the result
print(count_element_in_list(list1, 'E'))

