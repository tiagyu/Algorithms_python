def merge_and_sort(arr1, arr2):
    merged_array = arr1 + arr2
    merged_array.sort()

    return merged_array


arr1 = [1, 3, 5]
arr2 = [2, 4, 6]
print(merge_and_sort(arr1, arr2))
