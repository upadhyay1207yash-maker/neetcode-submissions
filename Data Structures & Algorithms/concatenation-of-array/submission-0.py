class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:

        i,j,n = 0,0,len(nums)
        ans = [0]*2*n

        for num in nums:
            ans[i] = num
            ans[i+n] = num
            i+=1
        return ans