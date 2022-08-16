'''
Created on 20220812
@author: infilink_Jimmy
'''
import modbus_tk
import modbus_tk.defines as cst
import modbus_tk.modbus_tcp as modbus_tcp
import struct
import paho.mqtt.client as mqtt
import random
import json  
import datetime 
import time
import schedule

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

def conver32(LSB,MSB):
    conv32value = LSB + ( MSB << 16 )
    return (conv32value)



def getMainPower(HOST_Addr):
    
    try:
        MainSysPower = [0,0,0,0,0,0,0,0,0,0,0,0]
        master = modbus_tcp.TcpMaster(host=HOST_Addr)
        master.set_timeout(5.0)
        demo1 = master.execute(1, cst.READ_HOLDING_REGISTERS, 1, 24)
        for i in range(12):
            MainSysPower[i] = conver32(demo1[i*2],demo1[i*2+1])
            
        MainSysPayload = {"MainSysPower01" : MainSysPower[0]*0.1,
                          "MainSysPower02" : MainSysPower[1]*0.1,
                          "MainSysPower03" : MainSysPower[2]*0.1,
                          "MainSysPower04" : MainSysPower[3]*0.1,
                          "MainSysPower05" : MainSysPower[4]*0.1,
                          "MainSysPower06" : MainSysPower[5]*0.001,
                          "MainSysPower07" : MainSysPower[6]*0.001,
                          "MainSysPower08" : MainSysPower[7]*0.1,
                          "MainSysPower09" : MainSysPower[8]*0.001,
                          "MainSysPower10" : MainSysPower[9]*0.1,
                          "MainSysPower11" : MainSysPower[10]*0.01,
                          "MainSysPower12" : MainSysPower[11]*0.1, }
    except:
        MainSysPayload = {"MainSysPower01" : 9999,
                          "MainSysPower02" : 9999,
                          "MainSysPower03" : 9999,
                          "MainSysPower04" : 9999,
                          "MainSysPower05" : 9999,
                          "MainSysPower06" : 9999,
                          "MainSysPower07" : 9999,
                          "MainSysPower08" : 9999,
                          "MainSysPower09" : 9999,
                          "MainSysPower10" : 9999,
                          "MainSysPower11" : 9999,
                          "MainSysPower12" : 9999, }
    #print (MainSysPayload)
    return MainSysPayload

def SendMainSystem01(token,IPaddr):
    try:
        client1 = mqtt.Client()
        client1.username_pw_set("53JeWDHVqEqiWnHtP0Vx"," ")
        client1.connect("thingsboard.cloud", 1883, 60)
        print(client1.publish("v1/devices/me/telemetry", json.dumps(getMainPower('192.168.50.6'))))
    except:
        pass
    
def SendMainSystem02(token,IPaddr):
    try:
        client2 = mqtt.Client()
        client2.username_pw_set("YG1RNWgn8YEIGK7YFnId"," ")
        client2.connect("thingsboard.cloud", 1883, 60)
        print(client2.publish("v1/devices/me/telemetry", json.dumps(getMainPower('192.168.50.7'))))
    except:
        pass
    
def SendMainSystem03(token,IPaddr):
    try:
        client3 = mqtt.Client()
        client3.username_pw_set("PXShUefr1Utw13cfXzr1"," ")
        client3.connect("thingsboard.cloud", 1883, 60)
        print(client3.publish("v1/devices/me/telemetry", json.dumps(getMainPower('192.168.50.8'))))
    except:
        pass
def sendBatteryOP(num,ID):
    try:
        client3 = mqtt.Client()
        client3.username_pw_set("1AZnqejWVF8cm3BBy6xg"," ")
        client3.connect("thingsboard.cloud", 1883, 60)
        print(client3.publish("v1/devices/me/telemetry", json.dumps(getBatteryOP('192.186.50.6'))))
    except:
        pass
    
def getBatteryOP(HOST_Addr):
    try:
        clientB01 = mqtt.Client()
        clientB01.username_pw_set("1AZnqejWVF8cm3BBy6xg"," ")
        clientB01.connect("thingsboard.cloud", 1883, 60)
        
        master = modbus_tcp.TcpMaster(host=HOST_Addr)
        master.set_timeout(100.0)
        battery01 = master.execute(1, cst.READ_HOLDING_REGISTERS, 801, 100)
        time.sleep(2)
        
        for i in range(10):
           battery01payload={str(i)+"stBatterystateofcharge" : battery01[i*10],
                   str(i)+"stBatteryPackWarningFlag" : conver32(battery01[i*10+1],battery01[i*10+2]),
                   str(i)+"stBatteryCurrent" : conver32(battery01[i*10+3],battery01[i*10+4]),
                   str(i)+"stBatteryVoltage" : conver32(battery01[i*10+5],battery01[i*10+6]),
                   str(i)+"stHighTemperature" : conver32(battery01[i*10+7],battery01[i*10+8]),
                   str(i)+"stSOH" : battery01[i*10+9]
                   }
           print(battery01payload)
        
        #print(clientB01.publish("v1/devices/me/telemetry", json.dumps(battery01payload)))
        print(battery01payload)
        time.sleep(10)
        battery02 = master.execute(1, cst.READ_HOLDING_REGISTERS, 901, 100)
        time.sleep(2)
        for i in range(10):
           battery01payload={str(10+i)+"stBatterystateofcharge" : battery01[i*10],
                   str(10+i)+"stBatteryPackWarningFlag" : conver32(battery01[i*10+1],battery01[i*10+2]),
                   str(10+i)+"stBatteryCurrent" : conver32(battery01[i*10+3],battery01[i*10+4]),
                   str(10+i)+"stBatteryVoltage" : conver32(battery01[i*10+5],battery01[i*10+6]),
                   str(10+i)+"stHighTemperature" : conver32(battery01[i*10+7],battery01[i*10+8]),
                   str(10+i)+"stSOH" : battery01[i*10+9]
                   }
           print(battery01payload)
        #print(clientB01.publish("v1/devices/me/telemetry", json.dumps(battery01payload)))
        print(battery01payload)
        time.sleep(10)
        battery03 = master.execute(1, cst.READ_HOLDING_REGISTERS, 1001, 100)
        time.sleep(2)
        for i in range(10):
           battery01payload={str(20+i)+"stBatterystateofcharge" : battery01[i*10],
                   str(20+i)+"stBatteryPackWarningFlag" : conver32(battery01[i*10+1],battery01[i*10+2]),
                   str(20+i)+"stBatteryCurrent" : conver32(battery01[i*10+3],battery01[i*10+4]),
                   str(20+i)+"stBatteryVoltage" : conver32(battery01[i*10+5],battery01[i*10+6]),
                   str(20+i)+"stHighTemperature" : conver32(battery01[i*10+7],battery01[i*10+8]),
                   str(20+i)+"stSOH" : battery01[i*10+9]
                   }
           print(battery01payload)
        #print(clientB01.publish("v1/devices/me/telemetry", json.dumps(battery01payload)))
        print(battery01payload)
        time.sleep(10)
        
        
    except:
        pass

def dojob():
    SendMainSystem01("53JeWDHVqEqiWnHtP0Vx",'192.168.50.6')
    time.sleep(5)
    SendMainSystem02("YG1RNWgn8YEIGK7YFnId",'192.168.50.7')
    time.sleep(5)
    SendMainSystem03("PXShUefr1Utw13cfXzr1",'192.168.50.8')
    time.sleep(5)


if __name__ == '__main__':

    while True:
        #getBatteryOP('192.168.50.6')
        #time.sleep(60)
        schedule.every(2).minutes.do(dojob)
        
    