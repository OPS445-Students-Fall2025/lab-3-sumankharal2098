#!/usr/bin/env python3
# Author ID: 137379236

# initial list before function definitions
my_list = [1, 2, 3, 4, 5]

def add_item_to_list(ordered_list):
    # append last item + 1 (modify in place)
    last = ordered_list[-1]
    ordered_list.append(last + 1)

def remove_items_from_list(ordered_list, items_to_remove):
    # remove all occurrences of values listed in items_to_remove
    for item in items_to_remove:
        while item in ordered_list:
            ordered_list.remove(item)

if __name__ == '__main__':
    print(my_list)
    add_item_to_list(my_list)
    add_item_to_list(my_list)
    add_item_to_list(my_list)
    print(my_list)
    remove_items_from_list(my_list, [1, 5, 6])
    print(my_list)
