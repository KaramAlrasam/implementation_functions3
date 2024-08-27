def Radics_sort(m_list)->list:
  """Radics sort is the quickest algorithm to sort element"""
  
  def _get_digit(m_list)->int:
    m=max(m_list)
    return len(str(m))

  def main_helper(digit, m_list):
    for d in range(digit):
      matrics=[[]for _ in range(10)]
      for item in m_list:
        ind=item//10**d%10
        matrics[ind].append(item)
      m_list=flatting(matrics)
    return m_list
  
  def flatting(m_list):
    from functools import reduce
    return reduce(lambda x, y: x+y, m_list)

  A=_get_digit(m_list)
  return main_helper(A, m_list)


a=[1,7,2,9,0,3,7,8]
print(Radics_sort(a))
