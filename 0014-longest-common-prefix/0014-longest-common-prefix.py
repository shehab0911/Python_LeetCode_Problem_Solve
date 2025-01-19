class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        pre=strs[0]
        for x in strs:
            while not x.startswith(pre):
                pre=pre[:-1]
                if not pre:
                    return ""

        return pre








strs = ["flower", "flow", "flight"]
obj=Solution()
result=obj.longestCommonPrefix(strs)
print(result)