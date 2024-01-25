# Время выполнения кода: 4.024086427688599 минут. Это 241.44518566131592 секунд
import threading
from vidgear.gears import VideoGear
import cv2
import queue
import time

# Функция для захвата видео и помещения кадров в очередь
def video_capture_thread(source, queue, stop_event):
    stream = VideoGear(source=source, stabilize=True).start()
    if stream:
        # Непрерывное чтение кадров из видеопотока и помещение их в очередь
        while not stop_event.is_set():
            frame = stream.read()
            queue.put(frame)
    stream.stop()


def main():
    frame_queue = queue.Queue(maxsize=5)
    stop_event = threading.Event()

    # Запуск потока захвата видео
    capture_thread = threading.Thread(target=video_capture_thread, args=(0, frame_queue, stop_event))
    capture_thread.start()

    try:
        while True:
            # Получение стабилизированного кадра из очереди
            frame_stab = frame_queue.get()

            if frame_stab is None:
                stop_event.set()
                break

            # Визуализация стабилизированного кадра
            cv2.imshow("Stabilized Output", frame_stab)

            # Проверка нажатия клавиши 'q' или 'esc'
            key = cv2.waitKey(1) & 0xFF
            if key == 27 or key == ord('q'):
                stop_event.set()
                break
    finally:
        # Завершение работы потока захвата видео
        capture_thread.join()
        # Закрытие окна вывода
        cv2.destroyAllWindows()

# Вызов функции main
if __name__ == "__main__":
    # Замер времени выполнения
    start_time = time.time()
    main()
    end_time = time.time()
    tm = f"Время выполнения кода: {(end_time - start_time) / 60} минут. Это {end_time - start_time} секунд"
    print(tm)
    # Запись времени выполнения в файл
    with open('Время работы кода.txt', 'w') as file:
        file.write(tm)
