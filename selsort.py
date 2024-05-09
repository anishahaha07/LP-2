def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr

def print_menu():
    print("\nMenu:")
    print("1. Sort Array")
    print("2. Exit")

# Example usage:
arr = []

while True:
    print_menu()
    choice = input("Enter your choice: ")

    if choice == '1':
        arr = list(map(int, input("Enter the array elements separated by space: ").split()))
        sorted_arr = selection_sort(arr)
        print("Sorted array:", sorted_arr)
    elif choice == '2':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please enter a valid option.")
