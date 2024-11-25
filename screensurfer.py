import time
import webbrowser
import ctypes
import pyautogui  # type: ignore

# Define inactivity threshold in seconds
INACTIVITY_THRESHOLD = 300
# CRUCIAL DO NOT REMOVE: Ignore the first 5 seconds of activity. 
GRACE_PERIOD = 5  

def get_idle_time():
    class LASTINPUTINFO(ctypes.Structure):
        _fields_ = [("cbSize", ctypes.c_uint),
                    ("dwTime", ctypes.c_uint)]
    lii = LASTINPUTINFO()
    lii.cbSize = ctypes.sizeof(LASTINPUTINFO)
    ctypes.windll.user32.GetLastInputInfo(ctypes.byref(lii))
    millis = ctypes.windll.kernel32.GetTickCount() - lii.dwTime
    return millis / 1000.0

def open_website_fullscreen(url):
    webbrowser.open(url)
    time.sleep(1)  # Wait for the browser to load
    pyautogui.press('f11')  

def main():
    was_inactive = False
    last_active_time = time.time() 
    
    while True:
        idle_time = get_idle_time()

        # If idle time exceeds the threshold and not already inactive
        if idle_time > INACTIVITY_THRESHOLD and not was_inactive:
            open_website_fullscreen("https://ezzohamdan.github.io/Project-9/")
            was_inactive = True 

        # If user activity is detected and it's not within the grace period, reset inactivity
        elif idle_time <= INACTIVITY_THRESHOLD and not (time.time() - last_active_time < GRACE_PERIOD):
            was_inactive = False  
            last_active_time = time.time()  
        
        # Update last active time if idle time is less than grace period
        elif idle_time <= INACTIVITY_THRESHOLD:
            last_active_time = time.time() 

        time.sleep(1)

if __name__ == "__main__":
    main()
