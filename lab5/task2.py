def sort_list(data):
    # Sort numbers and strings separately, then combine
    numbers = sorted([x for x in data if isinstance(x, (int, float))])
    strings = sorted([x for x in data if isinstance(x, str)])
    return numbers + strings

items = [3, "apple", 1, "banana", 2]
sorted_items = sort_list(items)
print(sorted_items)