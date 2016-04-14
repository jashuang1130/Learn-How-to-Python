# calculate the content in DNA seq of BRCA1
gene = open ("brca1_sequence.txt", "r")

# set values to 0
A = 0;
T = 0;
G = 0;
C = 0;

# skip first line of header in txt file
gene.readline()

for line in gene:
	line = line.upper()
	for char in line:
		if char == "A":
			A += 1
		if char == "T":
			T += 1
		if char == "G":
			G += 1
		if char == "C":
			C += 1

print "What contents would you like to look at?"
choice = raw_input("Please type AT or GC content: ").upper()

# converting the numbers to float by adding a float number
AT = (A+T+0.)/(A+T+C+G+0.)
percent_AT = AT * 100.00

GC = (G+C+0.)/(A+T+C+G+0.)
percent_GC = GC * 100.00

if choice == "GC":
	print "The GC content for BRCA1 is "+ str(GC)
	print "Which is " + str(percent_GC) + "%"
	print " "

elif choice == "AT":
	print "The AT content for BRCA1 is "+ str(AT)
	print "Which is " + str(percent_AT) + "%"
	print " "

else:
	print "You've enterted: %s This is not a valid choice. " % choice
	
# printing A and T in one line  print "The number of A's are %s, number of T's are %s" %(A, T)
print "The total nucleic acid content is:  "
print "The number of A's are " + str(A)
print "The number of T's are " + str(T)
print "The number of G's are " + str(G)
print "The number of C's are " + str(C)
print " "
