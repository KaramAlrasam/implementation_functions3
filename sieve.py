color1 =[[2], [0], [1, 3], [0, 7], [9, 11], [13, 15, 17]]

def sieve(m_list:list, a:int, b:int)->list:
  """It is in charge to get rid of sublist which out of range"""
  return [i for i in m_list if min(i)>=a and max(i)<=b]

print(sieve(color1,13,17))