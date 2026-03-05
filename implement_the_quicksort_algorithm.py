** start of main.py **

def quick_sort(lst):
    if len(lst) <= 1:
        return lst
    
    pivot = lst[0]
    less = [x for x in lst[1:] if x < pivot]
    equal = [x for x in lst[1:] if x == pivot]
    greater = [x for x in lst[1:] if x > pivot]
    
    return quick_sort(less) + [pivot] + equal + quick_sort(greater)

** end of main.py **

