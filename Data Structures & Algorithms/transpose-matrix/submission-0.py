class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        new = [[0] * len(matrix) for _ in range(len(matrix[0]))]
        for m in range(len(matrix)):
            for n in range(len(matrix[m])):
                new[n][m] = matrix[m][n]
        return new 