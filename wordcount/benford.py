''' Benford check for bad data'''
from math import log10

mynum = '1, 2 ,3, 4, 5, 6, 7, 8, 9, 1'

mynum = mynum.replace(',', ' ').replace('\t', ' ').replace(';', ' ')

numlist = mynum.split()

numdict = {'1':0, '2':0, '3':0, '4':0, '5':0, '6':0, '7':0, '8':0, '9':0}

total = 0

for n in numlist:
	if n[0] in numdict:
		numdict[n[0]] += 1
		total += 1
		


print(numdict)

benford = [total*log10(1 + 1./i) for i in range(1, 10)]

for n in benford:
	print(n)
