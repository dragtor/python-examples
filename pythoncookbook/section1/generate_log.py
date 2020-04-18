import time

c = 0
while True:
        f = open('somefile.txt','a')
        f.write("line "+str(c)+ "\n")
        c += 1
        f.close()
        time.sleep(1)

