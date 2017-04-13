from dict import dict
import sys
  
letters = sys.argv[ 1: ]
used = {}
for i in range( 0, len( letters ) ):
	used[ i ] = False

words = []

def rec( depth, word ):
	if depth:
		for i in range( 0, len( letters ) ):
			if not used[ i ]:
				used[ i ] = True
				rec( depth - 1, word + letters[ i ] )
				used[ i ] = False
	else:
		if word in dict and word not in words:
			words.append( word );
			print word

n = len( letters )
while n>=3:
	rec( n, "" )
	n -= 1