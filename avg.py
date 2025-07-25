students = {}

while True:
    name = input("Enter name (or type 'done' to finish): ")
    if name.lower() == "done":
        break
    mark = float(input("Enter mark: "))
    if name in students:
        students[name].append(mark)
    else:
        students[name] = [mark]

search_name = input("Enter name to get average marks: ")
if search_name in students:
    avg = sum(students[search_name]) / len(students[search_name])
    print(f"Average marks for {search_name}: {avg}")
else:
    print("Name not found.")


