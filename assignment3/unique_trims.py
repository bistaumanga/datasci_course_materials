import MapReduce
import sys
mr = MapReduce.MapReduce()

def mapper(record):
    key, value = record[0].encode('utf-8'), record[1].encode('utf-8')
    mr.emit_intermediate(key, value[:-10])

def reducer(key, seq):
	if seq[0] not in mr.result:
		mr.emit(seq[0])

if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)