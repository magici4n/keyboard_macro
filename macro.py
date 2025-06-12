import tkinter as tk
import threading
import time
import keyboard

recorded = []

def record_keys():
    global recorded
    recorded = []
    start_time = time.time()

    def on_key(event):
        if event.name == '\\':
            keyboard.unhook_all()
            print("녹화 종료")
        else:
            timestamp = time.time() - start_time
            recorded.append((event.name, timestamp))
            print(f"기록 {event.name} @ {timestamp:.2f}s")

    keyboard.on_press(on_key)
    keyboard.wait('\\')  # '\' 누르면 종료

def replay_keys():
    print("3초 후 재생 시작")
    time.sleep(3)
    base_time = 0
    for key, delay in recorded:
        sleep_time = delay - base_time
        time.sleep(sleep_time)
        keyboard.press_and_release(key)
        print(f"{key} 입력됨")
        base_time = delay

def start_recording():
    threading.Thread(target=record_keys).start()

def start_replay():
    threading.Thread(target=replay_keys).start()

# tkinter GUI 구성
root = tk.Tk()
root.title("키보드 매크로")
root.geometry("300x150")

btn_record = tk.Button(root, text="🔴 녹화 시작", command=start_recording)
btn_record.pack(pady=10)

btn_replay = tk.Button(root, text="▶ 재생", command=start_replay)
btn_replay.pack(pady=10)

root.mainloop()
