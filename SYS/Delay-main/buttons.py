import RPi.GPIO as GPIO ## Import GPIO library
import time
import tcp
import subprocess
import threading 

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BOARD) ## Use board pin numbering


input_pins = [5, 7, 29]
output_pins = [31, 26, 24]

for x in input_pins:
    print("Input Pins:", x)
    GPIO.setup(x, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    
for y in output_pins:
    print("Output Pins:", y)
    GPIO.setup(y, GPIO.OUT)
    
for z in input_pins:
    print("Input Status:", GPIO.input(z))
    
    
    
    
##################################
def control_vlc():
    tcp.VLC_control.msg()
    

    
time.sleep(2)

samsung_ctrl = tcp.Samsung_control

def screen_init():
    print("Turning Screen on")
    samsung_ctrl.Samsung_On()
screen_init()
#


def VLC_zero():
    subprocess.Popen([
    "killall", "-e", "vlc"
    ])
    print("Kill VLC")
    time.sleep(2)
    #subprocess.Popen([
    #"vlc",
    #"--intf",
    #"rc",
    #"--rc-host", "192.168.10.130:50000"
    #])
    print("Start VLC")
VLC_zero()

def minimum():
    subprocess.Popen([
    "killall", "-e", "vlc"
    ])
    print("Kill VLC")
    time.sleep(2)
    subprocess.Popen([
    "vlc", "-I", "dummy", "-f", "--intf",
    
    "rc",
    "--rc-host", "127.0.0.1:50000",
     "rtsp://admin:ms1234@192.168.10.10:554/"
    #"--network-caching", "10000", "rtsp://192.168.10.211:8554/"
    ])
    print("Start VLC")
    
def low():
    subprocess.Popen([
    "killall", "-e", "vlc"
    ])
    print("Kill VLC")
    time.sleep(2)
    subprocess.Popen([
    "vlc", "-I", "dummy","-f", "--network-caching", "20000", "rtsp://admin:ms1234@192.168.10.10:554/"
    #"--intf",
    #"rc",
    #"--rc-host", "192.168.10.130:50000"
    ])
    print("Start VLC")
    
def medium():
    subprocess.Popen([
    "killall", "-e", "vlc"
    ])
    print("Kill VLC")
    time.sleep(2)
    subprocess.Popen([
    "vlc", "-I", "dummy","-f", "--network-caching", "30000", "rtsp://admin:ms1234@192.168.10.10:554/"
    #"--intf",
    #"rc",
    #"--rc-host", "192.168.10.130:50000"
    ])
    print("Start VLC")
    
def ButtonFeedback():
    #if y = 
    GPIO.output(output_pins[0],True)
    GPIO.output(output_pins[1],False)
    GPIO.output(output_pins[2],False)
    #GPIO.output(output_pins[3],False)
    #GPIO.output(output_pins[4],False)
    #GPIO.output(output_pins[5],False)
    
#def ScreenControl(state):
    
    #samsung_ctrl.Samsung_state()
    
               
    
    
def Listen_buttons():
    while True:
        
        #Button 1
        if GPIO.input(input_pins[0]) == GPIO.LOW:
            print("btn 1")
            time.sleep(0.1)
            t2 = threading.Thread(target=minimum)
            t2.start()
                
                
                            
        #Button 2
        if GPIO.input(input_pins[1]) == GPIO.LOW:
            print("btn 2")
            time.sleep(0.1)
            t2 = threading.Thread(target=low)
            t2.start()
                
                
        
        #Button 3
        if GPIO.input(input_pins[2]) == GPIO.LOW:
            time.sleep(0.1)
            if GPIO.input(input_pins[2]) == GPIO.LOW:
                print("btn 3")
                GPIO.output(output_pins[0],False)
                GPIO.output(output_pins[1],False)
                GPIO.output(output_pins[2],True)
                samsung_ctrl.Samsung_On()
                #tcp.VLC_control.normal()
                #t4 = threading.Thread(target=VLC_thirdty)
                #t4.start()
                #VLC_thirdty()
                tcp.VLC_control.slower()
                #control_vlc()
                #GPIO.output(output_pins[3],False)
                #GPIO.output(output_pins[4],False)
                #GPIO.output(output_pins[5],False)
            
       
        #if GPIO.input(btn_pin_3) == GPIO.LOW:
            #time.sleep(0.2)
            #if GPIO.input(btn_pin_3) == GPIO.LOW:
              #  print("btn 3")
              #  GPIO.output(out_pin_1,False)
              #  GPIO.output(out_pin_2,False)
              #  GPIO.output(out_pin_3,True)
                
                #GPIO.output(out_pin_4,False)
                #GPIO.output(out_pin_5,False)
                #GPIO.output(out_pin_6,False)
        
        #if GPIO.input(btn_pin_4) == GPIO.LOW:
         #   time.sleep(0.2)
          #  if GPIO.input(btn_pin_4) == GPIO.LOW:
           #     print("btn 4")
            #    print(GPIO.input(btn_pin_4))
                #GPIO.output(out_pin_1,False)
                #GPIO.output(out_pin_2,False)
                #GPIO.output(out_pin_3,False)
                #GPIO.output(out_pin_4,True)
                #GPIO.output(out_pin_5,False)
                #GPIO.output(out_pin_6,False)
        
        #if GPIO.input(btn_pin_5) == GPIO.LOW:
            #print("btn 5")
            #GPIO.output(out_pin_1,False)
            #GPIO.output(out_pin_2,False)
            #GPIO.output(out_pin_3,False)
            #GPIO.output(out_pin_4,False)
            #GPIO.output(out_pin_5,True)
            #GPIO.output(out_pin_6,False)
        
        #if GPIO.input(btn_pin_6) == GPIO.LOW:
            #print("btn 6")
            #GPIO.output(out_pin_1,False)
            #GPIO.output(out_pin_2,False)
            #GPIO.output(out_pin_3,False)
            #GPIO.output(out_pin_4,False)
            #GPIO.output(out_pin_5,False)
            #GPIO.output(out_pin_6,True)
                
        
        
        
       
t1 = threading.Thread(target=Listen_buttons)
t1.start()

print("T1 Start")
