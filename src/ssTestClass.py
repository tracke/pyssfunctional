#!/usr/bin/python
# using test unit 420.2-231-94DC6692F976
import serial, time

from ConfigParser import SafeConfigParser

def getWorkOrder(db):
    pass


def checkBarcodeData(info):       
    UUT.clear()
    if len(info)<22:
        print "Bar Code Length Error"
        return UUT
    for x in range(0,5):
        UUT.partNumber = UUT.partNumber + info[x]       
    for x in range(6,9):
        UUT.workOrder = UUT.workOrder + info[x]
    for x in range(10,22):
        UUT.HWID = UUT.HWID + info[x]    
    print  "Product: ", UUT.partNumber
    print "Work Order: ", UUT.workOrder
    print "HWID: ", UUT.HWID
    return UUT
 
          
class barcode(object):
    def __init__ (self):
        self.partNumber=""
        self.workOrder=""
        self.HWID=""
        
    def clear(self):
        self.partNumber=""
        self.workOrder=""
        self.HWID=""
        


class TestStation(object):
    def __init__(self):
        self.config_file="test_station.ini"
        self.stationID= "0"
        self.locationID = "0"
        self.onSitePC = "LocationPC1"
        self.revision = 1.0
         
    def initialize(self):
        parser=SafeConfigParser()
        if parser.read(self.config_file):
            if parser.has_section('test_station'):                
                self.stationID = parser.get('test_station','id')
                self.locationID= parser.get('test_station','location' )
                self.revision = parser.get('test_station','revision')
            else:
                return "file "+self.config_file+" has bad format - Test Station NOT Initialized"
            return "Test Station " + self.stationID + " at  " + self.locationID + " initialized"
        return "could not find test_station.ini - Test Station NOT Initialized"
        
             
    def register(self, id, rev, loc):
        #Contact DB and add an entry for this new Test Station
        pass
         


class DeviceTest(object):
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

UUT=barcode()

def runTest(object):
    
    pass

mesh_devices = ['unknown', 'Comm Hub', 'Location Hub', 'Hygiene Sensor']  #Device Types 0, 1, 2, 3



