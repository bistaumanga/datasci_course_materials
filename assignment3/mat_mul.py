import MapReduce
import sys
mr = MapReduce.MapReduce()
L, M, N = 5, 5, 5

def mapper(record):
	matrix = record[0].encode('utf-8')
	if matrix == 'a':
		i, j, val = record[1], record[2], record[3]
		for k in range(N):
   			mr.emit_intermediate((i,k), {(matrix,j):val})
   	elif matrix == 'b':
   		j, k, val = record[1], record[2], record[3]
   		for i in range(L):
   			mr.emit_intermediate((i,k), {(matrix,j):val})

def reducer(key, val):
	#print key,val
	A, B = [0] * M, [0] * M
	for v in val:
		if v.keys()[0][0] == 'a':
			A[v.keys()[0][1]] = v.values()[0]
		if v.keys()[0][0] == 'b':
			B[v.keys()[0][1]] = v.values()[0]
	i, k = key[0], key[1]
	mr.emit((key[0], key[1], sum(x * y for x, y in zip(A, B))))

if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)