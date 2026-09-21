def reverse_sentence(sentence):
  sentence_array=sentence.split()
  p1=0
  p2=len(sentence_array)-1
  while p1 < p2: 
    swap_value= sentence_array[p2]
    sentence_array[p2]=sentence_array[p1]
    sentence_array[p1]=swap_value
    p1+=1
    p2-=1
  return " ".join(sentence_array)
  
print(reverse_sentence("hello"))
print(reverse_sentence(""))
print(reverse_sentence("one two"))
print(reverse_sentence("hello world python"))
print(reverse_sentence("  hello  world  "))

#Time Complexity : O(n) where n is the length of the string.
#Space Complexity : O(n) where n is the length of the string.