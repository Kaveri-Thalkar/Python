def binary_search(list1, n):
    low = 0
    high = len(list1) - 1

    while low <= high:
        # Get middle index
        mid = (high + low) // 2

        # Check if n is present at mid
        if list1[mid] < n:
            low = mid + 1

        # If n is smaller, search left side
        elif list1[mid] > n:
            high = mid - 1

        # If element is found
        else:
            return mid

    # Element was not present
    return -1


# Initial list
list1 = [12, 24, 32, 39, 45, 50, 54]
n = 45

# Function call
result = binary_search(list1, n)

if result != -1:
    print("Element is present at index", result)
else:
    print("Element is not present in list1")