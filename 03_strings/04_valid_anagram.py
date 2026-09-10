def is_anagram(s, t):
    seen_s = {}

    if len(s) != len(t):
        return False

    for char in s:
        if char in seen_s:
            seen_s[char] += 1
        else:
            seen_s[char] = 1

    for char in t:
        if char in seen_s and seen_s[char] != 0:
            seen_s[char] -= 1
        else:
            return False

    return True

#Time: O(n)
#Space: O(n) general case.