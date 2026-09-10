def fin_min_max(num_arr):
  minimum=num_arr[0]
  maximum=num_arr[0]
  for num in num_arr:
    if(num<minimum):
      minimum=num
    if(num>maximum):
      maximum=num
  return [minimum,maximum]

print(fin_min_max([7, 2, 9, 4, 1, 6]))
print(fin_min_max([-5, -2, -10, -1]))
print(fin_min_max([5]))
print(fin_min_max([-3, -2, -8]
))
print(fin_min_max([1, 1, 1]))



