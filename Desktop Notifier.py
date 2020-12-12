from tkinter import Tk, Label, Canvas                                                   # Tkinter module used To display a GUI
import psutil                                                                           # Psutil module used To get system properties                                              
from plyer import notification                                                          # Plyer module used To enable to send notifications to the system
from datetime import date, time, datetime                                               # Datetime module used To get time, date, day, etc. in various formats
import time                                                                             # Time module used To get the elapsed time during the execution of code
                            
def push_notif():                                                                       # Defined a function to show notification with baterry, date and time

    bat_percent = psutil.sensors_battery().percent                                      # Variable used to store battery percentage
    current_DATETIME = datetime.now()                                                   # Variable used to store date and time
                                                                                    
    # Following format strings are used with the fucntion strftime() to 
    # "%A" returns the current Day
    # "%d %b %Y" returns date with month in letters and year,
    # "%X" returns time
    time_and_date = current_DATETIME.strftime("%A, %d %b, %Y\n%X ")                  

    notification.notify(                                                                # Built in plyer function to display notification
        title = "Battery, Date and Time",
        message = str(bat_percent) + "% Battery remaining \n" + time_and_date,
        timeout = 10
    )
# ******** push_notif() FUNCTION DEFINITION ENDS ********              
push_notif()                                                                            # Calling the push_notif function to show a notification along with the GUI window




# ----------------------- The following code segment is to show a GUI window created using Tkinter module :-----------------------------------------------------

tkobject = Tk()
tkobject.title("Battery, Date and Time Notifier")                                                                                       
C = Canvas(tkobject, bg = "#2f3848", height=900, width=1500)                           # To build a canvas window of 1500*1000 pixels 
current_DATETIME = datetime.now()

def clockGUI():                                                                         # Defined a function To diplay a clock in GUI using lable function
    hr = str(current_DATETIME.strftime("%I"))
    label_hr.config(text=hr)

    m = str(current_DATETIME.strftime("%m"))
    label_min.config(text=m)

    s = str(current_DATETIME.strftime("%S"))
    label_sec.config(text=s)

    p = str(current_DATETIME.strftime("%p"))
    label_day.config(text=p)

    d = str(current_DATETIME.strftime("%d"))
    label_d.config(text=d)

    
    label_x.config(text=m)

    y = str(current_DATETIME.strftime("%Y"))
    label_y.config(text=y)

# Label function is used to display text
# The following Label functions are used to display all the raw text such as,"Minutes", "YEAR",etc.

label_info = Label(tkobject, text = "Close this window to see notification after every 10 seconds! (alterable)", font = ("Poppins", 22, "bold italic"), bg="#2f3848", fg="#ea5469")
label_info.place(x=180, y=5, width=1100, height=110)

label_tag = Label(tkobject, text="Welcome! Here is the Digital Clock and Calander!", font=("Poppins", 30, "bold "), bg="#2f3848", fg="#ea5469")
label_tag.place(x=220, y=90, width=1050, height=110)

label_hr = Label(tkobject, text="", font=("Poppins", 50, ""), bg="#04c0b8", fg="white")
label_hr.place(x=400, y=300, width=150, height=150)

label_h2 = Label(tkobject, text="Hours", font=("Poppins", 20, ""), bg="#04c0b8", fg="white")
label_h2.place(x=400, y=460, width=150, height=45)

label_min = Label(tkobject, text="", font=("Poppins", 50, ""), bg="#04c0b8", fg="white")
label_min.place(x=570, y=300, width=150, height=150)

label_min2 = Label(tkobject, text="Minutes", font=("Poppins", 20, ""), bg="#04c0b8", fg="white")
label_min2.place(x=570, y=460, width=150, height=45)

label_sec = Label(tkobject, text="", font=("Poppins", 50, ""), bg="#04c0b8", fg="white")
label_sec.place(x=740, y=300, width=150, height=150)

label_sec2 = Label(tkobject, text="Seconds", font=("Poppins", 20, ""), bg="#04c0b8", fg="white")
label_sec2.place(x=740, y=460, width=150, height=45)

label_day = Label(tkobject, text="", font=("Poppins", 50, ""), bg="#04c0b8", fg="white")
label_day.place(x=910, y=310, width=150, height=200)

label_d = Label(tkobject, text="", font=("Poppins", 20, ""), bg="#04c0b8", fg="white")
label_d.place(x=480, y=600, width=150, height=45)

label_d2 = Label(tkobject, text="Date", font=("Poppins", 20, ""), bg="#04c0b8", fg="white")
label_d2.place(x=480, y=660, width=150, height=45)

label_x = Label(tkobject, text="", font=("Poppins", 20, ""), bg="#04c0b8", fg="white")
label_x.place(x=670, y=600, width=150, height=45)

label_x2 = Label(tkobject, text="Month", font=("Poppins", 20, ""), bg="#04c0b8", fg="white")
label_x2.place(x=670, y=660, width=150, height=45)

label_y = Label(tkobject, text="", font=("Poppins", 20, ""), bg="#04c0b8", fg="white")
label_y.place(x=840, y=600, width=150, height=45)

label_y2 = Label(tkobject, text="Year", font=("Poppins", 20, ""), bg="#04c0b8", fg="white")
label_y2.place(x=840, y=660, width=150, height=45)

clockGUI()                                                                              # Calling the clockGUI function to display time
C.pack()    
tkobject.mainloop()                                                                     # To keep the GUI window on screen(keeps it on loop)
                                                                                        # otherwise the window opens and instantly disappears

#******************************************************** CODE FOR GUI WINDOW ENDS HERE ********************************************************





# ----------------------- Following is the code to push notifications repeatedly after a specified period of time :-----------------------------------------------------


specified_time = 10                                                                    # The specified period of time in seconds 
count = 1                                                                              # A counter variable - to count the no. of pushed notifications  


while 1:                                                                               # An Infinite loop is running here
    time_at_start = time.time()
    while 1:
        time_now = time.time()
        time_elapsed = time_now - time_at_start

        if time_elapsed > specified_time:                                              # Checking if the elapsed time is greater than the specified 
            count = count + 1
            print("Notification pushed " , count , "times!" )                          # An Output statement to show the number of time the notification is pushed
            push_notif()                                                               # Calling the show_notif function
            break

