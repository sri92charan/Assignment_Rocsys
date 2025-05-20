import random
import time
import os
import datetime
# to dock the robot enter the current robot state as function argument
# the function returns a tuple of three
# first value: whether the dock was success (True of False)
# second value: the new state the robot is in after docking
# third value: A string textual explanation of the result
# the call simulate_robot_dock caters for various random results
def simulate_robot_dock(state):
    if state == "Docked":
        return (False, "Docked", "Cannot dock from a docked state")
    else:
        rand = random.random()
        time.sleep(rand * 0.5)
        if rand <= 0.8:
            return (True,"Docked", "Success")
        if rand > 0.8 and rand <= 0.9:
            return (False, state, "Failed to find socket")
        if rand >0.9 and rand <=0.95:
            return (False, state, "Failed to insert")
        if rand > 0.5:
            return (False, state, "General Mechanical Error")
    return (False, state, "Programming error")
# to undock the robot enter the current robot state as function argument
# the function returns a tuple of three
# first value: whether the undock was success (True of False)
# second value: the new state the robot is in after undocking
# third value: A string textual explanation of the result
def simulate_robot_undock(state):
    if state != "Docked":
        return (False, state, "Undock not possible in current state " +state)
    else:
        time.sleep(0.5)
        return (True,"Undocked", "Success")
# to bring the robot in a start state the function simulate_robot_prepare()
#is called with no arguments
# the function returns a stable state as result
def simulate_robot_prepare():
    return "Undocked"
#one robot cycle example (prepare -> dock -> undock)

#part of the code to prepare the logFile
dateToday=datetime.datetime.now().date()
dirPath = os.path.dirname(os.path.realpath(__file__))
endTestLogFileName="endTestLogFIle_"+str(dateToday)+".txt"
endTestLogfile=open(dirPath+"\\"+endTestLogFileName,"a")

for cycleIndex in range(100):
    print("Current cycle=",str(cycleIndex+1))
    startCycleString="Endurance test cycle {}:\r\n".format(str(cycleIndex+1))
    endTestLogfile.write(startCycleString)
    lenSpaces=len(startCycleString)-1
    timeNow=datetime.datetime.now().strftime('%H:%M:%S')
    state = simulate_robot_prepare()
    endTestLogfile.write(lenSpaces*" "+"Prepare step started at {}".format(str(timeNow))+"\r\n")
    (result, new_state, explanation_txt) = simulate_robot_dock(state)
    timeNow=datetime.datetime.now().strftime('%H:%M:%S')
    endTestLogfile.write(lenSpaces*" "+"Docking result received at {}".format(str(timeNow))+" and the result is {}\r\n".format(str(result)))
    state = new_state
    print ("Dockresult = ", result, explanation_txt)
    (result, new_state, explanation_txt) = simulate_robot_undock(state)
    timeNow=datetime.datetime.now().strftime('%H:%M:%S')
    endTestLogfile.write(lenSpaces*" "+"Undocking result received at {}".format(str(timeNow))+" and the result is {}\r\n".format(str(result)))
    state = new_state
    print ("Undockresult = ", result, explanation_txt)
    time.sleep(2)

endTestLogfile.close() # Closing the logFile at the end