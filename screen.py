import time 
import pyautogui

class game:
    def __init__(self):
        self.status = 0
        self.lasty = 0
        self.lastx = 0
        self.end = None
        self.ready_time = 0
        self.over_time = None
        self.bufferx = time.time()
        self.buffery = time.time()

        # pyautogui.press("t")

    def update(self, x , y):
        # print(x,y)
        if(time.time() > self.bufferx and ((self.lastx < 400 and x > 400) or (self.lastx < 240 and x > 240))):
            self.bufferx = time.time()+0.5
            print("right")
            pyautogui.press("right")

        if(time.time() > self.bufferx and ((self.lastx > 240 and x < 240) or (self.lastx > 400 and x < 400))):
            self.bufferx = time.time()+0.5
            print("left")
            pyautogui.press("left")

        if(time.time() > self.buffery and ((self.lasty > 210 and y < 210) or (self.lasty > 350 and y < 350))):
            self.buffery = time.time()+0.5
            print("up")
            pyautogui.press("up")

        if(time.time() > self.bufferx and ((self.lasty < 350 and y > 350) or (self.lasty < 210 and y > 210))):
            self.buffery = time.time()+0.5
            print("down")
            pyautogui.press("down")

        self.lastx = x
        self.lasty = y

    def get_stauts(self):  
        return self.status

    def start_game(self):
        print("=== start ===")
        self.status = 2
        self.end = time.time()+200
        pyautogui.press('t')    

    def end_game(self):
        self.game_over()

    def end_ready(self):
        self.ready_time = 0
        self.status = 0

    def start_ready(self):
        self.status = 1
        self.ready_time = time.time()+4
    
    def check_ready(self):
        if(self.ready_time < time.time()):
            self.start_game()
            self.ready_time = 0


    def remain_time(self):
        return self.end-time.time()

    def game_over(self):
        self.status = 3
        self.over_time = time.time()+5

    def check_over(self):
        if(self.over_time < time.time()):
            self.status = 0
    
