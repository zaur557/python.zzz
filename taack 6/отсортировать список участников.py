inFile = open('input.txt', 'r', encoding='utf8')
outFile = open('output.txt', 'w', encoding='utf8')
lines = inFile.readlines()
lines.sort()
for i in lines:
    print(*i.split()[:2] + i.split()[3:], file=outFile)
inFile.close()
outFile.close()
