for i in range(len(num_array)):
    if target - num_array[i] in seen:
        return [i, seen[target - num_array[i]]]

    seen[num_array[i]] = i


#Time: O(n) average
#Space: O(n)