def count_occurrences(l, target):
    count = 0
    for item in l:
        if item == target:
            count += 1
    return count

my_list = [1, 2, 3, 4, 2, 5, 2, 6, 2]

target_item = 2

freq = count_occurrences(my_list, target_item)

print(f"The item {target_item} occurs {freq} times in the list.")
