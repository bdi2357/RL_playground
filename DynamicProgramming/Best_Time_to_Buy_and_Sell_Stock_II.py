class Solution(object):
    def maxProfitSimple(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        #print(prices)
        if len(prices) == 0:
            #print("Here")
            return 0,0,0
        min_p = prices[0]
        max_pr = 0
        min_ind =0
        best_max_ind = 0
        best_min_ind =0
        for ii in range(len(prices)):
            if prices[ii] < min_p:
                min_p = prices[ii]
                min_ind = ii
            elif prices[ii] - min_p > max_pr:
                max_pr = prices[ii] - min_p
                best_max_ind = ii
                best_min_ind = min_ind
        return max_pr,best_min_ind,best_max_ind
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        print(prices)
        max_pr_simple,start,end = self.maxProfitSimple(prices)
        if max_pr_simple == 0:
            return 0
        addition = 0 
        #print("start: %d end: %d"%(start,end))
        #print(prices[start:min(end+1,len(prices)-1)])
        for ii in range(start,min(end+1,len(prices)-1)-1):
            if prices[ii]> prices[ii+1]:
                addition += prices[ii] - prices[ii+1]
        #print(addition,max_pr_simple)
        return self.maxProfit(prices[:start])+max_pr_simple+addition+self.maxProfit(prices[end+1:])
    
        
        
