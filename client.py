# from vidstream import CameraClient
# from vidstream import VideoClient
from vidstream import ScreenShareClient

# Choose One
# client1 = CameraClient('127.0.0.1', 9999)
# client2 = VideoClient('127.0.0.1', 9999, 'video.mp4')
client3 = ScreenShareClient('192.168.0.129', 8080)

# client1.start_stream()
# client2.start_stream()
client3.start_stream()