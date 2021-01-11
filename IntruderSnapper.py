import win32evtlog, win32event, win32api, win32con
import msvcrt, ctypes, cv2, psutil
from datetime import date, datetime

def sec_event_listener():
    
        server = "localhost"
        source_type = "Security"
        
        try:
                h_log = win32evtlog.OpenEventLog(server, source_type)
                flags = win32evtlog.EVENTLOG_BACKWARDS_READ | win32evtlog.EVENTLOG_SEQUENTIAL_READ
                total = win32evtlog.GetNumberOfEventLogRecords(h_log)
                
                h_evt = win32event.CreateEvent(None, 1, 0, "evt0")
                win32evtlog.NotifyChangeEventLog(h_log, h_evt)
                
                while not msvcrt.kbhit():
                    
                    wait_result = win32event.WaitForSingleObject(h_evt, 500)
                    if wait_result == win32con.WAIT_OBJECT_0:
                        take_picture()

                win32api.CloseHandle(h_evt)
                win32evtlog.CloseEventLog(h_log)
        except:
                print('Unable to initiate...')

def get_datetime():
    dt_string = datetime.now().strftime("D%d-%m-%Y_%H_%M_%S")
    return dt_string
    
def take_picture():
    cam = cv2.VideoCapture(0)
    
    photo_dt = get_datetime()
    try:
        ret, frame = cam.read()
        img_name = "IntCam_{:s}.png".format(photo_dt)
        cv2.imwrite(img_name, frame)
        print('Picture taken')
    except:
        print('Unable to take picture')

def check_lock_screen():
    for proc in psutil.process_iter():
        if(proc.name() == "LogonUI.exe"):
            sec_event_listener()

           
#Was not used - Did not provide consistent behavior
def check_lock_screen_2():
    user32 = ctypes.windll.User32
    if (user32.GetForegroundWindow() % 10 == 0):
        return True
    else:
        return False


def lock_screen():
   ctypes.windll.User32.LockWorkStation()



lock_screen()
while True:
    check_lock_screen()    
