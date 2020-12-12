# Desktop-Notifer-Application
A windows based application on python, which displays a clock GUI and pushes a notification showing remaining Battery, date, time and day; repeatedly after a specified amount of time. (10 seconds default). 


Python Libraries used in the project:
Tkinter	-	To display a GUI Window
Psutil		-	To get system properties, e.g Battery Percentage
Plyer		-	To enable to push notifications 
Datetime	-	To get time, date, day, etc. 
Time		-	To get the elapsed time during the execution of code


A Function is defined to push notification with all the info, in which 
psutil and plyer modules are interlinked and work together to show a notification.


A Segment of code is written using Tkinter to display a Clock and Calendar GUI.  (Additional Feature). 
Tkinter and Datetime modules are interlinked and work together to show the GUI window.

An infinite while loop is used to keep printing notifications after a certain period of time, until the program stops. 
Here the function created to push notifications is called.
