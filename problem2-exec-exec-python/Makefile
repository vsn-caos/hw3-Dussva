CC     = gcc
CFLAGS = -Wall -Wextra

.PHONY: all build run test clean

all: build

build: solution
solution: solution.c
	$(CC) $(CFLAGS) -o solution solution.c

run: build
	./solution

test: build
	@passed=0; failed=0; \
	for f in tests/*.in; do \
	    expected="tests/$$(basename $$f .in).out"; \
	    actual=$$(./solution < $$f 2>/dev/null); \
	    exp=$$(cat $$expected); \
	    if [ "$$actual" = "$$exp" ]; then \
	        echo "PASS: $$f"; passed=$$((passed+1)); \
	    else \
	        echo "FAIL: $$f  expected=[$$exp]  got=[$$actual]"; failed=$$((failed+1)); \
	    fi; \
	done; \
	echo "Results: $$passed passed, $$failed failed"; \
	[ $$failed -eq 0 ]

clean:
	rm -f solution
