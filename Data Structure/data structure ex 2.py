list = [34, 54, 67, 89, 11, 43, 94]
print("Original list: ",list)
list1 = list.pop(4)
print("List after removing element at index 4: ",list)
list[2] = list1
print("List after adding element at index 2: ",list)
list.append(list1)
print("List after adding element at last: ",list)