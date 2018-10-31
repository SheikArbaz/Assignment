class Solution:
    # @param A : tuple of strings
    # @return a list of list of integers
    def anagrams(self, A):
        #Dict for Mapping:- str->[indices]
        d = {}
        for i in xrange(len(A)):
            Ai_sort = ''.join(sorted(A[i]))#list to str
            if Ai_sort not in d.keys():
                d[Ai_sort]=[i+1]#1-based indexing
            else:
                d[Ai_sort].append(i+1)
        return d.values()
            