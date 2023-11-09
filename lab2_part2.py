from asyncio import sleep
from pycreate2 import Create2
import time


"""
This function keeps the robot moving forward and following the right wall of the labyrinth.

Its goal is to keep the robot close to the right wall and follow it along the labyrinth. 

The robot stops once it senses a wall in its front, right and left light bumper sensors.
"""
def run(bot, stop):
    
    sensors = bot.get_sensors()
    
    light_bumper = sensors.light_bumper
    light_bumper_right = sensors.light_bumper_right
    light_bumper_left = sensors.light_bumper_left
    light_bumper_center_left = sensors.light_bumper_center_left
    light_bumper_center_right = sensors.light_bumper_center_right
    light_bumper_front_left = sensors.light_bumper_front_left
    light_bumper_front_right = sensors.light_bumper_front_right

    
    print(f"light_bumper_front_left: {light_bumper_front_left}, light_bumper_front_right: {light_bumper_front_right}, light_bumper_left: {light_bumper_left}, light_bumper_right: {light_bumper_right}")
    
    if light_bumper_left > 30 and light_bumper_right > 30 and light_bumper_front_left > 30 and light_bumper_front_right > 30:
        bot.drive_stop()
        stop = True
    if light_bumper_center_right >= 50:
        bot.drive_direct(100, -100)
    elif light_bumper_front_right >= 50:
        bot.drive_direct(100, -100)
    elif light_bumper_right >= 25:
        bot.drive_direct(100, 75)
    elif light_bumper_right <= 10:
        bot.drive_direct(100, 100)
        sleep(.1)
        bot.drive_direct(0, 100)
    elif light_bumper_left >= 15:
        bot.drive_direct(0, 100)
    elif light_bumper_center_left >= 25:
        bot.drive_direct(0, 100)
    else:
        bot.drive_direct(75, 75)
        
    
    return stop



if __name__ == "__main__":
    port = '/dev/ttyUSB0'

    bot = Create2(port=port)
    
    bot.start()
    
    bot.safe()
    
    stop = False
    
    # while irobot has not reached stop condition, keep going to run() function
    while not stop:
        
        stop = run(bot, stop)
        # print(f"light bumper: {light_bumper}, light_bumper_center_left: {light_bumper_center_left}, light_bumper_center_right: {light_bumper_center_right}, light_bumper_front_left: {light_bumper_front_left}, light_bumper_front_right: {light_bumper_front_right}, light_bumper_left: {light_bumper_left}, light_bumper_right: {light_bumper_right}, distance: {distance}, angle: {angle}")
        
    bot.drive_stop()
        