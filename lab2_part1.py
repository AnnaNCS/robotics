from pycreate2 import Create2
import time


"""
This function keeps track of angle change and distance since the beginning of the run.

It moves the robot forward unless it nears a wall, then it changes direction to keep light bumper sensors
within a range.

Once the robot has done a full circle, it stops.
"""
def run(bot, currAngle, currDistance):
    
    sensors = bot.get_sensors()
    
    light_bumper = sensors.light_bumper
    light_bumper_right = sensors.light_bumper_right
    light_bumper_left = sensors.light_bumper_left
    light_bumper_center_left = sensors.light_bumper_center_left
    light_bumper_center_right = sensors.light_bumper_center_right
    light_bumper_front_left = sensors.light_bumper_front_left
    light_bumper_front_right = sensors.light_bumper_front_right
    
    distance = sensors.distance
    angle = sensors.angle
    
    currAngle += angle
    currDistance += distance
    
    print(f"angle: {angle},  currAngle: {currAngle}")

    print(light_bumper_front_left)
    if light_bumper_front_left >= 75:
        bot.drive_direct(-100, 100)
    elif light_bumper_front_right >= 75:
        bot.drive_direct(100, -100)
    elif light_bumper_center_left >= 75:
        bot.drive_direct(-100, 100)
    elif light_bumper_center_right >= 75:
        bot.drive_direct(100, -100)
    elif light_bumper_left >= 25:
        bot.drive_direct(0, 100)
    elif light_bumper_right >= 25:
        bot.drive_direct(100, 0)
    else:
        bot.drive_direct(50, 50)
    
    return currAngle, currDistance



if __name__ == "__main__":
    port = '/dev/ttyUSB3'

    bot = Create2(port=port)
    
    bot.start()
    
    bot.safe()
    
    
    currAngle = 0
    currDistance = 0
    
    
    # while irobot has not reached stop condition, keep going to run() function
    while currAngle < 375 and currAngle > -375:
        
        currAngle, currDistance = run(bot, currAngle, currDistance)
        # print(f"light bumper: {light_bumper}, light_bumper_center_left: {light_bumper_center_left}, light_bumper_center_right: {light_bumper_center_right}, light_bumper_front_left: {light_bumper_front_left}, light_bumper_front_right: {light_bumper_front_right}, light_bumper_left: {light_bumper_left}, light_bumper_right: {light_bumper_right}, distance: {distance}, angle: {angle}")
        
    bot.drive_stop()
        