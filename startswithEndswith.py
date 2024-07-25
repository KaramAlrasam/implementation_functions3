word="karam.py"
def m_endswith(m_str:str, par:str):
  length=len(m_str)
  par_len=len(par)
  start_p=par_len-length
 
  return par[start_p:]==m_str

print(m_endswith(".py", word))


def m_startswith(word:str, m_str:str):
  length=len(m_str)
  print(word[:length])
  return word[:length]==m_str

print(m_startswith(word, "ka"))
