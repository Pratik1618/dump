og_list = [1, 2, 3, 4, 5]
copied_list1 = og_list.copy()
copied_list2 = og_list[:]
copied_list3 = list(og_list)
print("Original list:", og_list)
print("Copied list (copy method):", copied_list1)
print("Copied list (slicing):", copied_list2)
print("Copied list (list constructor):", copied_list3)