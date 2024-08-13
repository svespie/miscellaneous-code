def is_sorted_ascending(set):
    if len(set) < 2:
        return True
    if len(set) == 2:
        if set[0] < set[1]:
            return True
        return False
    for i in range(1,len(set)-2):
        if set[i] < set[i-1] or set[i] > set[i+1]:
            return False
    return True

def is_sorted_descending(set):
    if len(set) < 2:
        return True
    if len(set) == 2:
        if set[0] > set[1]:
            return True
        return False
    for i in range(1,len(set)-2):
        if set[i] > set[i-1] or set[i] < set[i+1]:
            return False
    return True

def selection_sort_ascending(set):
    s = set.copy()
    if not is_sorted_ascending(s):
        for i in range(len(s)-1):
            min_index = i
            for j in range(i+1, len(s)):
                if s[min_index] > s[j]:
                    min_index = j
            s[i], s[min_index] = s[min_index], s[i]
    return s