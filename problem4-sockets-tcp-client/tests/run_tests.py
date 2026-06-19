#!/usr/bin/env python3
"""Run tests for problem4-sockets-tcp-client.

Starts a local TCP server for each test, runs the student binary,
and compares stdout output.

Usage: run_tests.py <path-to-binary>
"""
import socket
import struct
import subprocess
import sys
import threading
import time


TESTS = [
    # (test_name, port, stdin_text, server_responses, expected_stdout)
    ("test 1: basic exchange",    54321, "1\n2\n3\n",   [2, 3, 4],   "2\n3\n4"),
    ("test 2: negative numbers",  54322, "10\n-5\n0\n", [11, -4, 1], "11\n-4\n1"),
    ("test 3: single value",      54323, "100\n",       [101],       "101"),
]


def start_server(port: int, responses: list) -> threading.Thread:
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(("127.0.0.1", port))
    server.listen(1)

    def serve() -> None:
        conn, _ = server.accept()
        for resp in responses:
            data = b""
            while len(data) < 4:
                chunk = conn.recv(4 - len(data))
                if not chunk:
                    break
                data += chunk
            if len(data) < 4:
                break
            conn.send(struct.pack("<i", resp))
        conn.close()
        server.close()

    t = threading.Thread(target=serve, daemon=True)
    t.start()
    return t


def run_test(binary: str, name: str, port: int,
             stdin_text: str, responses: list, expected: str) -> bool:
    t = start_server(port, responses)
    time.sleep(0.1)

    try:
        result = subprocess.run(
            [binary, "127.0.0.1", str(port)],
            input=stdin_text,
            capture_output=True,
            text=True,
            timeout=5,
        )
    except subprocess.TimeoutExpired:
        print(f"FAIL: {name}  (timeout)")
        return False
    finally:
        t.join(timeout=2)

    actual = result.stdout.rstrip("\n")
    exp = expected.rstrip("\n")
    if actual == exp and result.returncode == 0:
        print(f"PASS: {name}")
        return True
    else:
        print(f"FAIL: {name}  expected=[{exp}]  got=[{actual}]  rc={result.returncode}")
        return False


def main() -> None:
    binary = sys.argv[1] if len(sys.argv) > 1 else "./solution"
    passed = 0
    failed = 0
    for args in TESTS:
        if run_test(binary, *args):
            passed += 1
        else:
            failed += 1
    print(f"Results: {passed} passed, {failed} failed")
    sys.exit(0 if failed == 0 else 1)


if __name__ == "__main__":
    main()
