def binarySearch(nums, target):

    nums.sort()
    
    right = len(nums) - 1
    left = 0
        

    if len(nums) == 1 or nums[0] == target:
        return True
        

    while(left <= right):
        if right >= left:
            mid = left + (right-left) //2 #half it

            if nums[mid] == target:
                return True
            elif nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1            
                        
    return False
    
def searchInsert(nums, target):

    nums.sort()
    
    right = len(nums) - 1
    left = 0
        

    while(left <= right):
        if right >= left:
            mid = left + (right-left) //2 #half it

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1            
                        
    return left


def searchRotatedArray(nums, target):
    pass 

nums = [4,5,6,7,0,1,2]

val = binarySearch(nums, 1)
print(val)

    