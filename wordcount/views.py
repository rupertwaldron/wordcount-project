from django.http import HttpResponse
from django.shortcuts import render # used with templates
import operator
from math import log10

def homepage(request):
	#return HttpResponse('<h1>Hello</h1>')
	
	#return render(request, 'home.html', {'Hi': 'Hello Rupert'})
	return render(request, 'home.html')

def count(request):
	fulltext = request.GET['fulltext']
	wordlist = fulltext.split()
	worddictionary = {}
	for word in wordlist:
		if word in worddictionary:
			worddictionary[word] += 1
		else:
			worddictionary[word] = 1
	sortedwords = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)

	return render(request, 'count.html', {'fulltext' : fulltext, 'count' : len(wordlist), 'worddictionary' : sortedwords})

def about(request):
	return render(request, 'about.html')

def benford(request):
	fulltext = request.GET['fulltext']
	mynum = fulltext.replace(',', ' ').replace('\t', ' ').replace(';', ' ')

	numlist = mynum.split()

	numdict = {'1':0, '2':0, '3':0, '4':0, '5':0, '6':0, '7':0, '8':0, '9':0}


	total = 0
	for n in numlist:
		if n[0] in numdict:
			numdict[n[0]] += 1
			total += 1


	benford = [total*log10(1 + 1./i) for i in range(1, 10)]

	return render(request, 'benford.html', {'numdict' : numdict.items(), 'benford' : benford})