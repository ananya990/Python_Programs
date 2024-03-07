my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
chunk_size = 2

list_chunked = [my_list[i:i + chunk_size] for i in range(0, len(my_list), chunk_size)]

print(list_chunked)
