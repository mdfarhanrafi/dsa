class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:

        # Helper function to find the row index of the maximum element in a given column
        def maxColEl(arr, m, col):
            ind = -1  # To store the index of the maximum element in the column
            val = -1  # To store the maximum value in the column
            for i in range(m):  # Loop through each row in the column
                if arr[i][col] > val:  # If current element is greater than the previous max
                    val = arr[i][col]
                    ind = i  # Update the index of the max element
            return ind  # Return the row index of the maximum element in the column

        m = len(mat)  # Number of rows
        n = len(mat[0])  # Number of columns

        low, high = 0, n - 1  # Initialize binary search boundaries on columns

        # Binary search loop on columns
        while low <= high:
            mid = (low + high) // 2  # Find the middle column
            # Find the row with the maximum element in the mid column
            row = maxColEl(mat, m, mid)

            # Get the left and right neighbors of the current element
            # Left neighbor (handle edge case if mid == 0)
            l = -1 if mid == 0 else mat[row][mid - 1]
            # Right neighbor (handle edge case if mid == n - 1)
            r = -1 if mid == n - 1 else mat[row][mid + 1]
            c = mat[row][mid]  # Current element

            # Check if the current element is a peak
            if l < c > r:
                return [row, mid]  # Peak found, return its position

            # If left neighbor is greater, move to the left half
            elif c < l:
                high = mid - 1
            # If right neighbor is greater, move to the right half
            else:
                low = mid + 1

        # Return [-1, -1] if no peak is found (edge case, though the problem guarantees a peak exists)
        return [-1, -1]
