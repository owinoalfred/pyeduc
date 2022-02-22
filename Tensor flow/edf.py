def find_max(nums):
    max_num = float('-inf')
    for num in nums:
        if num > max_num:
            max_num = num 
            return max_num


print(find_max((33.4, 44.6, 67.6)))