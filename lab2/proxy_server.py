#!/usr/bin/env python3
import socket
from utils import *
from multiprocessing import Process

#define address & buffer size
HOST = ""
PORT = 8001
BUFFER_SIZE = 1024

PROXIED_HOST = "www.google.com"
PROXIED_PORT = 80

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    
        #QUESTION 3
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
        #bind socket to address
        s.bind((HOST, PORT))
        #set to listening mode
        s.listen(2)
        
        #continuously listen for connections
        while True:
            conn, addr = s.accept()
            print("Connected by", addr)
            p = Process(target=handle_mp, args=(conn,))
            p.daemon = True
            p.start()
            conn.close()

def handle_mp(conn):
    full_data = receive_data(conn, BUFFER_SIZE).decode("utf-8")
    print("Proxy request:", full_data)
    
    #make the socket, get the ip, and connect
    s2 = create_tcp_socket()

    remote_ip = get_remote_ip(PROXIED_HOST)

    s2.connect((remote_ip, PROXIED_PORT))
    print (f'Socket Connected to {PROXIED_HOST} on ip {remote_ip}')
    
    #send the data and shutdown
    send_data(s2, full_data)
    s2.shutdown(socket.SHUT_WR)

    #continue accepting data until no more left
    ret = receive_data(s2, BUFFER_SIZE)
    print("Sending response back")
    conn.sendall(ret)
    
    print("Response sent")
    print("---------------")

if __name__ == "__main__":
    main()
