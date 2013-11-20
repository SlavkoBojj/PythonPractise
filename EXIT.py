import os
import time

question = "Enter the exact name of the task you wish to end: "
taskID = raw_input(question)

print taskID + " shutting down in 10 seconds."
time.sleep(10)
os.system("TASKKILL /F /IM " + taskID + ".exe")
exit(2)
