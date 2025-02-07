# Copyright (c) 2025 Thomas Duggan
# This work is licensed under CC BY-SA 4.0


from engi1020.arduino.api import *
from time import sleep

oled_clear()			# <
buzzer_stop				# < Resets system after launch
digital_write(4,False)	# <
buzzer_active = True	# <


while True:
    threshold  = analog_read(0)
    threshold = int(threshold/8) #Reduces sensitivity of dial
    print(threshold)
     
    oled_print("Temp Threshold:")
    oled_print(threshold)
    oled_print("Hold D6")  #Hold due to sleep function
    oled_print("to select")
    
    sleep(0.5)
    oled_clear()
    
    pressed = digital_read(6)
    if pressed == True:
        break
    
print ("Threshold is",threshold)

oled_clear()
oled_print("Temp Threshold:")
oled_print(threshold)
oled_print(" ")
oled_print("Value Selected!")
sleep(2)


while 1 > 0: # same as while:True for Q3
    temp = pressure_get_temp()
    # print ("temperature=",temp)
    
    press1 = pressure_get_pressure()
    alti1 = pressure_get_altitude() 
    sleep(0.5)
    press2 = pressure_get_pressure()	#Finds the difference between values over time
    alti2 = pressure_get_altitude()
    press_diff = int(press2 - press1)
    alti_diff = int(alti2 - alti1)
    
    print ("pressure difference=", press_diff)
    print ("altitude difference=", alti_diff)   
    
    if buzzer_active == False:
        buzzer_stop(5)
        digital_write(4,False)
    
    if temp > threshold :
        while buzzer_active == True:
            oled_clear()
            oled_print("Temp Threshold:")
            oled_print(threshold)
            oled_print(" ")
            oled_print("VALUE SURPASSED!")
        
            if buzzer_active == True:
               buzzer_frequency(5,30)
               digital_write(4,True)

            button = digital_read(6)	#Disables buzzer
            if button == True:
                buzzer_active = False
        
    else:
        if (temp > 15) and (press_diff == 0) and (alti_diff ==0):
            oled_clear() 
            oled_print("Temp Threshold:")
            oled_print(threshold)
            oled_print("Weather is:")
            oled_print("Sunny")
            
        elif (temp > 0) and (press_diff < 0) and (alti_diff < 0):
            oled_clear()
            oled_print("Temp Threshold:")
            oled_print(threshold)
            oled_print("Weather is:")
            oled_print("Rainy")
        else:
            oled_clear()
            oled_print("Temp Threshold:")
            oled_print(threshold)
            oled_print("Weather is:")
            oled_print("NOT ENOUGH DATA!")
        
        
        
        
        
        
        