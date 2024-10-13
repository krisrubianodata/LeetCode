class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashtable = {}
        length = len(nums)

        for i in range(length):
            if nums[i] in hashtable:
                if abs(hashtable[nums[i]] - i) <= k:
                    return True
            hashtable[nums[i]] = i
                
        return False