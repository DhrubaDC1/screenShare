from vidstream import StreamingServer
import threading

server = StreamingServer('192.168.0.129', 8080)
thread = threading.Thread(target=server.start_server)
thread.start()

# Other Code

# When You Are Done
# server.stop_server()