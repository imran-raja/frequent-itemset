import os
import time
import functions as fns
import sys

# convert TID strings to int and save in txt file
start_time = time.time()
dict_ = dict()
f1 = open("transactionDB.txt","r")
f2 = open("tempDB.txt","w")

i=1
for line in f1:
    tokens=line.split()
    for t in tokens:
        if not t in dict_:
            dict_[t]=i
            i += 1
            f2.write(str(dict_[t]) + ' ')
        else:
            f2.write(str(dict_[t]) + ' ')
    f2.write('\n')

# input file with int values
input_file = 'tempDB.txt'
lines = []
with open(input_file, 'r') as f:
	for line in f.readlines():
		line = tuple(sorted([int(each) for each in line.split()]))
		lines.append(line)
inputs = lines

# command line input of support and k
support, k_value = int(sys.argv[1]), int(sys.argv[2])

# apriori being implemented here
dict_itemsets = fns.do_apriori(inputs, support, k_value)

print "\nTime taken to terminate: %f seconds" % (time.time()-start_time)
print "Number of %d+ frequent itemsets identified with support of %d is: %d" %(k_value, support, len(dict_itemsets))

# save frequent itemsets in txt file
output_file = 'out_s=%d_k=%d+.txt'%(support,k_value)
with open(output_file,'w') as f:
	for key,value in dict_itemsets.items():
		key = sorted(key)
		itemstring = ' '.join(dict_.keys()[dict_.values().index(int(t))] for t in key)
		string = '%s (%d)\n' % (itemstring,value)
		f.write(string)
