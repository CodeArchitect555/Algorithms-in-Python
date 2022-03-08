def selection_sort(nums):
    for i in range(5):
        minpos = i
        print(minpos)
        for j in range(i,6):
            if nums[j] < nums[minpos]:
                minpos = j    
        temp = nums[i]
        nums[i] = nums[minpos]
        nums[minpos] = temp
        print(nums)

list_a = [5,3,7,4,8,0]
selection_sort(list_a)

def better_selection_sort(nums):
    for i in range(0,len(nums)-1):
        minpos = i
        for j in range(i,len(nums)):
            if nums[j] < nums[minpos]:
                minpos = j
        temp = nums[i]
        nums[i] = nums[minpos]
        nums[minpos] = temp
        print(nums)

list_b = [7,9,8,5,3,6,8,9,2,4,9,10,2,3,5,6]
better_selection_sort(list_b)        