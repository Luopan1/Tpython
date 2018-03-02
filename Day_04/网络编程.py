#coding=utf-8
import  socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("www.sina.com.cn",80))
s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')
buffer=[]
while True:
	# 接收数据时，调用recv(max)方法，一次最多接收指定的字节数，因此，在一个while循环中反复接收，直到recv()返回空数据，表示接收完毕
	d=s.recv(1024)
	if d:
		buffer.append(d)
	else:
		break
data = b"".join(buffer)
s.close()

header, html = data.split(b'\r\n\r\n', 1)
print(header.decode('utf-8'))
# 把接收的数据写入文件:
with open('sina.html', 'wb') as f:
    f.write(html)
