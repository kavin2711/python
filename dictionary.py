def find_value_in_dict(data_dict, target_key):
    if target_key in data_dict:
        print(f"The value for '{target_key}' is: {data_dict[target_key]}")
    else:
        print(f"Key '{target_key}' not found in the dictionary.")

# Example usage:
my_dict = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

user_key = input("Enter key to search for: ")
find_value_in_dict(my_dict, user_key)
