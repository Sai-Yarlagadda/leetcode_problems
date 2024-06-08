# This is a less optimized solution

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        temp_num = 0
        rows = len(matrix)
        cols = len(matrix[0])
        last_num_each_cell = []
        while temp_num<rows:
            last_num_each_cell.append(matrix[temp_num][-1])
            temp_num+=1
  
        for i in range(len(last_num_each_cell)):
            if target <= last_num_each_cell[i]:
                row_to_check = i
                break
            else:
                continue
        
        try:
            for i in range(len(matrix[row_to_check])):
                if target == matrix[row_to_check][i]:
                    return True
                else:
                    continue
            return False
        
        except UnboundLocalError:
            return False


# more optimized solution
