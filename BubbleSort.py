a=[1,5,2,8,3,9,7,8,6,4]
def BubbleSort(m_list):
  length=len(m_list)
  while length!=0:
    for i in range(length-1):
      if m_list[i]>m_list[i+1]:
        m_list[i],m_list[i+1]=m_list[i+1],m_list[i]
    length-=1
  return m_list

print(BubbleSort(a))