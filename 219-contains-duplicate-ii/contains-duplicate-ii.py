class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        freq={}
        for i in range(len(nums)):
            if nums[i] not in freq:
                freq[nums[i]]=i
            else:
                # if present,check distance
                if abs(freq[nums[i]]-i)<=k:
                    return True
                # update with new distance
                freq[nums[i]]=i
        return False