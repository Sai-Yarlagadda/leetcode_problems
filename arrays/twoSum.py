def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict_nums = {}
        for i, num1 in enumerate(nums):
            #num1 + num2 = target
            num2 = target - num1
            if num2 in list(dict_nums.values()):
                key_list = list(dict_nums.keys())
                val_list = list(dict_nums.values())
                position = val_list.index(num2)
                j = key_list[position]
                return [j, i]
            else:
                dict_nums[i] = num1

if __name__ == '__main__':
  nums = [1,2,3]
  target = 5
  output = twoSum(nums, target)
  print(output)
