# This was made by Jacob Graham at 12:21 pm on 01/23/2025  so that I don't have to open canvas myself everytime

# pyautogui is how I control the mouse
import pyautogui
# webbrowser is built in and it's how I open the website
import webbrowser
# time is also built in and I use it to make the program delay to allow the webpage to open before clicking
import time
# datetime is what allows me to get the current time so the bot can open the class for that time period
from datetime import datetime
import pyperclip
# So it can open notepad to take notes
import subprocess
# These two libraries are what allows the bot to close vs code when it's done
import os
import atexit
# These two libraries are what allows the bot to show the pop up box
import tkinter as tk
#from tkinter import messagebox

# Get the current time
current_time = datetime.now().time()

# Get the current day
current_day = datetime.now().strftime("%A")

ksu_website = "https://flashline.kent.edu"
github_website = "https://github.com/"
spanish_website = "https://eleteca.edinumen.es/login/index.php"


# Coordinates for sign in button
sign_In_Button_x = 880
sign_In_Button_y = 650

# Coordinates for Next button
next_Button_x = 1480
next_Button_y = 650

# Coordinates for sign in button #2
sign_In_Button_2_x = 1480
sign_In_Button_2_y = 710

# Coordinates for canvas button
canvas_button_x = 1865
canvas_button_y = 200

# Coordinates for the middle of the page
middle_x = 1280
middle_y = 720

# Coordinates for the Math classroom page
math_button_x = 300
math_button_y = 1020

# Coordinates for the Spanish classroom page
spanish_button_x = 900
spanish_button_y = 620

# Coordinates for the Spanish Textbook sign in button
spanish_sign_in_button_x = 1280
spanish_sign_in_button_y = 720

# Coordinates for the Spanish Textbook username ThisIsMyAmazingPasswordTurtleParrot12345678910@#!ton
spanish_username_button_x = 990
spanish_username_button_y = 890

# Coordinates for the Spanish Textbook enter button
spanish_enter_button_x = 1490
spanish_enter_button_y = 940

# Coordinates for the PSA classroom page
psa_button_x = 500
psa_button_y = 620

# Coordinates for the Ethics classroom page
ethics_button_x = 1500
ethics_button_y = 620

# Coordinates for the Programming classroom page
programming_button_x = 900
programming_button_y = 920

# Coordinates for the github repo page
github_repo_button_x = 300
github_repo_button_y = 615

#open website
webbrowser.open(ksu_website)
# wait for website to load
time.sleep(8)
# move the mouse over the sign in button
pyautogui.moveTo(sign_In_Button_x, sign_In_Button_y)
# and now click the sign in button
pyautogui.click()

# NEXT PAGE

# wait for website to load sign in page
time.sleep(5)
# move the mouse over the next button
pyautogui.moveTo(next_Button_x, next_Button_y)
# and now click the sign in button
pyautogui.click()

# NEXT PAGE

# wait for website to load password page
time.sleep(6)
# move the mouse over the sign in button
pyautogui.moveTo(sign_In_Button_2_x, sign_In_Button_2_y)
# and now click the sign in button
pyautogui.click()

# NEXT PAGE

# wait for website to load Home page
time.sleep(7) 
# move the mouse over the Canvas button
pyautogui.moveTo(canvas_button_x, canvas_button_y)
# and now click the canvas button
pyautogui.click()

#====If it is Math Class time====
# 30 minutes before to the start of class
Math_class_start_time = datetime.strptime("08:20", "%H:%M").time()  # 8:20 am
Math_class_end_time = datetime.strptime("10:30", "%H:%M").time()    # 10:30 am

# Check if the current time is within the range
if Math_class_start_time <= current_time <= Math_class_end_time:
    print("Math class")
    time.sleep(7)
    pyautogui.moveTo(math_button_x, math_button_y)
    pyautogui.click()
else:
    print("")


#====If it is Spanish Class time====
# 20 minutes before to the start of class
Spanish_class_start_time = datetime.strptime("10:40", "%H:%M").time()  # 10:40 am
Spanish_class_end_time = datetime.strptime("12:00", "%H:%M").time()    # 12:00 pm

# Check if the current time is within the range
if Spanish_class_start_time <= current_time <= Spanish_class_end_time:
    print("Spanish class")
    time.sleep(7)
    pyautogui.moveTo(spanish_button_x, spanish_button_y)
    pyautogui.click()
    #Click sign on button for spanish textbook site
    #open website
    time.sleep(4)
    webbrowser.open(spanish_website)
    time.sleep(7)
    pyautogui.moveTo(spanish_sign_in_button_x, spanish_sign_in_button_y)
    pyautogui.click()
    time.sleep(3)
    pyperclip.copy("Username")
    pyautogui.hotkey("ctrl", "v")
    time.sleep(3)
    pyautogui.moveTo(spanish_username_button_x, spanish_username_button_y)
    time.sleep(3)
    pyautogui.click()
    time.sleep(4)
    pyautogui.moveTo(spanish_username_button_x, 850)
    time.sleep(4)
    with open("FileThatHasPassword.txt", "r") as file:
        pyautogul = file.read()
        pyperclip.copy(pyautogul)
        pyautogui.click()
        time.sleep(2)
        pyautogui.hotkey("ctrl", "v")
        pyperclip.copy("")
        time.sleep(3)
        pyautogui.moveTo(spanish_enter_button_x, spanish_enter_button_y)
        time.sleep(2)
        pyautogui.click()
