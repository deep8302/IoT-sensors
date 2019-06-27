#import RPi.GPIO as rp
#rp.setmode(rp.BOARD)

l=[7,11,13,15,19,21,23]
#for i in range(0,len(l)):
 #           rp.setup(l[i],rp.OUT)
def zero():
    while(1):
        print('ZERO')
        '''rp.output(7,0)
        rp.output(11,0)
        rp.output(13,0)
        rp.output(15,0)
        rp.output(190)
        rp.output(21,0)
        rp.output(23,0)'''

def one():
    while(1):
        print('ONE')
       ''' rp.output(7,0)
        rp.output(11,0)
        rp.output(13,0)
        rp.output(15,0)
        rp.output(19,0)
        rp.output(21,0)
        rp.output(23,0)'''

def two():
    while(1):
        print('TWO')
       '''rp.output(7,0)
        rp.output(11,0)
        rp.output(13,0)
        rp.output(15,0)
        rp.output(190)
        rp.output(21,0)
        rp.output(23,0)'''
            
def three():
    while(1):
        print('THREE')
        '''rp.output(7,0)
        rp.output(11,0)
        rp.output(13,0)
        rp.output(15,0)
        rp.output(190)
        rp.output(21,0)
        rp.output(23,0)'''

def four():
    while(1):
        print('FOUR')
     '''   rp.output(7,0)
        rp.output(11,0)
        rp.output(13,0)
        rp.output(15,0)
        rp.output(190)
        rp.output(21,0)
        rp.output(23,0)'''

def five():
    while(1):
        print('FIVE')
      '''  rp.output(7,0)
        rp.output(11,0)
        rp.output(13,0)
        rp.output(15,0)
        rp.output(190)
        rp.output(21,0)
        rp.output(23,0)'''

def six():
    while(1):
        print('SIX')
      '''  rp.output(7,0)
        rp.output(11,0)
        rp.output(13,0)
        rp.output(15,0)
        rp.output(190)
        rp.output(21,0)
        rp.output(23,0)'''

def seven():
    while(1):
        print('SEVEN')
       ''' rp.output(7,0)
        rp.output(11,0)
        rp.output(13,0)
        rp.output(15,0)
        rp.output(190)
        rp.output(21,0)
        rp.output(23,0)'''

def eight():
    while(1):
        print('EIGHT')
     '''   rp.output(7,0)
        rp.output(11,0)
        rp.output(13,0)
        rp.output(15,0)
        rp.output(190)
        rp.output(21,0)
        rp.output(23,0)'''

def nine():
    while(1):
        print('NINE')
      '''  rp.output(7,0)
        rp.output(11,0)
        rp.output(13,0)
        rp.output(15,0)
        rp.output(190)
        rp.output(21,0)
        rp.output(23,0)'''

ch=int(input("ENTER ANY NUMBER FROM 0 To 9\n"))
lf=[zero(),one(),two(),three(),four(),five(),six(),seven(),eight(),nine()]
lf[ch]
