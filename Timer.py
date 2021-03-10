#!/usr/bin/python
import time as time

# starts timer and returns the system time at which the timer started
def beginTime():
  return(time.time())

#takes the time started as a parameter and returns the amount of time elapsed since the timer started
def finishTime(startTime):
  endTime = time.time()
  elapsedTime = endTime - startTime
  return(elapsedTime)

#takes elapsed time as a parameter and returns it in an hours:mins:secs format
def formatTime(elapsedTime):
  mins = elapsedTime // 60
  sec = elapsedTime % 60
  hours = mins // 60
  mins = mins % 60
  return("\nTime Lapsed = {0}:{1}:{2}\n".format(int(hours),int(mins),sec))

#takes elapsed time and name of worker as parameters and returns it in an hours:mins:secs format with the name of the worker
def formatTimeWithWorker(elapsedTime, worker):
  mins = elapsedTime // 60
  sec = elapsedTime % 60
  hours = mins // 60
  mins = mins % 60
  return("\nWorker: " + worker + "\nTime Lapsed = {0}:{1}:{2}\n".format(int(hours),int(mins),sec))
