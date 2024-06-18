a=[1, 1, 3, 4, 4, 5, 6, 7]
b=[0, 1, 2, 3, 4, 4, 5, 7, 8]


def Average_of_two_lists(a_list:list, b_list:list)->float:
  """It is in charge to return Average number of two lists"""
  res=[(a+b)/2 for a, b in zip(a_list, b_list)]
  return sum(res)/len(res)

print(Average_of_two_lists(a,b))
def average_two_lists(nums1, nums2):
  # Calculate the average by summing the elements of both lists and dividing by their combined length
  result = sum(nums1 + nums2) / len(nums1 + nums2)
  return result

print(average_two_lists(a,b))