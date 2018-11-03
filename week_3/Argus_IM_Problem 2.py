# Created by Young Chen at 8/27/2018
class Solution(object):
    # M is every matrix
    def get_sum(self, M, x1, x2, y1, y2):
        mydict = {}
        for i in range(len(M)):
            sum_of_row = 0
            for j in range(len(M[0])):
                sum_of_row += M[i][j]
                if i != 0:
                    mydict[(i,j)] = mydict[(i-1,j)] + sum_of_row
                else:
                    mydict[(i, j)] = sum_of_row
        return mydict[(x2,y2)] - mydict[(x1,y2)] - mydict[(x2,y1)] + mydict[(x1,y1)]