class Solution(object):
    def findMaxAverage(self, nums, k):
        w_sum=sum(nums[:k])
        m_sum=w_sum
        for i in range(k,len(nums)):
            w_sum=w_sum+nums[i]-nums[i-k]
            m_sum=max(m_sum,w_sum)
        return m_sum/float(k)


