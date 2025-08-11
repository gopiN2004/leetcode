class Solution:
    def rob(self, nums: List[int]) -> int:
      cur=prev=0
      for num in nums:
        prev,cur=cur,max(cur,prev+num)
      return cur