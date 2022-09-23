#!/usr/bin/env python3
import socket
import time
from multiprocessing import Process
from utils import *

#define address & buffer size
HOST = ""
PORT = 8001
BUFFER_SIZE = 1024

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
    #recieve data, wait a bit, then send it back
    full_data = receive_data(conn, BUFFER_SIZE)
    print("Sending response back")
    conn.sendall(full_data)
    
    print("Response sent")
    print("---------------")

if __name__ == "__main__":
    main()
