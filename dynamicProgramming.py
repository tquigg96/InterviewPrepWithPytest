
#this approach adopts a binary search in the mix
def threeSome(target, nums):
    sumVals = []
    nums.sort()

    if len(nums) < 3:
        return []

    for i in range(0, len(nums)-2):
        left = i+1
        right = len(nums) -1

        if (nums[i] + nums[left] + nums[right] == target):
            sumVals.append(nums[i])
            sumVals.append(nums[left])
            sumVals.append(nums[right])
        
        elif(nums[i] + nums[left] + nums [right] < target):
            left += 1

        else:
            right -= 1

    return sumVals


vals = [1, 0, 1, 2, -2, 0]

sumVals = threeSome(0, vals)

print(sumVals)