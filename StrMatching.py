def kmpMatch(text, pattern):
	n = len(text)
	m = len(pattern)
	fail = []
	fail = computeFail(pattern)
	i=0
	j=0

	while (i < n):
		if (pattern[j] == text[i]):
			if (j == m - 1):
				return i - m + 1 #match 
			i += 1
			j += 1
		elif (j > 0):
			j = fail[j-1]
		else:
			i += 1
	return -1 #no match

def computeFail(pattern):
	fail = [0]*len(pattern)
	m = len(pattern)
	j = 0
	i = 1

	while (i < m):
		if  (pattern[j] == pattern[i]):   #j+1 chars match
			fail[i] = j + 1
			i += 1
			j += 1
		elif (j > 0): #j follows matching prefix
			j = fail[j-1]
		else:     #no match
			fail[i] = 0
			i += 1

	return fail

def bmMatch(text, pattern):
	last = []
	last = buildLast(pattern)
	n = len(text)
	m = len(pattern)
	i = m-1

	if (i > n-1):
		return -1 #no matchif pattern is longer than text

	j = m-1;

	if (pattern[j] == text[i]):
		if (j == 0):
			return i # match
		else: # looking-glass technique
			i -= 1
			j -= 1
	else: # character jump technique
		lo = last[ord(text[i])]  #last occ
		i = i + m - min(j, 1+lo)
		j = m - 1

	while (i <= n-1):
		if (pattern[j] == text[i]):
			if (j == 0):
				return i # match
			else: # looking-glass technique
				i -= 1
				j -= 1
		else: # character jump technique
			lo = last[ord(text[i])]  #last occ
			i = i + m - min(j, 1+lo)
			j = m - 1

	return -1; #no match 

def buildLast(pattern): # Return array storing index of last occurrence of each ASCII char in pattern.
	last = [-1]*128 # ASCII char set
	for i in range(len(pattern)):
		last[ord(pattern[i])] = i
	return last

def isSpamKMP(text, pattern):
	idx = kmpMatch(text,pattern)
	if(idx == -1):
		return False
	else:
		return True

def isSpamBM(text, pattern):
	idx = bmMatch(text,pattern)
	if(idx == -1):
		return False
	else:
		return True

t1 = "Adit kuliah di itb jalan"
p1 = "Adit"

print(isSpamKMP(t1,p1))
print(isSpamBM(t1,p1))