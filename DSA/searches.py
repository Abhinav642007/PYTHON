#LINEAR SEARCH
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            print(f"Element found at index {i}")
            return i
    print("Element not found")
    return -1

arr=[1, 2, 3, 4, 5]
target=3
linear_search(arr, target)

#binary search
def binary_search(arr1, target1):
    left, right = 0, len(arr1) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target1:
            print(f"Element found at index {mid}")
            return mid
        elif arr1[mid] < target1:
            left = mid + 1
        else:
            right = mid - 1
    print("Element not found")
    return -1
arr1=[1, 2, 3, 4, 5]
target1=4
binary_search(arr1, target1)
