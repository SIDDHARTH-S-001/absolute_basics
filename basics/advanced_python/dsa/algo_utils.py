class BinarySearch:
    def __init__(self, array):
        self.array = array

    def search(self, target):
        left = 0
        right = len(self.array)

        while left <= right:
            mid = (left + right) // 2

            if self.array[mid] == target:
                return mid
            elif self.array[mid] > target:
                # update search space to be on the left side of mid
                right = mid - 1
            else: # mid < target
                # update search space to be on the right side of mid
                left = mid + 1

        # Return "False" if target not found
        return False
                
            
