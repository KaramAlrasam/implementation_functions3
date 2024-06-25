def commen_items(m_list:list)->list:
  return list(set.intersection(*map(set, m_list)))

def intersection(*m_list:set):
  if len(m_list)<=1:
    return m_list
  
  res=m_list[0]
  for i in range(len(m_list[1:])):
    res&=m_list[i]
  return res
 
a=[[12, 18, 23, 25, 45], [7, 12, 18, 24, 28], [1, 5, 8, 12, 15, 16, 18]]

print(intersection({12, 18, 23, 25, 45}, {7, 12, 18, 24, 28}, {1, 5, 8, 12, 15, 16, 18}))