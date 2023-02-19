import cv2 as cv
from cvzone.HandTrackingModule import HandDetector

detector = HandDetector(maxHands=1, detectionCon=0.8)
video = cv.VideoCapture(0)

while True:
    ret, img = video.read()
    img = cv.flip(img, 1)
    hand = detector.findHands(img, draw = False)

    fing = cv.imread(r"C:\Users\HP\OneDrive\Desktop\Python\OpenCv\Hand Detection and Finger Counting Project\Finger Images\0fing.jpg")

    if hand:
        lmlist = hand[0]
        if lmlist:
            fingersup = detector.fingersUp(lmlist)
            
            if fingersup == [1,0,0,0,0]:
                fing = cv.imread(r"C:\Users\HP\OneDrive\Desktop\Python\OpenCv\Hand Detection and Finger Counting Project\Finger Images\thumbsup.jpg")
            if fingersup.count(1) == 1 and fingersup != [1,0,0,0,0]:
                fing = cv.imread(r"C:\Users\HP\OneDrive\Desktop\Python\OpenCv\Hand Detection and Finger Counting Project\Finger Images\1fing.jpg")
            if fingersup.count(1) == 2:
                fing = cv.imread(r"C:\Users\HP\OneDrive\Desktop\Python\OpenCv\Hand Detection and Finger Counting Project\Finger Images\2fing.jpg")
            if fingersup.count(1) == 3:
                fing = cv.imread(r"C:\Users\HP\OneDrive\Desktop\Python\OpenCv\Hand Detection and Finger Counting Project\Finger Images\3fing.jpg")
            if fingersup.count(1) == 4:
                fing = cv.imread(r"C:\Users\HP\OneDrive\Desktop\Python\OpenCv\Hand Detection and Finger Counting Project\Finger Images\4fing.jpg")
            if fingersup.count(1) == 5:
                fing = cv.imread(r"C:\Users\HP\OneDrive\Desktop\Python\OpenCv\Hand Detection and Finger Counting Project\Finger Images\5fing.jpg")
    
    fing = cv.resize(fing, (220, 280))
    img[50:330, 20:240] = fing
    cv.imshow("Video", img)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv.destroyAllWindows()