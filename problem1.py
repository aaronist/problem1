def find_max(nums: list[int]) -> int:
    '''
    Finds the maximum value using recursion of the given
    list of integers, or None if the list is empty
    '''
    try:
        if len(nums) > 1:
            if nums[0] > nums[1]:
                return find_max([nums[0]] + nums[2:])
            else:
                return find_max(nums[1:])
        else:
            return nums[0]
    except IndexError:
        # Occurs when user inputs an empty list
        return None
