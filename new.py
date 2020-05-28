import pyautogui as pg 
import keyboard
import time

while True: #for infinite loop
	if(keyboard.is_pressed('h')): #checking pressed key is "h"
		print('Liked photo')
		pg.click(clicks=2) #Two click neededd for like a post
		time.sleep(0.3)	#To avoid multiple entry 
	if(keyboard.is_pressed('p')): #checking pressed key is "p"
		print('video played')
		pg.click()
		time.sleep(0.3)	#To avoid multiple entry 


