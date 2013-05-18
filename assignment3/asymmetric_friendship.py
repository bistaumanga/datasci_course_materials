import MapReduce
import sys
mr = MapReduce.MapReduce()

def mapper(record):
    key, value = record[0].encode('utf-8'), record[1].encode('utf-8')
    mr.emit_intermediate(key, value)

def reducer(key, list_of_values):
	for fr in list_of_values:
		if mr.intermediate.has_key(fr):
			if key not in mr.intermediate[fr]:
				mr.emit((key, fr))
				mr.emit((fr, key))
		else:
			mr.emit((key,fr))
			mr.emit((fr, key))

if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)