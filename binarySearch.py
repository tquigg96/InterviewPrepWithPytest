def search(nums, target):
    
    right = len(nums) - 1
    left = 0

    mid = (len(nums)-1) //2
    print(mid)
        

    if len(nums) == 1 or nums[0] == target:
        return 0
        

    while(left <= right):
        if right >= left:
            mid = left + (right-left) //2 #half it

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
        
        
                
                        
    return -1


nums = [4,5,6,7,0,1,2]

val = search(nums, 6)
print(val)

    