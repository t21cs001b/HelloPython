'''
Created on 2023/10/13

@author: t21cs001
'''
def quick_sort(data):
    if len(data) <= 1:
        return data
    pivot = data.pop(0)
    
    left = [i for i in data if i<= pivot]
    
    right = [i for i in data if i > pivot]
    
    left  = quick_sort(left)
    right = quick_sort(right)
    
    return left + [pivot] + right