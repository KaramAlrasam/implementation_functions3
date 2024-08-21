def shell_sort(m_list):
  #element "B"
  def insertionSort(start, m_list, gap):
    for i in range(start+gap, len(m_list), gap):
      temp= m_list[i]
      position=i
      while position >= gap and (m_list[position-gap]>temp):
        m_list[position]=m_list[position-gap]
        position-=gap
      
      m_list[position]=temp

  #element "A"  
  subListCount=len(m_list)//2
  while subListCount > 0:
    for i in range(subListCount):
      insertionSort(i, m_list, subListCount)
    subListCount//=2
  return m_list
  
a = [9, 8, 3, 7, 5, 6, 4, 1]

print(shell_sort(a))#[1, 3, 4, 5, 6, 7, 8, 9]