else:
    print("")

#====If it is PSA Class time====
psa_class_start_time = datetime.strptime("12:05", "%H:%M").time()  # 12:05 pm
psa_class_end_time = datetime.strptime("12:55", "%H:%M").time()    # 12:55 pm

class_days1 = {"Monday", "Wednesday"} 
# Check if the current time is within the range
if current_day in class_days1 and psa_class_start_time <= current_time <= psa_class_end_time:
    print("PSA class")
    time.sleep(7)
    pyautogui.moveTo(psa_button_x, psa_button_y)
    pyautogui.click()
else:
    print("")


#====If it is Ethics Class time====
#$$$$$$$$$NEED TO DEBUG TIMES AND ON DIFFERNT DAYS$$$$$$$$$$$$$
ethics_class_start_time = datetime.strptime("12:15", "%H:%M").time()  # 12:15 PM
ethics_class_end_time = datetime.strptime("13:45", "%H:%M").time()    # 1:45 PM

class_days2 = {"Tuesday", "Thursday"} 

# Check if the current time and day is within the range
if current_day in class_days2 and ethics_class_start_time <= current_time <= ethics_class_end_time:
    print("Ethics class on Tuesday or Thursday!")
    time.sleep(7)
    pyautogui.moveTo(ethics_button_x, ethics_button_y)
    pyautogui.click()
    time.sleep(3)
    # Open Notepad so I can take notes
    subprocess.run(['notepad.exe'])
else:
    print("")



#====If it is Structure of programming Class time====
program_class_start_time = datetime.strptime("15:25", "%H:%M").time()  # 3:25 PM #15:25
program_class_end_time = datetime.strptime("17:00", "%H:%M").time()    # 5:00 PM

# Check if the current time is within the range
if program_class_start_time <= current_time <= program_class_end_time:
    print("Structure of programming languages class")
    time.sleep(7)
    pyautogui.moveTo(programming_button_x, programming_button_y)
    pyautogui.click()
    # Open up github aswell
    time.sleep(5)
    webbrowser.open(github_website)
    # wait for website to load
    time.sleep(7)
    pyautogui.moveTo(github_repo_button_x, github_repo_button_y)
    pyautogui.click()
    time.sleep(3)
    webbrowser.open("https://github.com/gregdelozier/struct-prog-lang")
    time.sleep(3)
    # Open Notepad so I can take notes
    subprocess.run(['notepad.exe'])
else:
    print("")

# The bot says goodbye
def close_window():
    popup.destroy()  # Close the popup

root = tk.Tk()
root.withdraw()  # Hide the main window

# Create the pop-up window
popup = tk.Toplevel()
popup.title("Class Bot Timmy")
popup.configure(bg="green")  # Set background color to green

# Set the pop-up window to be always on top
popup.attributes('-topmost', True)

# Set the pop-up window to full screen
popup.attributes('-fullscreen', True)

# Create message label
label = tk.Label(popup, text="Everything is set up, have a great class Jacob!", bg="green", fg="white", padx=10, pady=10)
label.pack(expand=True)  # Use expand=True to center the label in full screen

# Create a frame to hold the button and text
button_frame = tk.Frame(popup, bg="green")
button_frame.pack(pady=20)  # Add some vertical padding

# Create a cookie button with an icon
cookie_color = "#D2B48C"  # Light brown/tan (cookie-like)
cookie_button = tk.Button(button_frame, text="🍪", command=close_window, bg=cookie_color, fg="black", font=("Arial", 24), width=3)
cookie_button.pack(side=tk.LEFT)  # Place the button on the left

# Create a label for the text next to the cookie button
text_label = tk.Label(button_frame, text="Give Timmy a cookie for his good work", bg="green", fg="black", font=("Arial", 16))
text_label.pack(side=tk.LEFT, padx=10)  # Add some horizontal padding

# Wait for the popup to close before continuing
popup.wait_window()
# The code after this will execute **after the pop-up is closed**
print("The program continues executing after closing the pop-up!")


# Closes VS code one everything is open for that class
time.sleep(2)
def close_vscode():
    os.system("taskkill /f /im code.exe")

atexit.register(close_vscode)