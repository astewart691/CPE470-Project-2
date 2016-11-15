"""
File Name: Project2b.py
Author: Aarron Stewart
Class: CPE470
Term: Fall 2016
"""

# import libraries
import math
import numpy as np
import matplotlib.pyplot as plt


class bot():
    def __init__(self):
        self.x = []
        self.y = []
        self.theta = []


def main( ):
    # Initialize variables
    deltaT = 0.05
    robotVel = []
    lmbda = 0.25  # used for lambda variable
    velMax = 50  # Max speed for the robot
    noiseMean = 0.5
    noiseSTD = 0.1
    length = 100
    robot = bot()
    target = bot()
    relativeBot = bot()
    error = [ 0.0 ]

    #  target initialization
    #  set target initial position
    target.x.append( 10 )
    target.y.append( 10 + 5 * math.sin( deltaT ))

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
    relativeBot.x.append( relativeX )
    relativeBot.y.append( relativeY )

    ########################################

    for index in range( 1 , length ):
        # set the trajectory for the target

        #####################################

        #  without noise
        qt_x = target.x[ index - 1 ] + 0.25
        qt_y = 10 + 5 * math.sin( deltaT )

        #  with noise
        '''
        qt_x =  target.x[ index - 1 ] + 0.25 + noiseSTD * np.random.randn() + noiseMean
        qt_y =  10 + 5 * math.sin( deltaT ) + noiseSTD * np.random.randn() + noiseMean
        '''
        #  assign the position of the target
        target.x.append( qt_x )
        target.y.append( qt_y )

        thetaXtemp = target.x[ index ] - target.x[ index - 1 ]
        thetaYtemp = target.y[ index ] - target.y[ index - 1 ]

        target.theta.append( math.atan2( thetaYtemp , thetaXtemp ) )

        #####################################

        #  enter the code here

        #  get phi variable
        phi = math.atan2( relativeBot.y[ index - 1 ] , relativeBot.x[ index - 1 ] )

        tempArray = np.array( [ targetVel ] )

        magTarg = np.linalg.norm( tempArray )

        tempArray = np.array( [ relativeBot.x[ index - 1 ] , relativeBot.y[ index - 1 ] ] )

        #  get the magnitude of the robot and target relative position
        magRobTarg = np.linalg.norm( tempArray )

        anglePhi = math.cos( target.theta[ index ] - phi )
        subVariableOne = math.pow( magTarg , 2 )
        subVariableTwo = 2 * lmbda * magRobTarg * magTarg * anglePhi
        subVariableThree = (math.pow( lmbda , 2 )) * (math.pow( magRobTarg , 2 ))
        intVelDifRobot = math.sqrt( subVariableOne + subVariableTwo + subVariableThree )
        robotVel.append( min( intVelDifRobot , velMax ) )

        #  determine robot theta
        innerVariable = target.theta[ index ] - phi
        variableOne = magTarg * math.sin( innerVariable )
        tempArray = np.array( [ robotVel[ index ] ] )
        robVelMag = np.linalg.norm( tempArray )
        robot.theta.append( phi + math.asin( (variableOne / abs( robVelMag )) ) )

        #  robot dynamic controller
        robot.x.append( robot.x[ index - 1 ] + (deltaT * robotVel[ index ]) * math.cos( robot.theta[ index ] ) )
        robot.y.append( robot.y[ index - 1 ] + (deltaT * robotVel[ index ]) * math.sin( robot.theta[ index ] ) )

        #  get relative position of robot and target
        relativeX = target.x[ index ] - robot.x[ index ]
        relativeY = target.y[ index ] - robot.y[ index ]

        relativeBot.x.append( relativeX )
        relativeBot.y.append( relativeY )

        tempArray = np.array( [ relativeX , relativeY ] )
        error.append( np.linalg.norm( tempArray ) )
        #  increment deltaT by 0.05
        deltaT += 0.05

        #####################################

        #  display the robot and target location tracking
    for index in range( 0 , length ):
        plt.scatter( robot.x[ index ] , robot.y[ index ] , s = 2 , color = "black" )
        plt.scatter( target.x[ index ] , target.y[ index ] , s = 2 , color = "red" )

    plt.show( )

    #  display relative location
    for index in range( 0 , length ):
        plt.scatter( index , error[ index ] , s = 2 , color = "black" )

    plt.show( )

    #  display theta for robot and target
    for index in range( 0 , length ):
        plt.scatter( index , robot.theta[ index ] , s = 2 , color = "black" )
        plt.scatter( index , target.theta[ index ] , s = 2 , color = "red" )

    plt.show( )


main( )