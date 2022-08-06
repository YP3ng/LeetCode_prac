class Solution:
    def canMakeArithmeticProgression(self, arr) -> bool:
        
        
        # sort
        for i in range (1, len(arr)):
            v = arr[i]
            j = i - 1
            while j >= 0 and v < arr[j]:
                arr[j+1] = arr[j]
                j = j - 1
            arr[j+1] = v

        # ai = a1 + (i-1)d
        d = arr[1] - arr[0]
        for i in range(1, len(arr)):
            if arr[i] - arr[i-1] == d:
                continue
            else:
                return False
        
        return True

if __name__ == "__main__":
    s1 = Solution()

    arr = [3,5,1]
    print(s1.canMakeArithmeticProgression(arr))

    arr = [9,8,7,6,5,4,3,2,1]
    print(s1.canMakeArithmeticProgression(arr))