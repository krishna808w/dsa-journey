def union_intersection(array_a,array_b):
  pointer_1=0
  pointer_2=0
  union_array=[]
  inter_section_array=[]
  while pointer_1<len(array_a) and pointer_2<len(array_b):
    if(pointer_1!=0 and array_a[pointer_1-1] == array_a[pointer_1]):
      pointer_1+=1
      continue
    if(pointer_2!=0 and array_b[pointer_2-1] == array_b[pointer_2]):
      pointer_2+=1
      continue
    if(array_a[pointer_1]<array_b[pointer_2]):
      union_array.append(array_a[pointer_1])
      pointer_1+=1
    elif(array_b[pointer_2]<array_a[pointer_1]):
      union_array.append(array_b[pointer_2])
      pointer_2+=1
    elif(array_b[pointer_2] ==array_a[pointer_1]):
        union_array.append(array_b[pointer_2])
        inter_section_array.append(array_b[pointer_2])
        pointer_1+=1
        pointer_2+=1
  while pointer_1<len(array_a):
      if(array_a[pointer_1-1] == array_a[pointer_1]):
        pointer_1+=1
        continue
      union_array.append(array_a[pointer_1])
      pointer_1+=1

  while pointer_2<len(array_b):
      if(array_b[pointer_2-1] == array_b[pointer_2]):
        pointer_2+=1
        continue
      
      union_array.append(array_b[pointer_2])
      pointer_2+=1

  return [union_array,inter_section_array]
    

A = [1, 2, 4, 5,6,7,8]
B = [2, 3, 5, 6]
print(union_intersection(A,B))

A = [1, 1, 2]
B = [1, 2, 2]
print(union_intersection(A,B))

A = []
B = [1, 2, 3]
print(union_intersection(A,B))

A = [1, 2, 3]
B = []
print(union_intersection(A,B))

A = []
B = []
print(union_intersection(A,B))

#Time Complexity: O(min(m,n)) where m and n are the lengths of the two arrays.
#Space Complexity: O(m+n) in the worst case for storing the union and intersection arrays.