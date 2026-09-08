strs = ["flower", "flow", "flight"]


def longest_common_prefix(strs):
    prefix = ""

    for i in range(len(strs[0])):
        for j in range(len(strs)):
            if i >= len(strs[j]) or strs[j][i] != strs[0][i]:
                return prefix

        prefix += strs[0][i]

    return prefix


print(longest_common_prefix(strs))

# Time Complexity: O(n * m)
# n = number of strings
# m = length of the shortest string
# Space Complexity: O(m)
