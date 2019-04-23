#导入CSV

import csv
filename = 'flpandsr稳定.csv, encoding= "gbk"', 
with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)
	print(index, header_row)
