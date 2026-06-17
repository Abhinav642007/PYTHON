#selection sort is a simple sorting algorithm that repeatedly selects the smallest (or largest) element from the unsorted portion of the list and moves it to the end of the sorted portion. The algorithm maintains two subarrays in a given array: one that is already sorted and one that is unsorted. Initially, the sorted subarray is empty and the unsorted subarray is the entire input array. The algorithm proceeds by finding the smallest (or largest) element in the unsorted subarray, swapping it with the leftmost unsorted element (putting it in sorted order), and moving the subarray boundaries one element to the right.
def selection_sort(arr):
    n=len(arr)
    for i in range(n):
        min_idx=i
        for j in range(i+1, n):
            if arr[j]<arr[min_idx]:
                min_idx=j
        arr[i], arr[min_idx]=arr[min_idx], arr[i]
    return arr

arr=[64, 25, 12, 22, 11]
print("Unsorted array:", arr)
sorted_arr=selection_sort(arr)
print("Sorted array:", sorted_arr)