import os
import cv2

os.chdir('Your\VideoFolder\path')

try:
    if not os.path.exists('Name_your_folder_for_the_frames'):
        os.makedirs('Name_your_folder_for_the_frames')
except OSError:
    print('Error: Creating directory of data')

currentFrame = 0
kat = cv2.VideoCapture('Your_Video_Name.extension')
ret, frame = kat.read()
ret = True
while ret:
    kat.set(cv2.CAP_PROP_POS_MSEC, (currentFrame * 1000))  # You can set your frames per second 1000 represents 1 frame/second if you wanna change the FPS do the math this way
    ret, frame = kat.read()
    if not ret: break
    name = 'Your\VideoFolder\path\\anyNameForTheFrame' + str(currentFrame) + '.png'# can also use.jpeg,.bmp but using png will result have less loss in quality
    print('Creating...' + name) # This is for reference not necessary line of code
    cv2.imwrite(name, frame)
    # To stop duplicate images
    currentFrame += 1

# When the process is done, release the capture
kat.release()
cv2.destroyAllWindows()
