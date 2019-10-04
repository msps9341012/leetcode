def findDiagonalOrder(matrix):
	res=[]
	for i in range(len(matrix)):
		for j in range(len(matrix[0])):
			t=[]
			if matrix[i][j]!='T':
				t.append(matrix[i][j])
				d=i+1
				l=j-1
				while d<len(matrix) and l>-1:
					t.append(matrix[d][l])
					matrix[d][l]='T'
					d=d+1
					l=l-1
				res=res+t[::-1]
			

def findDiagonalOrder(self, matrix):
    """
    :type matrix: List[List[int]]
    :rtype: List[int]
    """
    result = [ ]
    dd = collections.defaultdict(list)
    if not matrix: return result
    # Step 1: Numbers are grouped by the diagonals.
    # Numbers in same diagonal have same value of row+col
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[0])):
            dd[i+j+1].append(matrix[i][j]) # starting indices from 1, hence i+j+1.
    # Step 2: Place diagonals in the result list.
    # But remember to reverse numbers in odd diagonals.
    for k in sorted(dd.keys()):
        if k%2==1: dd[k].reverse()
        result += dd[k]
    return result

m=[[ 1,  2,  3,  4],
   [ 6,  7,  8,  9],
    [11, 12, 13, 14],
    [16, 17, 18, 19]]
findDiagonalOrder(m)

[1, 6, 2, 11, 7, 3, 16, 12, 8, 4, 17, 13, 9, 18, 14, 19]