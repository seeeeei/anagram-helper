from dict import dict
import sys

if len(sys.argv) == 1:
	print "no letters provided"
	letters = [ 'z' ]
elif len(sys.argv) == 2:
  letters = sys.argv[ 1 ]
else:
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
while n>=4:
  rec( n, "" )
  n -= 1