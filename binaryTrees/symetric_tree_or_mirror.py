from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def sym(root1, root2) -> bool:
            if not root1 and not root2:
                return True
            if not root1 or not root2:
                return False
            if root1.val != root2.val:
                return False

            return sym(root1.left, root2.right) and sym(root1.right, root2.left)

        return sym(root, root)


# Main function
if __name__ == "__main__":
    # Creating a sample symmetric binary tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(3)

    # Creating an instance of the Solution class
    solution = Solution()

    # Check if the binary tree is symmetric
    is_symmetric = solution.isSymmetric(root)

    print("The binary tree is symmetric:", is_symmetric)
