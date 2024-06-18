a=[4, 5, 8, 9, 6, 10]

# def test(m_list:list)->list:
#   """It is in charge to return list has difference between consecutive numbers"""
#   res=[]
  
#   for i in range(0,len(m_list)):
#     if i < len(m_list)-1:
#       res.append(m_list[i+1]-m_list[i])
#   return res

# print(test(a))#[0, 2, 1, 0, 1, 1, 1]
# print(test(a))#[1, 3, 1, -3, 4]

def  difference_between_consecutive_numbers(m_list:list)->list:
   """It is in charge to return list has difference between consecutive numbers"""
   res=[a-b for a, b in zip(m_list[1:],m_list[:-1])]
   return res

print(difference_between_consecutive_numbers(a))
  