import time

start_time = time.time()
import threading
from vidgear.gears import VideoGear
import cv2
import queue
import concurrent.futures


# Функция для захвата видео и помещения кадров в очередь
def video_capture_thread(source, queue, stop_event):
    stream = VideoGear(source=source, stabilize=True).start()
    if stream:
        # Оставшаяся часть вашего кода
        # ...
        while not stop_event.is_set():
            frame = stream.read()
            queue.put(frame)


def main():
    frame_queue = queue.Queue(maxsize=5)
    stop_event = threading.Event()

    capture_thread = threading.Thread(target=video_capture_thread, args=("orig.ts", frame_queue, stop_event))
    capture_thread.start()

    try:
        with concurrent.futures.ThreadPoolExecutor() as executor:
            while True:
                frame_stab = frame_queue.get()

                if frame_stab is None:
                    stop_event.set()
                    break

                # Визуализация кадра движка стабилизации
                cv2.imshow("Stabilized Output", frame_stab)

                # Проверка, была ли нажата клавиша 'q' или 'esc'
                key = cv2.waitKey(1) & 0xFF
                if key == 27 or key == ord('q'):
                    stop_event.set()
                    break
    finally:
        capture_thread.join()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
# Вычисляем время выполнения
end_time = time.time()
tm = f"Время выполнения кода: {(end_time - start_time) / 60} минут. Это {end_time - start_time} секунд"
print(tm)
# Открываем файл для записи (если файл не существует, он будет создан)
with open('Время работы кода.txt', 'w') as file:
    # Записываем текст в файл
    file.write(tm)
# Файл автоматически закрывается благодаря использованию ключевого слова 'with'
