class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        if sum(gas)<sum(cost):
            return -1
        tank,index_no=0,0
        for x in range(len(gas)):
            tank+=gas[x]-cost[x]
            if tank<0:
                tank,index_no=0,x+1
        return index_no
                

       
         