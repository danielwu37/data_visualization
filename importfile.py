import csv
filename = 'flpandsr稳定.csv'
with open(filename, encoding='utf-8') as f:
	reader = csv.reader(f)
	header_row = next(reader)
	
	deptime = []
	for row in reader:
		deptime = int(row[11])
		deptime.append(deptime)
	print(deptime)
