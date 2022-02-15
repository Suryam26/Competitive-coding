# Find the maximum and minimum element in an array

def maxmin(arr):
    max_element = arr[0]
    min_element = arr[0]

    for i in arr:
        if i > max_element:
            max_element = i
        if i < min_element:
            min_element = i

    print ("MIN:", min_element)
    print ("MAX:", max_element)
    
maxmin([1,2,3,4,5,6,7])