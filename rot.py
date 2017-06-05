import sys
import getopt

#Help message -h
def helpmsg():
    print ("Usage: rot.py -k <key> [-e,-d] -s <message>")
    print ("  -k ROT Key 0-25")
    print ("  [-e,-d] Encrypt/Decrypt")
    print ("  -s String to pass into the cipher")

try:
    opts, argu = getopt.getopt(sys.argv[1:],"k:eds:h")
except getopt.GetoptError:
    print ("GET OPT ERROR")
    sys.exit(3)

#initialse all sys args 
for opt, val in opts:
    if opt == '-h':
        helpmsg()
        sys.exit(0)
    elif opt == '-k':
        k=int(val) # ROT(x) value
    elif opt == '-e':
        mode = 'enc' #Encrypt mode
    elif opt == '-d':
        mode = 'dec' #Decrypt mode
    elif opt == '-s':
        msg = val #Messgae
    else:
        print ('Invalid option: ',opt)
        sys.exit(2)
 
#Check things are set, multiple "trys" ensure all error messages are displayed
try:
    msg
except NameError:    
    print ('String -s not set')
    error = 1
 
try:
    mode
except NameError:  
    print ('Mode not set, use -e for encryption or -d for decryption')
    error = 1

try:
    if k not in range(26):
        print (k)
        print ('k value needs to be between 0 and 25')
        error = 1
except NameError:
    print ('Key (-k) value not set')
    error = 1

try:
    if error == 1:
        sys.exit(2)
except:
    pass

if mode == 'dec':
    k = -k

def cryptchar(x,k):
    if 97<= ord(x) <= 122: #If x is lowercase
        y=((ord(x)-97+k) % 26)+97
        return chr(y)
    elif 65 <= ord(x) <= 90: #If x is uppercase
        y=((ord(x)-65+k) % 26)+65
        return chr(y)
    else:
        return x #Ignore punctuation: spaces "!" "," "." etc.

out=""
for x in msg:
    out += cryptchar(x,k)

print (out)