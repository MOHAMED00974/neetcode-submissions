class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lr, rr= 0, len(matrix)-1
        while lr<= rr: 
            midr= (lr+ rr)//2
            if matrix[midr][0]== target: 
                return True
            elif matrix[midr][0]> target: 
                rr= midr- 1
            else: 
                lc, rc= 0, len(matrix[0])-1
                while lc<= rc: 
                    midc= (lc+ rc)//2
                    if matrix[midr][midc]== target: 
                        return True
                    elif matrix[midr][midc]> target: 
                        rc= midc- 1
                    else: 
                        lc= midc+ 1 
                lr= midr+ 1
        return False