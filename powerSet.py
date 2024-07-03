from itertools import combinations

a=['orange', 'red', 'green', 'blue']

def powerSet2(m_list:list):
  if len(m_list)==0:
    return [[]]
  else:
    res=[]
    for x in powerSet2(m_list[1:]):
      res+=[x,x+[m_list[0]]]
    return res
print(powerSet2(a))

print("="*50)

def powerSet(m_list:list):
  res=[]
  for i in range(len(m_list)+1):
    c0mpinationres=combinations(m_list, i)
    res.extend(c0mpinationres)
  return res

print(powerSet(a))