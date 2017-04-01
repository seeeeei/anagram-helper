import dict.dict
  
letters = sys.argv[ 1: ]
used = {}
for i in range( 0, len( letters ) ):
	used[ i ] = False
word = ""

