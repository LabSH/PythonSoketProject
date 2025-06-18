import tkinter
from tkinter import ttk
import socket
from threading import Thread

def send(event=None):
    msg = input_msg.get()
    selected_user = user_combo.get()
    if selected_user and selected_user != "모두":
        msg = f"/w {selected_user} {msg}"
    sock.send(bytes(msg, "utf-8"))
    input_msg.set("")
    if msg == "end":
        sock.close()
        win.quit()

def recvMessage():
    try:
        while True:
            msg = sock.recv(1024).decode("utf-8")
            if msg.startswith("USERLIST:"):
                users = msg[9:].split(",")
                user_combo["values"] = ["모두"] + users
            else:
                chat_list.insert(tkinter.END, msg)
    except ConnectionAbortedError:
        print("서버 종료")

def on_delete(event=None):
    input_msg.set("end")
    send()

win = tkinter.Tk()
win.title("채팅 프로그램")
win.configure(bg="white")
frame = tkinter.Frame(win, bg="white")
input_msg = tkinter.StringVar()

# Combobox 스타일 설정
style = ttk.Style()
style.theme_use('default')
style.configure("TCombobox", fieldbackground="white", background="white", foreground="black")

user_combo = ttk.Combobox(win, values=["모두"], state="readonly")
user_combo.set("모두")
user_combo.pack(side=tkinter.TOP, fill=tkinter.X, padx=5, pady=5)

scroll = tkinter.Scrollbar(frame)
scroll.pack(side=tkinter.RIGHT, fill=tkinter.Y)

chat_list = tkinter.Listbox(frame, height=15, width=50, yscrollcommand=scroll.set,
                            bg="white", fg="black")
chat_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
frame.pack()

inputbox = tkinter.Entry(win, textvariable=input_msg, bg="white", fg="black")
inputbox.bind("<Return>", send)
inputbox.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=tkinter.YES, padx=5, pady=5)

send_button = tkinter.Button(win, text="전송", command=send, bg="lightgray", fg="black")
send_button.pack(side=tkinter.RIGHT, fill=tkinter.X, padx=5, pady=5)
win.protocol("WM_DELETE_WINDOW", on_delete)

IP = "localhost"
PORT = 9999

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((IP, PORT))
receive_thread = Thread(target=recvMessage)
receive_thread.start()

win.mainloop()
