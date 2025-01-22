class Solution(object):
    def uniqueOccurrences(self, arr):
        s=Counter(arr)
        list1=[]
        list2=[]
        list3=[]
        for key ,values in s.items():
            list1.append(values)
        for x in list1:
            if x in list1 and x not in list2:
                list2.append(x)
            else:
                list3.append(x)
        if len(list3)>0:
            return False
        else:
            return True

        
        
            
        