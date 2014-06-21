import sys

def dna2freqs(str):
	dict={'A':0,'C':0,'G':0,'T':0}
	for x in str:
		dict[x]=dict[x]+1
	return "{A} {C} {G} {T}".format(**dict)	

def main(argv):
	print dna2freqs(argv[0])

if __name__ == "__main__":
   main(sys.argv[1:])
