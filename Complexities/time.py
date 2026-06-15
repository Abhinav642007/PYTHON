#understanding time complexity
#time complexity is a measure of how the runtime of an algorithm changes as the size of the input increases. It is often expressed using Big O notation, which describes the upper bound of the runtime in terms of the input size.

arr=[1,2,3,4,5]
# del arr[0] #O(n) because we have to shift all the elements to the left after deleting the first element
# print(arr)

arr.insert(3,6) 
# O(n) because we have to shift all the elements to the right after inserting an element in the middle
print(arr)

arr.append(7)
# O(1) because we are adding an element to the end of the list, which does not require shifting any elements
print(arr)

arr.pop(2)
# O(n) because we have to shift all the elements to the left after removing an element
print(arr)

arr.remove(4)
# O(n) because we have to search for the element to remove and then shift all the   elements to the left after removing it
print(arr)

ab=arr.index(5)
# O(n) because we have to search for the element in the list
print(ab)

a=arr.count(2)
# O(n) because we have to search for the element in the list and count its occurrences
print(a)

arr1=1 in arr
# O(n) because we have to search for the element in the list
print(arr1)

