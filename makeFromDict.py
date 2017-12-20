from collections import defaultdict
use_subset = False
dsource = open("wordswithfriends.txt")
words = [x.strip() for x in dsource.readlines()]
if(use_subset):
	words = words[:1000]
dsource.close()
#create a dictionary where dict['string in order']=[all words with those letters]
anagrams=defaultdict(list)
for w in words:
	anagrams[''.join(sorted(w))].append(w)
#we now export to a json compatible format. Could use json module, but it's simple enough
#to do ourselves
# 15Dec12 we can make this file smaller, by not printing the keys, and letting javascript
# calculate them... We'll do this for anagram_keyless.js. This file is 2.6 vs 4.7Mb, but needs
# ~4s more processing locally
osource = open('anagram.js', 'w')
osource_kl = open('anagram_keyless.js', 'w')
osource.write("var v={")
osource_kl.write("var vk=[")
for i,key in enumerate(anagrams):
	if i>0:
		osource.write(",")
		osource_kl.write(",thon")

	osource.write("'%s':[%s]"%(key, ','.join(["'"+x+"'" for x in anagrams[key]])))
	osource_kl.write("[%s]"%(','.join(["'"+x+"'" for x in anagrams[key]])))
	if i % 20 == 0:
		osource.write("\n")
		osource_kl.write("\n")
osource.write("}")
osource_kl.write("]")
osource.close()
osource_kl.close()
