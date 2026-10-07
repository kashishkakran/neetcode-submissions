class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        #sort the (number, count) pair by count, in descending order
        sorted_items = sorted(count.items(), key=lambda x: x[1], reverse=True)

        #take the top k numbers
        result = []
        for item in sorted_items[:k]:
            result.append(item[0])
        return result