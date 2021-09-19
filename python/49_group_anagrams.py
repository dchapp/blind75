
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        return self.by_sort(strs)
   
    
    def by_sort(self, strs):
        sorted_strs = [(i, "".join(x for x in sorted(s))) for i,s in enumerate(strs)]
        #print(sorted_strs)
        groups = {}
        for x in sorted_strs:
            idx, ss = x
            ss = tuple(ss)
            if ss not in groups:
                groups[ss] = [idx]
            else:
                groups[ss].append(idx)
        #print(groups)        
        return [ [strs[i] for i in v] for v in groups.values() ]
