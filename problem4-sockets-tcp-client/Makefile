CC     = gcc
CFLAGS = -Wall -Wextra

.PHONY: all build run test clean

all: build

build: solution
solution: solution.c
	$(CC) $(CFLAGS) -o solution solution.c

run: build
	@echo "Usage: ./solution <ipv4_addr> <port>"

test: build
	@python3 tests/run_tests.py ./solution

clean:
	rm -f solution
