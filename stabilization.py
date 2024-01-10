# Время выполнения кода: 396.18249559402466 секунд
# Время выполнения кода: 313.74548625946045 секунд
import time
start_time = time.time()

# import required libraries
from vidgear.gears import VideoGear
import numpy as np
import cv2


# open any valid video stream with stabilization enabled(`stabilize = True`)
stream_stab = VideoGear(source="orig.TS", stabilize=True).start()

# loop over
while True:

    # read stabilized frames
    frame_stab = stream_stab.read()

    # check for stabilized frame if None-type
    if frame_stab is None:
        break

    # {do something with the frame here}
    # resized_frame = cv2.resize(frame_stab, None, fx=0.8, fy=0.9)
    # Set the window size smaller than the frame size
    cv2.namedWindow("Stabilized Output", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Stabilized Output", frame_stab.shape[1], frame_stab.shape[0])
    # Show output window
    cv2.imshow("Stabilized Output", frame_stab)

    # check for 'q' key if pressed
    key = cv2.waitKey(1) & 0xFF
    if key == 27:
        break

# close output window
cv2.destroyAllWindows()

# safely close streams
stream_stab.stop()




end_time = time.time()
# Вычисляем время выполнения
print(f"Время выполнения кода: {end_time - start_time} секунд")