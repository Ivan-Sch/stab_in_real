# Входное видео Формата "TS" 3 минуты 39 секунд. Это 219 секунд
# Время выполнения кода: 4.065817399819692 минут. Это 243.94904398918152 секунд

import time

start_time = time.time()

from vidgear.gears import VideoGear
import cv2
import queue
import threading


def video_capture_thread(source, queue, stop_event):
    stream = VideoGear(source=source, stabilize=True).start()
    try:
        while not stop_event.is_set():
            frame = stream.read()
            queue.put(frame)
    finally:
        stream.stop()


def main():
    frame_queue = queue.Queue(maxsize=5)  # Установите максимальный размер буфера
    stop_event = threading.Event()

    # Запустите поток захвата видео
    capture_thread = threading.Thread(target=video_capture_thread, args=("orig.ts", frame_queue, stop_event))
    capture_thread.start()

    try:
        while True:
            # Получите кадр из буфера
            frame_stab = frame_queue.get()

            if frame_stab is None:
                stop_event.set()
                break
            # {do something with the frame here}
            # Например, выполните некоторые операции с frame_stab здесь

            # Показать окно вывода
            cv2.imshow("Stabilized Output", frame_stab)

            # Проверьте, была ли нажата клавиша 'q' или 'esc'
            key = cv2.waitKey(1) & 0xFF
            if key == 27 or key == ord('q'):
                stop_event.set()
                break

    finally:
        # Завершите поток захвата видео
        capture_thread.join()
        # Дайте небольшую задержку перед закрытием окна вывода
        cv2.waitKey(1)
        # Закройте окно вывода
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
