import MapReduce
import sys

'''
SELECT * 
FROM Orders, LineItem 
WHERE Order.order_id = LineItem.order_id
'''

mr = MapReduce.MapReduce()

def mapper(record):
    key = record[1]
    value = record[0:]
    mr.emit_intermediate(key, value)

def reducer(key, list_of_values):
    orderList = [[]]
    for val in list_of_values:
      if val[0] == 'order':
        orderList.append([i.encode('utf-8') for i in val])
      
    orderList = orderList[1:]
    final = [[]]
    for val in list_of_values:
      if val[0] == 'line_item':
        for j in orderList:
          final.append(j + [i.encode('utf-8') for i in val])
    
    final = final[1:]
    for line in final:
      mr.emit(line)

if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
