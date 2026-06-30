from typing import List


def reverse_list(arr: List[int]) -> List[int]:
    result = []
    n = len(arr)
    while n > 0:
        result.append(arr[n-1])
        n -= 1 
    return result

# do not modify below this line
print(reverse_list([1, 2, 3]))
print(reverse_list([3, 2, 1, 4, 6, 2]))
print(reverse_list([1, 9, 7, 3, 2, 1, 4, 6, 2]))
