"""
File Name: Project2a.py
Author: Aarron Stewart
Class: CPE470
Term: Fall 2016
"""

# import libraries
import math
#  import numpy as np
import matplotlib.pyplot as plt


class bot:
    x = []
    y = []
    theta = []


def main( ):
    # Initialize variables
    deltaT = 0.5
    targetVel = 0
    robotVel = []
    lmbda = 8.5  # used for lambda variable
    robotMax = 50  # Max speed for the robot
    noiseMean = 0.5
    noiseSTD = 0.1
    length = 100

    robot = bot()
    target = bot()
    relativeBot = bot()
    potentialBot = bot()

    #  target initialization
    #  set target initial position
    target.x.append( 0 )
    target.y.append( 0 )

    #  set initial heading of the target
    target.theta.append( 0 )

    #  set velocity of the target
    targetVel = 1.2

    ########################################
    #  robot Initialization

    #  initial position of the robot
    robot.x.append( 0 )
    robot.y.append( 0 )

    #  initial heading of the robot
    robot.theta.append( 0 )

    #  initial velocity of the robot
    robotVel.append( 0 )

    ########################################
    #  determine the difference between the robot and the target
    relativeX = ( target.x[ 0 ] - robot.x[ 0 ])
    relativeY = ( target.y[ 0 ] - robot.y[ 0 ])

    #  save the relative position of the robot and the target
    relativeBot.x = relativeX
    relativeBot.y = relativeY

    #  save the relative velocity of the robot and the target
    targetAngle = math.cos( target.theta[ 0 ])
    robotAngle = math.cos( robot.theta[ 0 ])
    potentialX = targetVel * targetAngle - robotVel[ 0 ] * robotAngle

    targetAngle = math.sin( target.theta[ 0 ])
    robotAngle = math.sin( robot.theta[ 0 ])
    potentialY = targetVel * targetAngle - robotVel[ 0 ] * robotAngle

    potentialBot.x.append( potentialX )
    potentialBot.y.append( potentialY )

    ########################################

    for index in range( 0 , length + 1 ):
        # set the trajectory for the target

        #####################################

        #  without noise
        qt_x = 60 - 15 * ( math.cos( deltaT ) )
        qt_y = 30 + 15 * ( math.sin( deltaT ) )

        #  assign the position of the target
        target.x.append( qt_x )
        target.y.append( qt_y )

        #####################################
        #  with noise
        '''
        qt_x = 60 - 15cos( t(i) ) + noiseSTD * randn + noiseMean
        qt_y = 30 + 15sin( t(i) ) + noiseSTD * randn + noiseMean

        #  assign the position of the target
        qt( index, : ) = [ qt_x , qt_y ]
        '''

        #####################################

        #  enter the code here


        #  increment deltaT by 0.05
        deltaT += 0.05

    #####################################

    #  display the robot and target location tracking
    for index in range( 0 , length + 1 ):
        plt.scatter( robot.x[ index ] , robot.y[ index ] , s = 2 , color = "black" )
        plt.scatter( target.x[ index ] , target.y[ index ] , s = 2 , color = "red" )

    plt.show()
    '''
    #  display the velocity and iteration scatter plot
    for index in range( 1, length ):
        plt.scatter( index, robotVelocity, s = 2, color = "black" )
        plt.scatter( index, targetVelocity, s = 2, color = "red" )

    plt.show()
    '''

main( )
