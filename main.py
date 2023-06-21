import cv2
import time
from detect import detect
from screen import game
import win32gui

cap = cv2.VideoCapture(0)

cap.set(3, 640)
cap.set(4, 480)

prev_time = 0
counter = 1
results = None
lasty = 300

detector = detect()
Game = game()

handle = win32gui.FindWindow(None, "BlueStacks App Player")
win32gui.SetForegroundWindow(handle)

while cap.isOpened():
    success, frame = cap.read()

    if success:
        frame = cv2.flip(frame, 1)
        fps = 1/(time.time()-prev_time)
        prev_time = time.time()
        fps = str(int(fps))

        if counter == 1:
            results = detector.get(frame)
            counter = 0
        
        else:
            counter += 1;

        annotated_frame = results[0].plot()
        kpts = results[0].keypoints[0].xy.squeeze().tolist()

        
        cv2.rectangle(annotated_frame, (240,210),(400,350), (0,255,0), 2)            

        if(results[0].boxes.shape[0] == 0):
            if(Game.get_stauts() == 1):
                Game.end_ready()
        else:
            if(Game.get_stauts() == 0):
                Game.start_ready()

            elif(Game.get_stauts() == 1):
                Game.check_ready()

            elif(Game.get_stauts() == 2):
                cv2.putText(annotated_frame, str(int(Game.remain_time())), (400, 70), cv2.FONT_HERSHEY_SIMPLEX, 2, (100, 255, 0), 3, cv2.LINE_AA)
                box = results[0].boxes[0]
                xmin,ymin,xmax,ymax = box.xyxy.tolist()[0]

                x = int((xmin+xmax)/2)
                y = int((ymin+ymax)/2)
                
                if(ymax-y > 100 and xmax-x > 100):
                    Game.update(kpts[0][0],kpts[0][1])

                if(Game.remain_time() < 0):
                    Game.end_game()

        if(Game.get_stauts()==3):
            cv2.putText(annotated_frame, "GAME OVER", (400, 70), cv2.FONT_HERSHEY_SIMPLEX, 2, (100, 255, 0), 3, cv2.LINE_AA)
            Game.check_over()
        elif(Game.get_stauts()<2):
            cv2.putText(annotated_frame, "Start game", (400, 70), cv2.FONT_HERSHEY_SIMPLEX, 2, (100, 255, 0), 3, cv2.LINE_AA)
        
        # for kpt in results[0].keypoints[0].xy.squeeze().tolist():
            # cv2.circle(annotated_frame, (int(kpt[0]),int(kpt[1])), 10, (0,255,0), 2)

        

        if(len(kpts) != 0):
            # print(results[0].keypoints[0].xy.squeeze().tolist()[0])
            cv2.circle(annotated_frame, (int(kpts[0][0]),int(kpts[0][1])), 10, (0,255,0), 2)

       
        # for idx, kpt in enumerate(results[0].keypoints[0]):
        #     print(f"Keypoint {idx}: ", kpt)

        cv2.putText(annotated_frame, fps, (7, 70), cv2.FONT_HERSHEY_SIMPLEX, 2, (100, 255, 0), 3, cv2.LINE_AA)
        cv2.imshow("cam", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()