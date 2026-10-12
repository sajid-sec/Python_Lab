# Write a function remove_last(lst) that removes the last element of a list. Call this function with a list and check whether the original list changes outside the function. 
def remove_last(lst):
    lst.pop()

country = ["Japan", "China", "India", "Russia", "Germany"]
print("Original list:", country)
remove_last(country)
print("List after removing last element:", country)