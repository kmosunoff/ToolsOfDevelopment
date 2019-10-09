class Sorter():

    """[Method that sorts a list using a bubble sort algorithm]
    
    Returns:
        [nums] -- [sorted list of numbers]
    """
    def bubble_sort(self, nums):
        swapped = True
        while swapped:
             swapped = False
             for i in range(len(nums) - 1):
                 if nums[i] > nums[i + 1]:
                     nums[i], nums[i + 1] = nums[i + 1], nums[i]
                     swapped = True
        return nums
    
    """[Method that sorts a list using a selection sort algorithm]
    
    Returns:
        [nums] -- [sorted list of numbers]
    """
    def selection_sort(self, nums):
        n = len(nums)
        for i in range(n):
            i_min = i
            for k in range(i + 1, n):
                if nums[k] < nums[i_min]:
                    i_min = k
            nums[i_min], nums[i] = nums[i], nums[i_min]
        return nums

    """[Method that sorts a list using an insertion sort algorithm]
    
    Returns:
        [nums] -- [sorted list of numbers]
    """
    def insertion_sort(self, nums):
        for i in range(1, len(nums)):
            item_to_insert = nums[i]
            j = i - 1
            while j >= 0 and nums[j] > item_to_insert:
                nums[j + 1] = nums[j]
                j -= 1
            nums[j + 1] = item_to_insert
        return nums