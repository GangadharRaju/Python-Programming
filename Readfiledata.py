#Read data from the file and display the file data
f = open("CSEA_integers.txt", 'r')
for line in f:
    print(line,end="")
