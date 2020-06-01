name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
counts=dict()
#for takings all lines and making split of it

for line in handle:
    words = line.split()
    for word in words:
        counts[word]=counts.get(word,0)+1
        

        

#for fidings big words withs its letters
bigCount=None
bigWord = None
for word,Count in counts.items():
    if bigCount is (None or  Count) > bigCount:
        bigWord = word
        bigCount = counts
print(bigWord,bigCount)

