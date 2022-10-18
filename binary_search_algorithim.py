# binary search is a divide and concor algorithim that allows one to search through a list faster




def binary_search(numbers_list,target, low = None, high = None):
    if low == None:
        low = 0
    if high == None:
        high = len(numbers_list) - 1
    if high < low:
        return -1

    midpoint = (low + high) // 2

    if numbers_list[midpoint] == target:
        return midpoint

    elif target < numbers_list[midpoint]:
        return binary_search(numbers_list, target, low , midpoint -1)

    else:
        return binary_search(numbers_list, target, midpoint + 1, high )


if __name__ == "__main__":
   numbers_list = [40,1,2,6,10,16]
   numbers_list.sort()
   target = 1
   print(binary_search(numbers_list, target))

# def naive_search(numbers, target):
#  for i in range(len(numbers)):
#         if numbers[i] == target:
#             return i
#  return -1

# # print(naive_search(numbers, target))


# def binary_search (numbers, target, low = None, high = None):
#     if low is None:
#         low = 0
#     if high is None:
#         high = len(numbers) - 1

#     if high < low:
#         return -1

#     midpoint = (low + high) // 2

#     if numbers[midpoint] == target:
#         return midpoint

#     elif target < numbers[midpoint]:
#         return binary_search(numbers, target, low, midpoint - 1)
#     else:
#         return binary_search(numbers, target,midpoint + 1, high)



# if __name__ == "__main__":
#     numbers = [40,1,2,6,10,16]
#     numbers.sort()
#     target = 10
#     print(naive_search(numbers,target))
#     print(binary_search(numbers, target)

#




