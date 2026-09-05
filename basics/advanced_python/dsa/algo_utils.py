class BinarySearch:

    @staticmethod
    def search(array, target):
        left, right = 0, len(array)

        while left <= right:
            mid = (left + right) // 2

            if array[mid] == target:
                return mid
            elif array[mid] > target:
                # update search space to be on the left side of mid
                right = mid - 1
            else: # mid < target
                # update search space to be on the right side of mid
                left = mid + 1

        # Return "False" if target not found
        return False


class SelectionSort:

    @staticmethod
    def minimalSort(array):
        """
        Runs through the array, pops out the minimum value, and
        Inserts it at the front of the array

        Problem: Each pop & insert operation shifts the remaining elements
        High Time Complexity
        """
        length = len(array)
        for i in range(length-1): # Note the range
            min_index = i
            for j in range(i+1, length):
                if array[j] < array[min_index]:
                    min_index = j
            min_value = array.pop(min_index) # this removes the min value
            array.insert(i, min_value) # the inserts at the start

        return array

    @staticmethod
    def sort(array):
        """
        Swaps the minimum value with the value at front of the array"
        Doesn't have to shift values in the array for each operation
        """
        length = len(array)
        for i in range(length): # Note the range difference
            min_index = i
            for j in range(i+1, length):
                if array[j] < array[min_index]:
                    min_index = j
            # Swap the elements (min value index & element at front)
            array[i], array[min_index] = array[min_index], array[i]

        return array


class QuickSort:
    def __init__(self):
        pass

    # @staticmethod
    def partition(self, array, low, high):
        """
        Receives a sub-array, moves values around, 
        Swaps the pivot element into the sub-array, and 
        
        input:
            array, low, high

        returns:
            the index where the next split in sub-arrays happens.
        """
        pivot = array[high]
        i = low - 1

        for j in range(low, high):
            if array[j] <= pivot:
                i = i + 1
                array[i], array[j] = array[j], array[i]
        array[i + 1], array[high] = array[high], array[i + 1]

        return i + 1

    # @staticmethod
    def sort(self, array, low=0, high=None):
        if high is None: high = len(array) - 1

        if low < high:
            pivot_index = self.partition(array, low, high)
            self.sort(array, low, pivot_index - 1)
            self.sort(array, pivot_index + 1, high)

