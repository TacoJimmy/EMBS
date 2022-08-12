'''
Created on 2022/08/11
@author: NTUT
'''
# coding:utf-8
import codecs

import paho.mqtt.client as mqtt
import random
import json  
import datetime 
import time
import struct


i = [40801,40802,40803,40804,40805,40806,40807,40808,40809,40810]

def ReadFloat(*args,reverse=False):
    for n,m in args:
        n,m = '%04x'%n,'%04x'%m
    if reverse:
        v = n + m
    else:
        v = m + n
    y_bytes = bytes.fromhex(v)
    y = struct.unpack('!f',y_bytes)[0]
    y = round(y,6)
    return y

def get_ModbusTCP():
    
    #master = modbus_tcp.TcpMaster(host="192.168.50.6")
    #master.set_timeout(5.0)
    #demo1 = master.execute(3, cst.READ_HOLDING_REGISTERS, 1, 2)
    
    #print(ReadFloat((demo1[1], demo1[0])))
    
    #master = modbus_tcp.TcpMaster(host="192.168.50.6")
    #master.set_timeout(5.0)
    #demo1 = master.execute(3, cst.READ_HOLDING_REGISTERS, 40801, 599)
    
    
    
    #print(ReadFloat((demo1[1], demo1[0])))
    
    print(ReadFloat((7, 6)))

def getMainData():
    
    a2 = i[0]
    b2 = i[1]+i[2]
    c2 = i[3]+i[4]
    d2 = i[5]+i[6]
    e2 = i[7]+i[8]
    f2 = i[9]
    
    a1 = 0
    b1 = 0
    c1 = 0
    d1 = 0
    e1 = 0
    f1 = 0
    
    for j in range(1):
       
        
        'a'+str(j) = i[j*10 + 0]
        'b'+str(j) = i[j*10 + 1]
        'c'+str(j) = i[j*10 + 3]
        'd'+str(j) = i[j*10 + 5]
        'e'+str(j) = i[j*10 + 7]
        'f'+str(j) = i[9] 
    
    print (a1,b1,c1,d1,e1,f1)
    print (a2,b2,c2,d2,e2,f2)

def battery():
    
    for i in range(0,90):
        
        BTC = 5001 + i*6
        BPF = 5002 + i*6
        BC = 5003 + i*6
        BV = 5004 + i*6
        HT = 5005 + i*6
        SOH = 5006 + i*6
        
        pets={"BatteryID"+str(i):
                    {str(i)+"stBatterystateofcharge" : BTC,
                    str(i)+"stBatteryPackWarningFlag" : BPF,
                    str(i)+"stBatteryCurrent" : BC,
                    str(i)+"stBatteryVoltage" : BV,
                    str(i)+"stHighTemperature" : HT,
                    str(i)+"stSOH" : SOH
                       }}
        print (pets)
        
        time.sleep(1)
    


if __name__ == '__main__':
    while True:
        getMainData()
        time.sleep(5)