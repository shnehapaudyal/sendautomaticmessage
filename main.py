import pyautogui
import time
# import psutil
import wmi


# To check if any process is running in your windows application
def skypeping():
    # Initializing the wmi constructor
    f = wmi.WMI()
    flag = 0
    # Iterating through all the running processes
    for process in f.Win32_Process():
        # Checking processes
        if "chrome.exe" == process.Name:
            print("Application is Running")
            automatedtyping()
            flag = 1
            break

    if flag == 0:
        print("Application is not Running")


# Open a application where you want to send automatic message, and it types the message for you.
def automatedtyping():
    print("Automated typing starts here")
    for i in range(1):
        text = "This is an automated message"
        pyautogui.typewrite(text)
        time.sleep(2)
        pyautogui.press('enter')
    print("Automated typing ends here")


if __name__ == "__main__":
    skypeping()
