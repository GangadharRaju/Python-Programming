#CREATE A FILE AND WRITE RANDOM INTEGERS INTO THE FILE
import random
f = open("CSEA_integers.txt", 'w')
for count in range(25):
    number = random.randint(1, 500)
    f.write(str(number)+'\n' )
f.close()
