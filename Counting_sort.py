def counting_sort(m_list):
  def duild_countong_array(m_list):
    max_array=max(m_list)+1
    Boxes=[0]*max_array

    for i in m_list:
      Boxes[i]+=1

    for i in range(1, len(m_list)):
      Boxes[i]+=Boxes[i-1]
    return Boxes

  def helperCountingSort(C_Array, m_list):
    SortedList=[0]*len(m_list)
    for i in reversed(m_list):
      C_Array[i]-=1
      SortedList[C_Array[i]]=i
    return SortedList

  C_Array=duild_countong_array(m_list)
  return helperCountingSort(C_Array, m_list)
  
a=[9,7,6,0,1,5,2,4,3,8]
print("Unsorted Array: ",a)
print("Sorted Array: ",counting_sort(a))
print("="*50)

#######################################

def counting_sort(array1):
  max_n=max(array1)+1
  C_array=[0]*(max_n)

  for i in array1:
    C_array[i]+=1

  i=0
  for a in range(max_n):
    for _ in range(C_array[a]):
      array1[i]=a
      i+=1
  return array1
b=[1, 2, 7, 3, 2, 5000, 4, 2, 3, 2, 5]  
print("Unsorted Array: ",b)
print("Sorted Array: ",counting_sort(b))


    
