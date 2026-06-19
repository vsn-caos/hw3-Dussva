#!/usr/bin/env python3
"""Simple TCP test server.

Usage: server.py <port> <exchanges>

Accepts one connection, reads <exchanges> int32 LE values,
responds to each with (value + 1) as int32 LE, then closes.
"""
import socket
import struct
import sys


def run(port: int, exchanges: int) -> None:
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(("127.0.0.1", port))
    server.listen(1)
    conn, _ = server.accept()
    for _ in range(exchanges):
        data = b""
        while len(data) < 4:
            chunk = conn.recv(4 - len(data))
            if not chunk:
                break
            data += chunk
        if len(data) < 4:
            break
        (n,) = struct.unpack("<i", data)
        conn.send(struct.pack("<i", n + 1))
    conn.close()
    server.close()


if __name__ == "__main__":
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 54321
    exchanges = int(sys.argv[2]) if len(sys.argv) > 2 else 3
    run(port, exchanges)
