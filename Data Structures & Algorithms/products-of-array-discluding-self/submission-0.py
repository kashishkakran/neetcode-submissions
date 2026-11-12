class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
# prefix handles everything before the index and suffix handles everything after the index

        n = len(nums)
        pref = [0] * n 
        suff = [0] * n
        res = [0] * n

        pref[0] = 1
        suff[n - 1] = 1

        # build the prefix product array
        for i in range(1, n):
            pref[i] = nums[i-1] * pref[i - 1]

        # build the suff product array
        for i in range(n-2, -1, -1):
            suff[i] = nums[i + 1] * suff[i + 1]
        
        for i in range(n):
            res[i] = pref[i] * suff[i]

        return res
            
            
        # more optimal 
        n = len(nums)
        res = [1] * n
        prefix = 1

        for i in range(1, n):
            res[i] = prefix
            prefix *= nums[i]
        
        postfix = 1
        for i in range(n-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res        