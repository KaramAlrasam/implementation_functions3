
list1= ['Red color', 'Orange#', 'Green', 'Orange @', 'White']
def getRidOfChar(m_list:list, chr_list)->list:
  #make empty list to colect the result
  res=[]
  #make for loop on the m_list
  for line in m_list:
    #make for loop on the splited line and get rid of each word which belongs to chr_list
    purWord="".join([word for word in line.split()if not any(phrase in word for phrase in chr_list)])
    res.append(purWord)
  return res
chr=['#', 'color', '@']
print(getRidOfChar(list1,chr))
  