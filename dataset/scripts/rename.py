import os

for num in range(31, 57):
    print(num)
    os.system("mv s{}.txt s{}.txt".format(num, num-6))
