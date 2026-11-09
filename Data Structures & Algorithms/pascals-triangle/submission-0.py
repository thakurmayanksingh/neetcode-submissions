class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows==0:
            return []
                
        triange = [[1]]

        for x in range(1,numRows):
            prev_row = triange[-1]

            current_row = [1]
            for j in range(1,x):
                current_row.append(prev_row[j-1] + prev_row[j]
                                        )
            current_row.append(1)
            triange.append(current_row)
        return triange