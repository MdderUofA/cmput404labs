#!/usr/bin/env python3
import socket
from utils import *

def main():
    try:
        #define address info, payload, and buffer size
        host = '127.0.0.1'
        port = 8001
        payload = f'My response I expect to get back.'
        buffer_size = 4096

        #make the socket, get the ip, and connect
        s = create_tcp_socket()

        remote_ip = get_remote_ip(host)

        s.connect((remote_ip , port))
        print (f'Socket Connected to {host} on ip {remote_ip}')
        
        #send the data and shutdown
        send_data(s, payload)
        s.shutdown(socket.SHUT_WR)

        #continue accepting data until no more left
        print(receive_data(s, buffer_size))
    except Exception as e:
        print(e)
    finally:
        #always close at the end!
        s.close()
if __name__ == "__main__":
    main()

