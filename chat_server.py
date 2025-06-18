import socketserver

class MyHandler(socketserver.BaseRequestHandler):

    users = {}

    def broadcast(self, msg, exclude=None):
        for username, (sock, addr) in self.users.items():
            if username != exclude:
                sock.send(msg.encode())

    def send_userlist(self):
        userlist = ",".join(self.users.keys())
        for sock, addr in self.users.values():
            sock.send(f"USERLIST:{userlist}".encode())

    def addUser(self, username, conn, addr):
        if username in self.users:
            conn.send("이미 등록되어 있습니다.\n".encode())
            return None

        self.users[username] = (conn, addr)
        self.broadcast(f"{username}이 참여했습니다.\n")
        self.send_userlist()  # 유저 목록 전송
        print(f"채팅 참여 인원 {len(self.users)}")
        return username

    def delUser(self, username):
        del self.users[username]
        self.broadcast(f"{username}이 퇴장했습니다.\n")
        self.send_userlist()  # 유저 목록 전송
        print(f"채팅 참여 인원 {len(self.users)}")

    def handle(self):
        print(self.client_address[0])

        while True:
            self.request.send("이름을 입력하세요".encode())
            print('\n')
            username = self.request.recv(1024).decode()
            if self.addUser(username, self.request, self.client_address):
                break
        
        while True:
            data = self.request.recv(1024).decode()
            print(f"[{username}] {data}")

            if data == "end":
                self.request.close()
                break
            elif data.startswith("/w "):  # 귓속말 처리
                parts = data.split(" ", 2)
                if len(parts) < 3:
                    self.request.send("귓속말 형식: /w 유저명 메시지".encode())
                    continue
                target_user, message = parts[1], parts[2]
                if target_user in self.users:
                    target_sock, _ = self.users[target_user]
                    target_sock.send(f"[귓속말 from {username}]: {message}".encode())
                    self.request.send(f"[귓속말 to {target_user}]: {message}".encode())
                else:
                    self.request.send(f"{target_user}은 존재하지 않습니다.".encode())
            else:
                self.broadcast(f"[{username}]: {data}", exclude=None)
        
        print(f"[{username}] 접속 종료")
        self.delUser(username)

class ChatServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

print("chat server start...")

chat_serv = ChatServer(("", 9999), MyHandler)
chat_serv.serve_forever()
chat_serv.shutdown()
chat_serv.server_close()