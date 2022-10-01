#Window Resize Utils
from ctypes import windll, Structure, c_long, byref
import webbrowser
import time
import sys

class POINT(Structure):
    _fields_ = [("x", c_long), ("y", c_long)]

def queryMousePosition():
    pt = POINT()
    windll.user32.GetCursorPos(byref(pt))
    return { "x": pt.x, "y": pt.y}

def doresize(window):
    state_left =  windll.user32.GetKeyState(0x01)  # Left button down = 0 or 1. Button up = -127 or -128
    winWbefore=window.width
    winHbefore=window.height

    mouseactive=queryMousePosition()
    beforex= mouseactive['x']
    beforey=mouseactive['y']
    # print(beforex,beforey)
    # print(window.width,window.height)
    # print('Window coordinates are ({0}, {1})'.format(window.x, window.y))

    while True:
        a =  windll.user32.GetKeyState(0x01)
        if a != state_left:  # Button state changed
            state_left = a
            print(a)
            if a < 0:
                print('Left Button Pressed')
                break
            else:
                print('Left Button Released')
                break

        mouseactive=queryMousePosition()
        afterx= mouseactive['x']
        aftery=mouseactive['y']
        try:
            totalx=int(beforex)-int(afterx)
            totaly=int(beforey)-int(aftery)
            # print('totals',totalx,totaly)
        except:
            print('fail')
        if totalx > 0:
            # print('reduce x')
            #  print(totalx*-1)
            changerx=winWbefore+(totalx*-1)
        else:
            # print('expend x')
            changerx=winWbefore+(totalx*-1)
            # print(totalx*-1)
        
        if totaly > 0:
            # print('reduce y')
            # print(totaly*-1)
            changerY=winHbefore+(totaly*-1)
        else:
            # print('expend y')
            #print(totalx*-1)
            changerY=winHbefore+(totaly*-1)
        #
        # print('changed',changerx, changerY)
        window.resize(changerx, changerY)

        time.sleep(0.01)


#Window Set size be %
def setsizer(window,perW,perH):
    user32 = windll.user32
    user32.SetProcessDPIAware()
    [w, h] = [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)]
    

    window.move(10,10)
    
    w= (w*(perW/100)) #resize to 80% of user screen W
    y= (h*(perH/100)) #resize to 80% of user screen H
    # print(w,y)
    window.resize(round(w), round(y))

#Top Frame mini / full screen , Exit
def topbarhandler(code,window):
    if code == "mini":
        window.minimize()
    if code == "full":
        # print(window.get_current_url())
        window.toggle_fullscreen()
        window.move(0, 0)
    if code == "close":
        
        window.destroy()
        sys.exit()

#Bottom Frame
def botbarhandler(code,linkpage):
    print('page link',linkpage,'app code',code )
    if code == "applinks":
        webbrowser.open(linkpage)

    