a=[1,2,3,4,5,6,7,8,9]
def calulate(m_list):
  def helperC(res, m_list):
    if not m_list:
      return res
    return res+helperC(m_list[0],m_list[1:] )
    
  
  if len(m_list)==0:
    return 0
  else:
    res=0
    return helperC(res, m_list)
print(calulate(a))

###################################

a=[1,2,3,4,5,6,7,8,9]
def m_sum(m_list:list):
  if len(m_list)==1:
    return m_list[0]
  else:
    return m_list[0]+m_sum(m_list[1:])

print(m_sum(a))