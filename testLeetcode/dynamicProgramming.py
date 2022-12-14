
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

#improved with no duplicates, all solutions
def threeSumAll(target, nums):
    sumVals = []
    nums.sort()

    if len(nums) < 3:
        return []

    for i,a in enumerate(nums):
        left = i+1
        right = len(nums) -1
        if i > 0 and a == nums[i-1]:
            continue

        while( left < right):
            if (nums[i] + nums[left] + nums[right] == target):
                sumVals.append([nums[i], nums[left], nums[right]])
                left += 1
                while nums[left] == nums [left-1] and left < right:
                    left += 1

                
            elif(nums[i] + nums[left] + nums [right] < target):
                left += 1

            else:
                right -= 1

    return sumVals

#O(logn)
def firstMissingPositive(nums):
    s=set(nums)
    for i in range(1,len(nums)+2):
        if i not in s:
            return i

def minCoins(coins, amount):
    dp = [float('inf') for _ in range(amount + 1)]
    dp[0] = 0

    for i in range(0,len(dp)):
        
        for c in coins:
            #print('i' + str(i) + 'coins' + str(c))
            if i-c >= 0:
              
                dp[i] = min(dp[i], dp[i-c]+1)
            #print(dp)
    
    return -1 if dp[-1] == float('inf') else dp[-1]

    
        
#O(nLogn) + O(n^2)
vals = [1, 0, -1, 2, -2, 0]
coins = [1,3,5]

sumVals = threeSome(0, vals) # this one finds the first solution it finds then returns it and is buggy lets improve it
newSumVals = threeSumAll(0, vals)
value = firstMissingPositive(vals)
coins = minCoins(coins, 11)

print(sumVals)
print(newSumVals)
print(value)
print(coins)

