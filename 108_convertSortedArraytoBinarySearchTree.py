# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if nums==[]:
            return None

        mid = len(nums) // 2

        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])

        return root
 
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def main():
    solution = Solution()

    a = [1,2,3,4,5,6,7,8,9]
    # a = [-1,0,1,2]

    atree = solution.sortedArrayToBST(a)

    # print ('Output:', solution.isSameTree(aroot,broot))


if __name__ == '__main__':
    main()