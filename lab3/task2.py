def bubble_sort(arr):
    """
    Sorts a list of numbers in ascending order using the bubble sort algorithm.
    """
    n = len(arr)
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap if the element found is greater than the next element
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Example usage:
if __name__ == "__main__":
    numbers = [64, 34, 25, 12, 22, 11, 90]
    print("Original list:", numbers)
    bubble_sort(numbers)
    print("Sorted list:", numbers)
