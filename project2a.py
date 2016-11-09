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


class bot():
    def __init__(self):
        self.x = []
        self.y = []
        self.theta = []


def main( ):
    # Initialize variables
    deltaT = 0.5
    robotVel = []
    lmbda = 8.5  # used for lambda variable
    velMax = 50  # Max speed for the robot
    noiseMean = 0.5
    noiseSTD = 0.1
    length = 100
    robot = bot()
    target = bot()
    relativeBot = bot()
    potentialBot = bot()

    #  target initialization
    #  set target initial position
    target.x.append( 0.0 )
    target.y.append( 0.0 )

    #  set initial heading of the target
    target.theta.append( 0.0 )

    #  set velocity of the target
    targetVel = 1.2

    ########################################
    #  robot Initialization

    #  initial position of the robot
    robot.x.append( 0.0 )
    robot.y.append( 0.0 )

    #  initial heading of the robot
    robot.theta.append( 0.0 )

    #  initial velocity of the robot
    robotVel.append( 0.1 )

    ########################################
    #  determine the difference between the robot and the target
    relativeX = ( target.x[ 0 ] - robot.x[ 0 ])
    relativeY = ( target.y[ 0 ] - robot.y[ 0 ])

    #  save the relative position of the robot and the target
    relativeBot.x.append( relativeX )
    relativeBot.y.append( relativeY )

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

    for index in range( 0 , length ):
        # set the trajectory for the target

        #####################################

        #  without noise
        qt_x = 60 - 15 * ( math.cos( deltaT ) )
        qt_y = 30 + 15 * ( math.sin( deltaT ) )
        plt.scatter( qt_x, qt_y, s = 2, color = "red")

        #  assign the position of the target
        target.x.append( qt_x )
        target.y.append( qt_y )
        plt.scatter( target.x[ index - 1 ], target.y[ index - 1 ], s = 2, color = "black")

        thetaXtemp = target.x[ index ] - target.x[ index - 1 ]
        thetaYtemp = target.y[ index ] - target.y[ index - 1 ]

        target.theta.append( math.atan2( thetaYtemp, thetaXtemp ) )

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
        #  get relative position of robot and target
        relativeX = target.x[ index - 1 ] - robot.x[ index - 1 ]
        relativeY = target.y[ index - 1 ] - robot.y[ index - 1 ]

        relativeBot.x.append( relativeX )
        relativeBot.y.append( relativeY )

        #  get phi variable
        phi = math.atan2( relativeBot.y[ index ], relativeBot.x[ index ] )

        #  get the magnitude of the robot and target relative position
        magRobTarg = math.sqrt( math.pow( relativeBot.x[ index ], 2 ) + math.pow( relativeBot.y[ index ], 2 ) )

        magTarg = math.sqrt( math.pow( targetVel, 2 ) )
        anglePhi = abs( math.cos( target.theta[ index ] - phi ))
        subVariableOne = math.pow( magTarg, 2 )
        subVariableTwo = 2 * lmbda * magRobTarg * magTarg * anglePhi
        subVariableThree = math.pow( lmbda, 2 ) + math.pow( magRobTarg, 2 )
        intVelDifRobot = math.sqrt( subVariableOne + subVariableTwo + subVariableThree )
        robotVel.append( min( intVelDifRobot, velMax ) )

        #  determine robot theta
        subVariableOne = magTarg * math.sin( target.theta[ index ] - phi )
        subVariableTwo = math.sqrt( math.pow( robotVel[ index - 1 ], 2 ) )
        omega = phi + math.asin( subVariableOne / subVariableTwo )

        #  robot dynamic controller
        robot.x.append( robotVel[ index ] * math.cos( robot.theta[ index - 1 ] ))
        robot.y.append( robotVel[ index ] * math.sin( robot.theta[ index - 1 ] ))
        robot.theta.append( omega )

        #  increment deltaT by 0.05
        deltaT += 0.05

    plt.show()

    #####################################

    #  display the robot and target location tracking
    for index in range( 0 , length ):
        plt.scatter( robot.x[ index ] , robot.y[ index ] , s = 2 , color = "blue" )
        plt.scatter( target.x[ index ] , target.y[ index ] , s = 2 , color = "red" )

    plt.show()
'''
    #  display the velocity and iteration scatter plot
    for index in range( -1 , length ):
        plt.scatter( index, robotVel[ index ], s = 2, color = "blue" )
        plt.scatter( index, targetVel, s = 2, color = "red" )

    plt.show()

    #  display theta for robot and target
    for index in range( -1 , length + 1):
        plt.scatter( index, robot.theta[ index ], s = 2, color = "blue" )
        plt.scatter( index, target.theta[ index ], s = 2, color = "red" )

    plt.show()
'''
main()
