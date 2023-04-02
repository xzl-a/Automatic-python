#!/usr/bin/python3
import socket

def check_network(host="192.168.80.140", port=22, timeout=3):
    """
    Attempts to connect to a host on a specific port.
    Returns True if connection is successful, False otherwise.
    """
    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
        return True
    except socket.error as ex:
        print(str(ex))
        return False

# Example usage
if check_network():
    print("Network is reachable")
else:
    print("Network is not reachable")