a=[5,1,4,3,2,7,8,0,9]
def HeapSort(m_list):
  def heapify(i, n, arr):
    #make difult index for largest 
    largest=i
    #child left
    left=2*i+1
    #child right
    right=2*i+2
    #make sure from the left is lesser then n even doesn't make error
    # if the child left is lesser then its parent, use left value index to be
    #largest
    if left < n and arr[left] > arr[largest]:
      largest=left
    #and same in the right
    if right < n and arr[right] > arr[largest]:
      largest=right

    if largest != i:
      #make swap to get maxheap
      arr[i], arr[largest]=arr[largest], arr[i]
      #recurseive the operation again
      heapify(i, largest, arr)

  n=len(m_list)
  #build completed binary
  #by get parent first
  for i in range(n//2-1,-1,-1):
    heapify(i, n, m_list)
  #use for loop on the arr with up side down
  for i in range(n-1, 0, -1):
    #the root will be upper value, so it will be moved to the end of the arr
    m_list[i], m_list[0]=m_list[0], m_list[i]
    #reapete the operation again by using heapify func
    heapify(0, i, m_list)
  return m_list

print(HeapSort(a))
