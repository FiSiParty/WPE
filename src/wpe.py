import minimalmodbus
import serial
import paho.mqtt.publish as publish
import logging
import time
import URRouterInfo
from URMessageChannel import TimerEvtHandle, init_base, logconfig
import struct

instrument = minimalmodbus.Instrument('/dev/ttymxc2', 1)  # port name, slave address (in decimal)
instrument.serial.baudrate = 9600         # Baud
instrument.serial.bytesize = 8
instrument.serial.parity   = serial.PARITY_NONE
instrument.serial.stopbits = 1
instrument.serial.timeout  = 1.0          # seconds
instrument.close_port_after_each_call = True
instrument.address                         # this is the slave address number
instrument.mode = minimalmodbus.MODE_RTU   # rtu or ascii mode
instrument.clear_buffers_before_each_transaction = True
ServName = "siamgreenergy.com"
port = 1883
auth = {
    'username':'sgnserver',
    'password':'055280077'
}



def Sent_toServer():
    x = 0
    list_A = []
    while(x<8):
        if(x == 0): #1 Voltage
            try:
                try:
                    ad1 = 1
                    result1 = instrument.read_register(ad1-1,0,4,False)  #Uint32/1
                    result2 = instrument.read_register(ad1,0,4,False)
        
                    r = [result2] + [result1] #[Uint32/2, Uint32/1]
                      
                except AttributeError:
                    print("!!!!!!!!!!!!!!!!AttributeError Try Again!!!!!!!!!!!!!!!!")
                    Sent_toServer()
            except minimalmodbus.NoResponseError:
                print("!!!!!!!!!!!!!!NoResponseError Try Again!!!!!!!!!!!!!!!!")
                Sent_toServer()
            #print(r)
            b=struct.pack('HH',r[0],r[1]) 
            ans=struct.unpack('f',b)[0]
            ans = '%.2f'%ans
            list_A.append(ans)
            
        if(x == 1): #7 Current
            try:
                try:
                    ad1 = 7
                    result1 = instrument.read_register(ad1-1,0,4,False)  #Uint32/1
                    result2 = instrument.read_register(ad1,0,4,False)
        
                    r = [result2] + [result1] #[Uint32/2, Uint32/1]
    
                except AttributeError:
                    print("!!!!!!!!!!!!!!!!AttributeError Try Again!!!!!!!!!!!!!!!!")
                    Sent_toServer()
            except minimalmodbus.NoResponseError:
                print("!!!!!!!!!!!!!!NoResponseError Try Again!!!!!!!!!!!!!!!!")
                Sent_toServer()
            #print(r)
            b=struct.pack('HH',r[0],r[1]) 
            ans=struct.unpack('f',b)[0]
            ans = '%.2f'%ans
            list_A.append(ans)
        if(x == 2): #13 Active power
            try:
                try:
                    ad1 = 13
                    result1 = instrument.read_register(ad1-1,0,4,False)  #Uint32/1
                    result2 = instrument.read_register(ad1,0,4,False)
        
                    r = [result2] + [result1] #[Uint32/2, Uint32/1]
                    
                except AttributeError:
                    print("!!!!!!!!!!!!!!!!AttributeError Try Again!!!!!!!!!!!!!!!!")
                    Sent_toServer()
            except minimalmodbus.NoResponseError:
                print("!!!!!!!!!!!!!!NoResponseError Try Again!!!!!!!!!!!!!!!!")
                Sent_toServer()
            #print(r)
            b=struct.pack('HH',r[0],r[1]) 
            ans=struct.unpack('f',b)[0]
            ans = '%.2f'%ans
            list_A.append(ans)
        if(x == 3): #31 Power factor
            try:
                try:
                    ad1 = 31
                    result1 = instrument.read_register(ad1-1,0,4,False)  #Uint32/1
                    result2 = instrument.read_register(ad1,0,4,False)
        
                    r = [result2] + [result1] #[Uint32/2, Uint32/1]
                    
                except AttributeError:
                    print("!!!!!!!!!!!!!!!!AttributeError Try Again!!!!!!!!!!!!!!!!")
                    Sent_toServer()
            except minimalmodbus.NoResponseError:
                print("!!!!!!!!!!!!!!NoResponseError Try Again!!!!!!!!!!!!!!!!")
                Sent_toServer()
            #print(r)
            b=struct.pack('HH',r[0],r[1]) 
            ans=struct.unpack('f',b)[0]
            ans = '%.2f'%ans
            list_A.append(ans)
        if(x == 4): #71 Frequency
            try:
                try:
                    ad1 = 71
                    result1 = instrument.read_register(ad1-1,0,4,False)  #Uint32/1
                    result2 = instrument.read_register(ad1,0,4,False)
        
                    r = [result2] + [result1] #[Uint32/2, Uint32/1]
                    
                except AttributeError:
                    print("!!!!!!!!!!!!!!!!AttributeError Try Again!!!!!!!!!!!!!!!!")
                    Sent_toServer()
            except minimalmodbus.NoResponseError:
                print("!!!!!!!!!!!!!!NoResponseError Try Again!!!!!!!!!!!!!!!!")
                Sent_toServer()
            #print(r)
            b=struct.pack('HH',r[0],r[1]) 
            ans=struct.unpack('f',b)[0]
            ans = '%.2f'%ans
            list_A.append(ans)
            
        if(x == 5): #73
            try:
                try:
                    ad1 = 73
                    result1 = instrument.read_register(ad1-1,0,4,False)  #Uint32/1
                    result2 = instrument.read_register(ad1,0,4,False)
        
                    r = [result2] + [result1] #[Uint32/2, Uint32/1]
                    
                except AttributeError:
                    print("!!!!!!!!!!!!!!!!AttributeError Try Again!!!!!!!!!!!!!!!!")
                    Sent_toServer()
            except minimalmodbus.NoResponseError:
                print("!!!!!!!!!!!!!!NoResponseError Try Again!!!!!!!!!!!!!!!!")
                Sent_toServer()
            #print(r)
            b=struct.pack('HH',r[0],r[1]) 
            ans=struct.unpack('f',b)[0]
            ans = '%.2f'%ans
            ans = float(ans)
            list_A.append(ans)
            
        if(x == 6): #75 Import active energy
            try:
                try:
                    ad1 = 75
                    result1 = instrument.read_register(ad1-1,0,4,False)  #Uint32/1
                    result2 = instrument.read_register(ad1,0,4,False)
        
                    r = [result2] + [result1] #[Uint32/2, Uint32/1]
                    
                except AttributeError:
                    print("!!!!!!!!!!!!!!!!AttributeError Try Again!!!!!!!!!!!!!!!!")
                    Sent_toServer()
            except minimalmodbus.NoResponseError:
                print("!!!!!!!!!!!!!!NoResponseError Try Again!!!!!!!!!!!!!!!!")
                Sent_toServer()
            #print(r)
            b=struct.pack('HH',r[0],r[1]) 
            ans=struct.unpack('f',b)[0]
            ans = '%.2f'%ans
            list_A.append(ans)

        
        if(x == 7): #343 Total active energy
           try:
               try:
                   ad1 = 343
                   result1 = instrument.read_register(ad1-1,0,4,False)  #Uint32/1
                   result2 = instrument.read_register(ad1,0,4,False)

                   r = [result2] + [result1]  #[Uint32/2, Uint32/1]
               except AttributeError:
                   print("!!!!!!!!!!!!!!!!AttributeError Try Again!!!!!!!!!!!!!!!!")
                   Sent_toServer() 
           except minimalmodbus.NoResponseError :
               print("!!!!!!!!!!!!!!NoResponseError Try Again!!!!!!!!!!!!!!!!")
               Sent_toServer()
           #print(r)
           b=struct.pack('HH',r[0],r[1]) 
           ans=struct.unpack('f',b)[0]
           ans = '%.2f'%ans
           list_A.append(ans)

        #print('x = ',x)
        x+=1
        
    # out loop    
    #print(list_A)
    
    allans = 'V = '+str(list_A[0])+', '+'I = '+str(list_A[1])+', '+'W = '+str(list_A[2])+', '+'PF = '+str(list_A[3])+', '+'Hz = '+str(list_A[4])+', '+'IAE kWh = '+str(list_A[5])+', '+'EAE kWh = '+str(list_A[6])+', '+'TAE kWh = '+str(list_A[7])
    print("Sending .....",allans)
    publish.single("ur32/egat/wl/007",allans, hostname=ServName, port=port, auth=auth)
    #return allans
    



        
