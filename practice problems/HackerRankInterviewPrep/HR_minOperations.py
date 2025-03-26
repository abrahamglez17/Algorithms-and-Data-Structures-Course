def min_operations_to_zero(arr):
    n = len(arr)
    operations = 0
    prev = 0  # Keeps track of the previous value after operations

    for i in range(n):
        diff = arr[i] - prev
        if diff != 0:
            operations += abs(diff)
            prev = arr[i]  # This becomes the new "prefix state"

    return operations


print(min_operations_to_zero([3, 2, 0, 0, -1]))  # 5
print(min_operations_to_zero([-1, -1, -1, -1]))  # 1
print(min_operations_to_zero([5, 3, 2, 0, 0, -1]))  # 5
print(min_operations_to_zero([0, 0, 0]))  # 0
print(min_operations_to_zero([1, -1, 1, -1]))  # 4
