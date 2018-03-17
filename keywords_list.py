keywords = []
infile = open('keywords.txt','r')
for lines in range(198):
    d = str(infile.readline())
    keywords.append(d)
infile.close()

for i in range(198):
    keywords[i] = keywords[i].replace('\t\t','')
    keywords[i] = keywords[i].replace('\n','')
print(keywords)
keywords = list(set(keywords))
print(keywords)
