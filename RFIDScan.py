#!/usr/bin/python
import time

timeWorked = 0
clockedIn = True
# Dictionary assigning every employee to a card number
employeeNames = {3194967166 : "Emmanuel",1128644206 : "Sayeh",3201638574 : "Samantha",3194936622 : "Terri",3193054270 : "Marina",1132207246 : "Chue",1132849950 : "Timothy",52632090 : "Khandaker",1073433162 : "Michael",3186384958 : "Edin",3186356286 : "Derrick",3185943598 : "Eduardo",3185992142 : "Gordon",3186706382 : "Bryan",3185911774 : "Myron",3187063006 : "Jonathon",3186258206 : "Samsodin",3186236478 : "Oudom",3186648926 : "Candice",1225119082 : "Kevin",1232589594 : "Sara",1225917706 : "Asaf",1225048442 : "Wendy",1225976746 : "Paul",1225314026 : "Miguel",1225347642 : "Walfri",1230014186 : "Ernesto",1225445258 : "Charles",1225124458 : "Monique",2103732382 : "Randy",3331579884 : "Raul",2102780110 : "David",2103861214 : "Alessandro",2102692382 : "Thelma",2103924478 : "Mark",2103838382 : "Cao",2103224910 : "William",2103835326 : "Ben"}

# Starts time and returns the time that the system has at the beginning
def beginTime():
  startTime = time.time()
  return startTime

# Stops timer and returns the total elapsed time. 
def finishTime(beginTime):
  endTime = time.time()
  elapsedTime = endTime - beginTime
  return elapsedTime

# Takes the total elapsed time and name of worker, and returns how long they worked in a hour:min:sec format.
def getTimeWorked(elapsedTime, worker):
  mins = elapsedTime // 60
  sec = elapsedTime % 60
  hours = mins // 60
  mins = mins % 60
  return ( "\nWorker: " + worker + "\nTime Lapsed = {0}:{1}:{2}\n".format(int(hours),int(mins),sec))

  # Determines if someone different clocked in when someone else is clocked in and returns the name of the employee who didnt clock out and the time since they clocked in.
def differentEmployee(elapsedTime, worker1, worker2):
  mins = elapsedTime // 60
  sec = elapsedTime % 60
  hours = mins // 60
  mins = mins % 60
  return "\n" + worker1 + " forgot to clock out and " + worker2 + " clocked in after {0}:{1}:{2}\n".format(int(hours),int(mins),sec) 

