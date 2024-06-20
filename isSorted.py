a=[2,3,8,4,7,9,8,2,6,5,1,6,1,2,3,4,6,9,1,2]

def issorted(m_list:list)->bool:
  if len(m_list)<=1:
    return
  return all(a<=b for a, b in zip(m_list[:-1], m_list[1:]))

def issorted2(m_list:list)->bool:
  return all(m_list[i]<=m_list[i+1]for i in range(len(m_list)-1))

print(issorted(a))
print(issorted2(a))

  