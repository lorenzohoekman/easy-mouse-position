from datetime import datetime
from pynput import mouse

def on_click(x, y, button, pressed):
    if button == mouse.Button.left:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")

        print('{} at {}'.format('Pressed Left Click' if pressed else 'Released Left Click', (x, y)), current_time)
    
    else:
        print("Pressed Right click, Closing the program")
        return False # Returning False if you need to stop the program when Right clicked.

def init():
    listener = mouse.Listener(on_click=on_click)
    listener.start()
    listener.join()


if __name__ == '__main__':
    init()