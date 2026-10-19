class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        hashmap={}
        nums.sort()
        for i in range(len(nums)):
            if nums[i] not in hashmap:
                hashmap[nums[i]]=[]
            hashmap[nums[i]].append(i)
        return hashmap.get(target,[])