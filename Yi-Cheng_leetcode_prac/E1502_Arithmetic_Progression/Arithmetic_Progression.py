class Solution:
    def canMakeArithmeticProgression(self, arr) -> bool:
        '''
        This method can run, but it is slow and will change descending ordered list to ascending first
        '''
        # sort
        self.Mergesort(arr)

        # ai = a1 + (i-1)d
        d = arr[1] - arr[0]
        for i in range(1, len(arr)):
            if arr[i] - arr[i-1] == d:
                res = True
                continue
            else:
                return False
        
        return True
    
    def InsertionSort(self, arr):
        for i in range (1, len(arr)):
            v = arr[i]
            j = i - 1
            while j >= 0 and v < arr[j]:
                arr[j+1] = arr[j]
                j = j - 1
            arr[j+1] = v

    def Merge(self, B, C, A):
        p = len(B)
        q = len(C)
        i = j = k = 0
        while i < p and j < q:
            if B[i] <= C[j]:
                A[k] = B[i]
                i = i + 1
            else:
                A[k] = C[j]
                j = j + 1
                k = k + 1
        if i == p:
            A[k: p + q] = C[j: q]
        else:
            A[k: p + q] = B[i: p]

    def Mergesort(self, A):
        if len(A) > 1:
            n = len(A)
            print("Bracket A: ", A)
            B = A[:n // 2]
            print("Bracket B: ", B)
            C = A[n // 2:]
            print("Bracket C: ", C)
            Solution.Mergesort(self, B)
            Solution.Mergesort(self, C)
            Solution.Merge(self, B, C, A) # FIXME: sA is a para

if __name__ == "__main__":
    s1 = Solution()

    # True
    #arr = [3,5,1]
    #print(s1.canMakeArithmeticProgression(arr))

    # True
    #arr = [9,8,7,6,5,4,3,2,1]
    #print(s1.canMakeArithmeticProgression(arr))

    # False
    arr = [1,2,4]
    print(s1.canMakeArithmeticProgression(arr))