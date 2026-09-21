def vowel_consonant_count(string):
  vowels = ["a", "e", "i", "o", "u"]
  vowel_count=0
  consonant_count=0
  for char in string:
    if char.lower() in vowels:
        vowel_count += 1
    elif(char.isalpha()):
        consonant_count += 1
  return vowel_count, consonant_count

print(vowel_consonant_count("hello"))
print(vowel_consonant_count("Hello World! 123"))
print(vowel_consonant_count("AEIOU"))
print(vowel_consonant_count("bcdfg"))
print(vowel_consonant_count("123!@#"))
print(vowel_consonant_count(""))
print(vowel_consonant_count("aeiou123xyz!"))

#Time Complexity : O(n) where n is the length of the string.
#Space Complexity : O(1)
