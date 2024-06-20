from collections import Counter
def most_occurrences_number(m_list:list):
  itemsValues=Counter(m_list)
  return list(itemsValues)[0]
a=[1, 3, 1, 4, 7, 9, 8, 2, 6, 5, 1, 6, 1, 2, 3, 4, 6, 9, 1, 2]

print(most_occurrences_number(a))

def most_occurrences_number2(m_list:list):
  #make variable has zero value
  occur=0
  #make aother variable has value of first element in the m_list
  res=m_list[0]
  #make for loop on the m_list and count occur element and update res
  for i in m_list:
    #count i by using count function
    newItem=m_list.count(i)
    if newItem>occur:
      occur=newItem
      res=i
  return res

print(most_occurrences_number2(a))