import pyautogui as pg
import time

def cursorPositionMonitor():
    pos = pg.position()
    x, y = pos
    pos_msg = "X=" + str(x) + " Y=" + str(y);
            
    rgb = pg.pixel(x, y)
    color_msg = str(rgb[0]) + ", " + str(rgb[1]) + ", " + str(rgb[2])
    
    out_text = "\r" + "Posi: (" + pos_msg + ") RGB: (" + color_msg + ")       "
    print(out_text, end='')
    old_pos = pos
    
    while True:        
        pos = pg.position()
        if pos != old_pos:
            x, y = pos
            pos_msg = "X=" + str(x) + " Y=" + str(y);
            
            rgb = pg.pixel(x, y)
            color_msg = str(rgb[0]) + ", " + str(rgb[1]) + ", " + str(rgb[2])
            
            out_text = "\r" + "Posi: (" + pos_msg + ") RGB: (" + color_msg + ")      "
            
            print(out_text, end='')
            old_pos = pos
        
        time.sleep(0.1)
    
if __name__ == '__main__':
    cursorPositionMonitor()