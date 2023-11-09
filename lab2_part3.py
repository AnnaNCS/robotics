from asyncio import sleep
from pycreate2 import Create2
import time

"""
This function keeps the robot moving forward and following the right wall of the maze.

The robot stops once the front and left light bump sensors don't detect a wall (buggy).
"""
def run(bot, stop, time1):
    
    sensors = bot.get_sensors()
    
    light_bumper = sensors.light_bumper
    light_bumper_right = sensors.light_bumper_right
    light_bumper_left = sensors.light_bumper_left
    light_bumper_center_left = sensors.light_bumper_center_left
    light_bumper_center_right = sensors.light_bumper_center_right
    light_bumper_front_left = sensors.light_bumper_front_left
    light_bumper_front_right = sensors.light_bumper_front_right

    
    print(f"light_bumper_front_left: {light_bumper_front_left}, light_bumper_center_left: {light_bumper_center_left}, light_bumper_left: {light_bumper_left}, light_bumper_right: {light_bumper_right}")
    print(f"{time1%25}")
    if light_bumper_center_right >= 50:
        bot.drive_direct(100, -100)
    elif light_bumper_front_right >= 50:
        bot.drive_direct(100, -100)
    elif light_bumper_right >= 25:
        bot.drive_direct(100, 0)
    elif light_bumper_right <= 10:
        bot.drive_direct(100, 100)
        # sleep(.5)
        bot.drive_direct(0, 100)
    elif light_bumper_left >= 15:
        bot.drive_direct(0, 100)
    elif light_bumper_center_left >= 25:
        bot.drive_direct(0, 100)
    elif light_bumper_left < 1 and light_bumper_front_left < 1 and light_bumper_center_left < 1: #and light_bumper_right > 30:
        stop = True
    else:
        bot.drive_direct(75, 75)
        
    time1 += 1
    
    return stop, time1



if __name__ == "__main__":
    port = '/dev/ttyUSB0'

    bot = Create2(port=port)
    
    bot.start()
    
    bot.safe()
    
    stop = False
    time1 = 0
    
    # while irobot has not reached stop condition, keep going to run() function
    while not stop:
        
        stop, time1 = run(bot, stop, time1)
        # print(f"light bumper: {light_bumper}, light_bumper_center_left: {light_bumper_center_left}, light_bumper_center_right: {light_bumper_center_right}, light_bumper_front_left: {light_bumper_front_left}, light_bumper_front_right: {light_bumper_front_right}, light_bumper_left: {light_bumper_left}, light_bumper_right: {light_bumper_right}, distance: {distance}, angle: {angle}")
        
    bot.drive_stop()
        