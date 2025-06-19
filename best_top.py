import subprocess, sys, re
from io import StringIO
from decimal import *
#=====================================================
# HELPER FUNC
#=====================================================

LINE_PID       = 0
LINE_USER      = 1
LINE_PR        = 2
LINE_NI        = 3
LINE_VIRT      = 4
LINE_RES       = 5
LINE_SHR       = 6
LINE_S         = 7
LINE_CPU       = 8
LINE_MEM       = 9
LINE_TIME      = 10
LINE_COMMAND   = 11


# returns array/tuple in formatt [PID , USER, PR , NI , VIRT , RES , SHR , S , CPU , MEM , TIME , COMMAND]
def proccess_line(line):
    line = line.split()
    print(len(line) , line)
    return line

#=================================DATA_REQUEST_SECTION===================================
output = []
frame = []

# Open the file and read line by line
with open('file.txt', 'r') as file:
    for line in file:
        output.append(line.strip())  # .strip() removes trailing newline characters


# get the CPU stats
for x in range(7 , len(output)):
    line = output[x]
    frame.append(proccess_line(line))
print(frame[0][LINE_CPU] , frame[0][LINE_COMMAND])
total_cpu = Decimal(0)
for proc in frame:
    total_cpu += Decimal(proc[LINE_CPU])
print("Total CPU usage : " , total_cpu )

#get the MEM stats
# 3, 4
mem_stats = output[3].split()
mem_swap_stats = output[4].split()
print(mem_stats )
mem_percent = Decimal(mem_stats[7]) / Decimal(mem_stats[3])  * 100 
mem_percent = mem_percent.quantize(Decimal('00.0'), rounding=ROUND_HALF_UP)
print( mem_swap_stats )
print(f"total Mem used percent {mem_percent}%")

#========================GUI_SECTION==================================

from tkinter import *

root = Tk()
w = Label(root, text=f"total Mem used percent {mem_percent}%")
w.pack()
root.mainloop()
    


