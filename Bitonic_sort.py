def Bitonic_sort(m_list,up=True)->list:
  def Bitonic_merge(m_list, up):
    if len(m_list)<=1:
      return m_list
    else:
      mid=len(m_list)//2
      for j in range(mid):
        if (m_list[j] > m_list[j+mid]) == up:
          m_list[j], m_list[j+mid]=m_list[j+mid], m_list[j]
      left=Bitonic_merge(m_list[:mid], up)
      right=Bitonic_merge(m_list[mid:], up)
      return left+right
  if len(m_list)<=1:
    return m_list
  else:
    mid=len(m_list)//2
    increasing=Bitonic_sort(m_list[:mid], True)
    Decreasing=Bitonic_sort(m_list[mid:], False)
    return Bitonic_merge(increasing+Decreasing, up)
  

a=[3,1,2,5,6,0,7,8,9,22,12,5,3,44,56,78]
print(Bitonic_sort(a,True))
