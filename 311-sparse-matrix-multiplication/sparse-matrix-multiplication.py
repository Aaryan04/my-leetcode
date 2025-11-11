class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        ans = [[0] * len(mat2[0]) for _ in range(len(mat1))]

        for row_idx, row_elements in enumerate(mat1):
            for element_idx, row_element in enumerate(row_elements):
                if row_element:
                    for col_idx, col_element in enumerate(mat2[element_idx]):
                        ans[row_idx][col_idx] += row_element * col_element

        return ans

