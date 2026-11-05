class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        OCounter = Counter(nums)
        output = OCounter.most_common(k)
        for i, x in enumerate(output):
            output[i] = output[i][0]
        return output