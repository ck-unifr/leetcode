# https://leetcode.com/problems/4sum/description/

# Fork from https://shenjie1993.gitbooks.io/leetcode-python/018%204Sum.html
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if len(nums) < 4:
            return []
        result = set()
        sumsIndexes = {}
        # Get all two elements' sum and indexes map
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] in sumsIndexes:
                    sumsIndexes[nums[i] + nums[j]].append((i, j))
                else:
                    sumsIndexes[nums[i] + nums[j]] = [(i, j)]

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                sumNeeded = target - (nums[i] + nums[j])
                if sumNeeded in sumsIndexes:
                    for index in sumsIndexes[sumNeeded]:
                        # Ingore repeating results
                        if index[0] > j:
                            result.add(tuple(sorted([nums[i], nums[j], nums[index[0]], nums[index[1]]])))
        # Format result with list[list] pattern
        result = [list(l) for l in result]
        return result


if __name__ == "__main__":
    assert Solution().fourSum([1, 0, -1, 0, -2, 2], 0) == [[-1, 0, 0, 1], [-2, 0, 0, 2], [-2, -1, 1, 2]]