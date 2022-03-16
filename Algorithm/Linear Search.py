#Linear Search Function
# Runtime Complexity: O(N)
# Space Complexity: O(1)
def linear_search(arr,n,item):
    for i in range(0,n):
        if(arr[i]==item):
            return i
    return -1
# Main code
arr = [2,5,8,7,8,3,6]
n = len(arr)
item = int(input("Search Item: "))
index = linear_search(arr,n,item)
if (index==-1):
    print("Item Not Found")
else:
    print("Item found at index:",index)