import sys
f = open("bme280.txt", "r")
try:
    if sys.argv[1] == 'all':
        print(f.read())
except:
    print(f.readline().rstrip())
    print(f.readlines()[-1])
f.close()
