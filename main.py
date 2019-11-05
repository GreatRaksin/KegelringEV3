#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

# Write your program here
LM = Motor(Port.B)
RM = Motor(Port.D)
WD = 56
AT = 114

Robot = DriveBase(LM, RM, WD, AT)

Eyes = UltrasonicSensor(Port.S3)
Col = ColorSensor(Port.S2)

while True:
    Robot.drive(0, 90)

    if Eyes.distance() < 350:
        wait(10)
        while Col.reflection() > 10:
            Robot.drive(200, 0)

        else:
            Robot.drive_time(-250, 0, 1500)