import random
import sys
if (len(sys.argv) != 4):
    exit(84)
for i in range(int(sys.argv[1])):
    print(random.randint(int(sys.argv[2]), int(sys.argv[3])), end="")
    if (i != int(sys.argv[1]) - 1):
        print(" ", end="")
print("")
