#!/usr/bin/python
# using test unit 420.2-231-94DC6692F976
import serial, time

import test_support

class barcode:
    def __init__ (self):
        self.partNumber=""
        self.workOrder=""
        self.HWID=""

class DeviceTest:
    def __init__ (self):
        self.partNumber=""
        self.workOrder=""
        self.FWARE=""
        self.battery=""
        self.minRssi=""
        self.calOffset=""
        self.comm=""
        self.baud=""
 
 
def init_values(test):
    test.partNumber=420.2
    test.workOrder=231
    test.FWARE=193
    test.battery=6000
    test.minRssi=0
    test.calOffset=38
    test.comm="COM5" 

def u2(x):
    if x & 0x80: # MSB set -> neg.
        return -((~x & 0xff) + 1)
    else:
        return x

# the following routines parse data fields from the serial response 
# returned from the nRF tester

def get_address():
    inp =ser.read(18)
    response=""
    ret=""
    for x  in range(0,18):     
        if inp[x]!=" " :
            response=response + inp[x] 
    for x in range(1,12,2):
        ret=ret+response[-(x+1)]
        ret=ret+response[-x]      
    print ( 'Address detected:', ret)
    return (ret)

def get_fware():
    response=int(ser.read(5),16)
    print'Fware=',response
    return(response)

def get_device():
    response=ser.read(3)
    print"Device type:",response
    return response
    
def get_rssi():
#    sp=ser.read(1)
    rssi=int(ser.read(3),16)
    if rssi & 128:
        rssi=hex(rssi ^ 128)
        rssi = int(rssi,16)-128
    print "rssi=",  rssi
    return(rssi)

def get_battery():
    batt=int(ser.read(5),16)
    print"Battery (mv)= ", batt
    return(batt)
     
def get_test():
    test=ser.read(3)
    print"self test:",test
    return(test)
                 



def get_product_barcode(UUT):
    info = bytes(raw_input("Place Unit on fixture and scan barcode to begin..."))
    for x in range(0,5):
        UUT.partNumber = UUT.partNumber + info[x]       
    for x in range(6,9):
        UUT.workOrder = UUT.workOrder + info[x]
    for x in range(10,22):
        UUT.HWID = UUT.HWID + info[x]
    print  "Product: ", UUT.partNumber
    print "Work Order: ", UUT.workOrder
    print "HWID: ", UUT.HWID
    return info






if __name__ == "__main__":
    print("pySSFunctional Test Program")
    
    
    test=DeviceTest()
    UUT=barcode()
    
    
    init_values(test)
    
    

#UUT = raw_input("Place Unit on fixture and scan barcode to begin...")

get_product_barcode(UUT)
print "Testing unit with HWID", UUT.HWID


#initialization and open the port

#possible timeout values:
#    1. None: wait forever, block call
#    2. 0: non-blocking mode, return immediately
#    3. x, x is bigger than 0, float allowed, timeout block call

search_timeout = 35

ser = serial.Serial()
ser.port = test.comm
ser.baudrate = 115200
ser.bytesize = serial.EIGHTBITS #number of bits per bytes
ser.parity = serial.PARITY_NONE #set parity check: no parity
ser.stopbits = serial.STOPBITS_ONE #number of stop bits
#ser.timeout = None          #block read
ser.timeout = search_timeout     #non-block read
#ser.timeout = 2              #timeout block read
ser.xonxoff = False     #disable software flow control
ser.rtscts = False     #disable hardware (RTS/CTS) flow control
ser.dsrdtr = False       #disable hardware (DSR/DTR) flow control
ser.writeTimeout = 2     #timeout for write




try: 
    ser.open()
except Exception, e:
    print "error open serial port: " + str(e)
    exit()

if ser.isOpen():

    try:
        ser.flushInput() #flush input buffer, discarding all its contents
        ser.flushOutput()#flush output buffer, aborting current output 
                                 #and discard all that is in buffer

        #write data
        ser.write("G")
        print("write data: G")

        time.sleep(0.5)  #give the serial port sometime to receive the data
        test_end=0
        
        response=ser.read(2)
        if (response!="$S"):
            print("Test did not start properly")
            test_end=1
        print("Test starting on a "+response)
              
        while True:

            if(test_end ==1):
                break
            
            response=ser.read(2)
            
            if(response=="$F"):
                print("Unit not found")
                break
            
            if(response=="$A"):
                da=get_address()
                if UUT.HWID!=da:
                    print "**ERROR**"
                    print "Looking for",UUT.HWID
                    print "Found",da
                    test_end=1
                else:
                    print "Unit "+  UUT.HWID +" found"
                pass
            
            if(response=="$D"):
                dev=get_device()
                pass
            
            if(response=="$W"):
                fware=get_fware()
                if fware != test.FWARE:
                    print "**ERROR**"
                    print "Device has rev %d firmware instead of rev %d." % (fware, test.FWARE)
                    test_end=1
                pass
            
            if(response=="$R"):
                rssi=get_rssi()+test.calOffset
                if rssi  < test.minRssi:
                    print "**ERROR**"
                    print "Device RSSI of %d dbm not greater than %d dbm min" %(rssi, test.minRssi)
                    test_end=1                                     
                pass
            
            if(response=="$B"):
                batt=get_battery()               
                pass
            
            if(response=="$V"):
                test=get_test()
                break                                          
           
        ser.close()
        print("Close port")
        
    except Exception, e1:
        print "error communicating...: " + str(e1)
        if(ser.isOpen()):
            ser.close()            
else:
    print "cannot open serial port "
