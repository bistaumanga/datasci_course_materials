import MapReduce
import sys

mr = MapReduce.MapReduce()

def mapper(record):
    key = record[0]
    value = record[1]
    words = value.split()
    for w in words:
      mr.emit_intermediate(w, key)

def reducer(key, list_of_values):
    total = []
    for v in list_of_values:
      if v not in total:
        total.append(v.encode('utf-8'))
    mr.emit((key, total))

if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
