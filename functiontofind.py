def find_value_in_list(data_list, target_value):
    found = False
    for index, value in enumerate(data_list):
        if value == target_value:
            print(f"Value found at index: {index}")
            found = True
    if not found:
        print("Value not found in the list.")

# Example usage:
my_list = [10, 20, 30, 40, 20, 50]
user_value = int(input("Enter value to search for: "))
find_value_in_list(my_list, user_value)
