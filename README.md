# frequent-itemset

USAGE:

The apriori.py script takes as input the Support and k-value from the command line:

The command line input should look like the following:

python apriori.py <support> <k-value>

For example, to generate 1+ frequent itemsets identified with support of 75 is, the command line input should be:

python apriori.py 75 1


INPUT:

The input line is already loaded in the apriori.py script in line 9. If this script this used on a different dataset (formatted in the same fashion), line 9 needs to be edited. 

OUTPUT:

The output files are generated as txt files with the following name: out_s=<support>_k=<k-value>+.txt.
For example, to generate 1+ frequent itemsets identified with support of 75 is, the following output file will be generated: out_s=75_k=1+.txt
