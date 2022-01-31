import cv2
import time
import numpy as np
import keyboard

fourcc = cv2.VideoWriter_fourcc(*'XVID')
output_file = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

cap = cv2.VideoCapture(0)  
time.sleep(2)
bg = cv2.imread("H:/JISHNU/Rock n' Roll/Works/WhiteHat/Python/Project/CameraFilter/download.jpg")
run = True
while (cap.isOpened())and run:

    if keyboard.is_pressed("esc") or keyboard.is_pressed("q"):
        run = False

    ret, img = cap.read()
    if not ret:
        break        
    img = np.flip(img, axis=1)    
    bg = cv2.resize(bg, (640, 480)) 
    img = cv2.resize(img, (640, 480)) 
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    upper_red = np.array([104, 153, 70])
    lower_red = np.array([0, 0, 0])

    mask_1 = cv2.inRange(hsv, lower_red, upper_red)
    mask_1 = cv2.morphologyEx(mask_1, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8))
    mask_1 = cv2.morphologyEx(mask_1, cv2.MORPH_DILATE, np.ones((3, 3), np.uint8))    
    mask_2 = cv2.bitwise_not(mask_1)    

    res_1 = cv2.bitwise_and(img, img, mask=mask_2)
    res_2 = cv2.bitwise_and(bg, bg, mask=mask_1)
    
    final_output = cv2.addWeighted(res_1, 1, res_2, 1, 0)
    output_file.write(final_output)
    cv2.imshow("magic", final_output)
    cv2.imshow("real", img)
    cv2.waitKey(1)


cap.release()
cv2.destroyAllWindows()