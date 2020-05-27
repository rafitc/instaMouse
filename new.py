import pyautogui as pg 
import keyboard
import time

while True:
	if(keyboard.is_pressed('h')):
		print('Liked photo')
		pg.click(clicks=2)
		time.sleep(0.3)
	if(keyboard.is_pressed('p')):
		print('video played')
		pg.click()
		time.sleep(0.3)


