# arr = 1,2,3,4,5,6,7
#target = 9

# # brute Force
# arr = list(map(int,input().strip().split()))
# target = int(input())
# count = 0 
# for i in range(len(arr)):
#     diff = arr[i] - target
#     for j in range(i+1,len(arr)):
#         if diff == arr[j] :
#             print(i,j)       # its a position of two elements whose sum equal to target one.
#             count += 1      # This will count total elements whose sum equal ot target.
# print(count)

# time O(n^2)
#sapce O(1)


# Optimzed
# using dictionary in python.
def two_sum(arr,target):
    hashmap = dict()
    pos_ls = []
    for i in range(len(arr)):
        diff = target - arr[i]
        if diff not in hashmap:
            hashmap[arr[i]] = i
        else:    # if we get diff in hashmap then it return list of positions.
            pos_ls += [i,hashmap[diff]]
            return pos_ls
    return pos_ls     # loop through over all values in a given arr and we did not get two_summ == target then it returns an empty position list.     
   
arr = 1,2,3,4,5,6,7
target = 9
print(two_sum(arr,target))

# time complexity O(n)
# space complexity O(n)