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

from tkinter import ttk
from ttkthemes import ThemedTk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

root = ThemedTk(theme='yaru' )

# Get the available themes
print(root.get_themes())

#display the mem used
w = ttk.Label(root, text=f"total Mem used percent {mem_percent}%")
w.pack()

# Creating a themed button
button = ttk.Button(root, text="Quit", command=root.destroy)
button.pack(pady=20)

#show a graph
fig = Figure(figsize=(5, 4), dpi=100)
ax = fig.add_subplot(111) # Add a subplot to the figure
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
ax.plot(x, y)
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_title("My Graph")
canvas = FigureCanvasTkAgg(fig, master=root)
canvas_widget = canvas.get_tk_widget()
canvas_widget.pack(pady=10)  

root.mainloop()



