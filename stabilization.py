# Время выполнения кода: 396.18249559402466 секунд
# Время выполнения кода: 313.74548625946045 секунд


# Входное видео Формата "TS" 3 минуты 39 секунд. Это 219 секунд
# Время выполнения кода: 460.8513550758362 секунд
# Время выполнения кода: 7.309110637505849 минут. Это 438.54663825035095 секунд
# Время выполнения кода: 7.028223276138306 минут. Это 421.69339656829834 секунд    stabilization_thresh=0.1
# Итого: 1 секунда = 2 секундам

# Входное видео Формата "mp4" 3 минуты 39 секунд. Это 219 секунд
# Время выполнения кода: 8.72259046236674 минут. Это 523.3554277420044 секунд
# Время выполнения кода: 8.646813253561655 минут. Это 518.8087952136993 секунд



#
# Время выполнения кода: 5.016121554374695 минут. Это 300.9672932624817 секунд
import time

start_time = time.time()

# import required libraries
from vidgear.gears import VideoGear
import cv2

def main():
    # open any valid video stream with stabilization enabled(stabilize = True)
    stream_stab = VideoGear(source="orig.ts", stabilize=True).start()

    try:
        # loop over
        while True:
            # read stabilized frames
            frame_stab = stream_stab.read()

            # check for stabilized frame if None-type
            if frame_stab is None:
                break

            # {do something with the frame here}
            # For example, you can perform some operations on frame_stab here

            # Show output window
            cv2.imshow("Stabilized Output", frame_stab)

            # check for 'q' key if pressed
            key = cv2.waitKey(1) & 0xFF
            if key == 27:
                break

    finally:
        # close output window
        cv2.destroyAllWindows()

        # safely close streams
        stream_stab.stop()

if __name__ == "__main__":
    main()


end_time = time.time()
# Вычисляем время выполнения
print(f"Время выполнения кода: {(end_time - start_time) / 60} минут. Это {end_time - start_time} секунд")
