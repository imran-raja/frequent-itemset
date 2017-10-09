from collections import defaultdict
from customset import myCustomSet

# makes 2-itemsets from one tuple
def make_two_itemsets_from_one_fz(items):
    items = sorted(list(items))
    two_item_list = []
    for i in range(len(items)):
        for j in range(i+1, len(items)):
            two_item_list.append(tuple(sorted([items[i],items[j]])))
    return two_item_list

# makes 2-itemsets from multiple tuple
def make_two_itemsets_from_multiple_fz(list_fz, support, results, k_val):
	one_itemset, two_itemsets = defaultdict(int), defaultdict(int)
	for i in range(len(list_fz)):
		for item in make_two_itemsets_from_one_fz(list_fz[i]):
			two_itemsets[item] += 1
		if k_val == 1:
			for each in list_fz[i]:
				one_itemset[each] += 1
	if k_val == 1:
		results = {tuple(sorted([k])):one_itemset[k] for k in one_itemset if one_itemset[k] >= support}
	return two_itemsets, results

# tests if itemset is frequent
def freq_or_not(cans, itemset):
	itemset = myCustomSet(list(itemset))
	for item in itemset:
		item = myCustomSet(item)
		z = tuple(sorted(itemset.mydiff(item)))
		if z not in cans:
			return False
	return True

# generates candidates
def make_cans(cans,k):
	can_store = myCustomSet()
	for i in cans:
		for j in cans:
			i = myCustomSet(list(i))
			j = myCustomSet(list(j))
			i, j, z = tuple(i), tuple(j), tuple(sorted(i.myunion(j)))
			if len(z)==k and i != j:
				if freq_or_not(cans, z):
					can_store.myadd(z)
	return can_store

# counts the number of candidates
def count_cans(list_fz, cans):
	count = defaultdict(int)
	for i in range(len(list_fz)):
		list_fz[i] = list(list_fz[i])
		z =[c for c in cans if all(x in list_fz[i] for x in c)]
		for i in range(len(z)):
			count[z[i]] += 1
	return count

def make_sup_cans(count, sup):
	can_dict = {item:count[item] for item in count if count[item] >= sup}
	return can_dict

def do_apriori(input, support,k):
	results = {}
	cans, final_dict = make_two_itemsets_from_multiple_fz(input, support, results, k)
	print 'This is iteration number: 2'
	if cans:
		sup_can_dict = {item:cans[item] for item in cans if cans[item] >= support}
	if k <=2:
		final_dict.update(sup_can_dict)
	cans = sup_can_dict
	sup = 3
	while cans:
		print 'This is iteration number: %d' % sup
		cans = make_cans(cans.keys(), sup)
		# print len(cans)
		if not cans:
			break
		count = count_cans(input, cans)
		# print len(count)
		sup_can_dict = make_sup_cans(count, support)
		# print len(sup_can_dict)
		if k <= sup:
			final_dict.update(sup_can_dict)
		cans = sup_can_dict
		sup += 1
	return final_dict
