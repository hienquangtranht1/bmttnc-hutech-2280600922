from tkinter import Tk, Button, Text, END
import subprocess
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def run_server():
    output_display.delete(1.0, END)
    server_path = os.path.join(BASE_DIR, "server.py")
    result = subprocess.run(['python', server_path], capture_output=True, text=True)
    output_display.insert(END, result.stdout if result.stdout else result.stderr)

def run_client():
    output_display.delete(1.0, END)
    client_path = os.path.join(BASE_DIR, "client.py")
    result = subprocess.run(['python', client_path], capture_output=True, text=True)
    output_display.insert(END, result.stdout if result.stdout else result.stderr)

app = Tk()
app.title("DH Key Pair Application")

run_server_button = Button(app, text="Run Server", command=run_server)
run_server_button.pack(pady=10)

run_client_button = Button(app, text="Run Client", command=run_client)
run_client_button.pack(pady=10)

output_display = Text(app, height=15, width=50)
output_display.pack(pady=10)

app.mainloop()