
def dichotomy(list1,target):
    length = len(list1)
    index_low = 0
    index_high = length - 1
 
    while index_low <= index_high:
        index_midle = int((index_low + index_high) / 2)
        guess = list1[index_midle]
        if guess == target:
            return index_midle
        elif guess > target:
            index_high = index_midle - 1
        elif guess < target:
            index_low = index_midle + 1
    return None
