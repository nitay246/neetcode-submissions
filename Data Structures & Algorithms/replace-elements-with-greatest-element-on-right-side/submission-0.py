class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxi = -1 
        for i in range(len(arr) - 1, -1, -1):
            if maxi < arr[i]:
                temp = maxi
                maxi = arr[i]
                arr[i] = temp
            else:
                arr[i] = maxi
        return arr   