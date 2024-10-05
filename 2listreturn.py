List1 = [25, 34, 57, 90]
List2 = [12, 56, 78, 90, 34, 57]
common_elements = False
for item1 in List1:
    for item2 in List2:
        if item1 == item2:
            common_elements = True
            break 
if common_elements:
 print("True")
else:
 print("False")
