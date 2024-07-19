def into_str(n, base):
  m_chr="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

  if n==0:
    return ""
    
  reminder=n%base
  redu=n//base

  return into_str(redu,base)+m_chr[reminder]
print(into_str(2,16))
print(hex(2))
