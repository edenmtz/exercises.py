#!/usr/bin/python
## Second Problem




messages = open("/var/log/messages")
tmp = ""
count=1
for line in messages:
    
    minute = line [0:12]
    
    if  minute == tmp:
        count += 1
    else:
        print minute + "," + str(count)
        count = 1
        tmp = ""
    tmp =  minute
