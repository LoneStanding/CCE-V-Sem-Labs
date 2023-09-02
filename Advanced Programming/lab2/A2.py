def find_union(list1, list2):
    union = list1[:]
    for item in list2:
        if item not in union:
            union.append(item)
    return union


def find_intersection(list1, list2):
    intersection = []
    for item in list1:
        if item in list2:
            intersection.append(item)
    return intersection


def find_difference(list1, list2):
    difference = []
    for item in list1:
        if item not in list2:
            difference.append(item)
    return difference


list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

union = find_union(list1, list2)
intersection = find_intersection(list1, list2)
difference = find_difference(list1, list2)

print("List 1:", list1)
print("List 2:", list2)
print("Union:", union)
print("Intersection:", intersection)
print("Difference (List 1 - List 2):", difference)
