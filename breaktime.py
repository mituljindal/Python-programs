import time
import webbrowser

total_breaks = 3
break_count = 0

print("This program started on "+time.ctime())
#looping the breaks
while(break_count < total_breaks):
    time.sleep(2*60*60) #wait 2 hours
    webbrowser.open("https://www.youtube.com/watch?v=cwzNbCjYX1E") #open youtube link in webbrowser
    break_count = break_count + 1
