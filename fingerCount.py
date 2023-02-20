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
                cv.putText(img, 'Thumb', (50,400), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), 2)
            if fingersup.count(1) == 1 and fingersup != [1,0,0,0,0]:
                fing = cv.imread(r"C:\Users\HP\OneDrive\Desktop\Python\OpenCv\Hand Detection and Finger Counting Project\Finger Images\1fing.jpg")
                cv.putText(img, '1 Finger', (50,400), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), 2)
            if fingersup.count(1) == 2:
                fing = cv.imread(r"C:\Users\HP\OneDrive\Desktop\Python\OpenCv\Hand Detection and Finger Counting Project\Finger Images\2fing.jpg")
                cv.putText(img, '2 Fingers', (50,400), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), 2)
            if fingersup.count(1) == 3:
                fing = cv.imread(r"C:\Users\HP\OneDrive\Desktop\Python\OpenCv\Hand Detection and Finger Counting Project\Finger Images\3fing.jpg")
                cv.putText(img, '3 Fingers', (50,400), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), 2)
            if fingersup.count(1) == 4:
                fing = cv.imread(r"C:\Users\HP\OneDrive\Desktop\Python\OpenCv\Hand Detection and Finger Counting Project\Finger Images\4fing.jpg")
                cv.putText(img, '4 Fingers', (50,400), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), 2)
            if fingersup.count(1) == 5:
                fing = cv.imread(r"C:\Users\HP\OneDrive\Desktop\Python\OpenCv\Hand Detection and Finger Counting Project\Finger Images\5fing.jpg")
                cv.putText(img, '5 Fingers', (50,400), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), 2)
    
    fing = cv.resize(fing, (220, 280))
    img[50:330, 20:240] = fing
    cv.imshow("Video", img)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv.destroyAllWindows()