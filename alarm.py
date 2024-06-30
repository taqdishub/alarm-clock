import datetime
import time
import pygame
from threading import *
from tkinter import *

# Initialize Pygame
pygame.mixer.init()

# Create Object
root = Tk()

# Set geometry
root.geometry("400x250")

# Use Threading
def Threading():
    t1 = Thread(target=alarm)
    t1.start()

def alarm():
    while True:
        set_alarm_time = f"{hour.get()}:{minute.get()}:{second.get()} {ampm.get()}"
        current_time = datetime.datetime.now().strftime("%I:%M:%S %p")
        
        if current_time == set_alarm_time:
            print("Time to Wake up")
            pygame.mixer.music.load("Tere Pyar Mein_320(PagalWorld.com.se).wav.mp3")
            pygame.mixer.music.play(loops=0)
            break
        time.sleep(1)

# Add Labels, Frame, Button, Optionmenus
Label(root, text="Alarm Clock", font=("Helvetica 20 bold"), fg="red").pack(pady=10)
Label(root, text="Set Time", font=("Helvetica 15 bold")).pack()

frame = Frame(root)
frame.pack()

# Hours in AM/PM format
hour = StringVar(root)
hours = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
hour.set(hours[0])

hrs = OptionMenu(frame, hour, *hours)
hrs.pack(side=LEFT)

# Minutes and Seconds (unchanged)
minute = StringVar(root)
minutes = ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10',
           '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21',
           '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32',
           '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43',
           '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54',
           '55', '56', '57', '58', '59', '60']
minute.set(minutes[0])

mins = OptionMenu(frame, minute, *minutes)
mins.pack(side=LEFT)

second = StringVar(root)
seconds = ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10',
           '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21',
           '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32',
           '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43',
           '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54',
           '55', '56', '57', '58', '59', '60']
second.set(seconds[0])

secs = OptionMenu(frame, second, *seconds)
secs.pack(side=LEFT)

# AM/PM selection
ampm = StringVar(root)
ampm.set("AM")  # Default selection

ampm_choices = ['AM', 'PM']
ampm_option = OptionMenu(frame, ampm, *ampm_choices)
ampm_option.pack(side=LEFT)

Button(root, text="Set Alarm", font=("Helvetica 15"), command=Threading).pack(pady=20)

# Execute Tkinter
root.mainloop()
