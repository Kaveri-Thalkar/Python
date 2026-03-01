def selection_sort(array):
    length = len(array)
       
    for i in range(length - 1):
        minIndex = i
           
        for j in range(i + 1, length):
            if array[j] < array[minIndex]:
                minIndex = j
                   
        # Swap the found minimum element with first element
        array[i], array[minIndex] = array[minIndex], array[i]
             
    return array


# Define array outside the function
array = [21, 6, 9, 33, 3]

print("The sorted array is:", selection_sort(array))