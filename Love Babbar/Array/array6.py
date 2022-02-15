# Find the Union and Intersection of the two sorted arrays.

def unionAndIntersection(arr1, arr2):
    set1 = set(arr1)
    set2 = set(arr2)

    inter = sorted(list(set1.intersection(set2)))
    union = sorted(list(set1.union(set2)))

    print("Intersection:", inter)
    print("Union:", union)

unionAndIntersection([85, 25, 1, 32, 54, 6], [85, 2])
