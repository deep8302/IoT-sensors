import RPi.GPIO as rp
import time
rp.setwarnings(False)
rp.setmode(rp.BOARD)
rp.setup(7, rp.OUT)
rp.setup(11,rp.IN)
while(1):
    rp.output(7,1)
    time.sleep(0.0001)
    rp.output(7,0)
    while(rp.input(11)==0):
        pass
    st=time.time()
    while(rp.input(11)==1):
        pass
    sot=time.time()
    t=sot-st
    d=(34300*t)/2
    print('Object is at distance',d,'cm')
    time.sleep(2)

'''c=0
while(1):
    d=distance()
    if(d<10):
        while(d<10):
            d=distance()
        c=c+1
    print('NO. OF OBJECTS PASSED',c)'''
