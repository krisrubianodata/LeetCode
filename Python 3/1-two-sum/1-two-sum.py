class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtable = {}

        for i in range(len(nums)):
            hashtable[nums[i]] = i

        for i in range(len(nums)):
            j = target - nums[i]

            if j in hashtable and hashtable[j] != i:
                return [i, hashtable[j]]