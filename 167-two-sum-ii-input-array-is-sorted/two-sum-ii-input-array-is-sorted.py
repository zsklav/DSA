class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        seen={}
        for i in range(len(numbers)):
            comple=target-numbers[i]
            if comple in seen:
                return [seen[comple]+1,i+1]
            seen[numbers[i]]=i
        