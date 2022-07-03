import pyautogui as ps
import time
def wathsap():
    time.sleep(5)
    while True:
        ps.click(1100, 950)# (x,y)OF bar msg in wathssap web
        ps.write("#### mssage ####")#write msg that u want
        ps.press("enter")
        time.sleep(2)
wathsap()
