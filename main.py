import threading 
import time
import RPi.GPIO as GPIO ## Import GPIO library
import sys

blink_speed = 1
sleep = time.sleep(blink_speed)

GPIO.setmode(GPIO.BOARD) ## Use board pin numbering

#Btn 1
GPIO.setup(3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) 
GPIO.setup(5, GPIO.OUT) 

#Btn 2
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(29, GPIO.OUT)

#Btn 3
GPIO.setup(31, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(26, GPIO.OUT)

#Btn 4
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(21, GPIO.OUT)

#Btn 2
GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(23, GPIO.OUT)

#Btn 2
GPIO.setup(32, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(33, GPIO.OUT)




def Listen_buttons():
    
    btn_pin_1 = 3
    out_pin_1 = 5
    
    btn_pin_2 = 7
    out_pin_2 = 29
    
    btn_pin_3 = 31
    out_pin_3 = 26
    
    btn_pin_4 = 24
    out_pin_4 = 21
    
    btn_pin_5 = 31
    out_pin_5 = 26
    
    btn_pin_6 = 31
    out_pin_6 = 26
    
    
    while True:
        if GPIO.input(btn_pin_1) == GPIO.LOW:
            
            GPIO.output(out_pin_1,True)
            GPIO.output(out_pin_2,False)
            GPIO.output(out_pin_3,False)
            GPIO.output(out_pin_4,False)
            GPIO.output(out_pin_5,False)
            GPIO.output(out_pin_6,False)
            
        if GPIO.input(btn_pin_2) == GPIO.LOW:
            
            GPIO.output(out_pin_1,False)
            GPIO.output(out_pin_2,True)
            GPIO.output(out_pin_3,False)
            GPIO.output(out_pin_4,False)
            GPIO.output(out_pin_5,False)
            GPIO.output(out_pin_6,False)
            
        if GPIO.input(btn_pin_3) == GPIO.LOW:
            
            GPIO.output(out_pin_1,False)
            GPIO.output(out_pin_2,False)
            GPIO.output(out_pin_3,True)
            GPIO.output(out_pin_4,False)
            GPIO.output(out_pin_5,False)
            GPIO.output(out_pin_6,False)
        
        if GPIO.input(btn_pin_4) == GPIO.LOW:
            
            GPIO.output(out_pin_1,False)
            GPIO.output(out_pin_2,False)
            GPIO.output(out_pin_3,False)
            GPIO.output(out_pin_4,True)
            GPIO.output(out_pin_5,False)
            GPIO.output(out_pin_6,False)
        
        if GPIO.input(btn_pin_5) == GPIO.LOW:
            
            GPIO.output(out_pin_1,False)
            GPIO.output(out_pin_2,False)
            GPIO.output(out_pin_3,False)
            GPIO.output(out_pin_4,False)
            GPIO.output(out_pin_5,True)
            GPIO.output(out_pin_6,False)
        
        if GPIO.input(btn_pin_6) == GPIO.LOW:
            print("works")
            GPIO.output(out_pin_1,False)
            GPIO.output(out_pin_2,False)
            GPIO.output(out_pin_3,False)
            GPIO.output(out_pin_4,False)
            GPIO.output(out_pin_5,False)
            GPIO.output(out_pin_6,True)
                
        
            
            #loop_btn(3, False)
                
            #loop_btn(5, True)
            
        
        #if GPIO.input(8) == GPIO.LOW:
         #   print("btn 2")
          #  loop_btn(29, False)
            #time.sleep(0.2)
            #loop_btn(29, True)
            
            
        
        
       
t1 = threading.Thread(target=Listen_buttons)
t1.start()
t1.join()
print("T1 Start")


