import heapq

def ugly_num(primes, n):
  uRes=[1]
  seen=set()
  ugly=None
  for _ in range(n):
    ugly=heapq.heappop(uRes)
    for prime in primes:
      new_ugly= ugly * prime
      if new_ugly not in seen:
        seen.add(new_ugly)
        heapq.heappush(uRes, new_ugly)
  return ugly
    
  
    
    
par=[2,7,13,19]
print(ugly_num(par, 12))

