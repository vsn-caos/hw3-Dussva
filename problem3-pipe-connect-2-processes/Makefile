CC     = gcc
CFLAGS = -Wall -Wextra

.PHONY: all build run test clean

all: build

build: solution
solution: solution.c
	$(CC) $(CFLAGS) -o solution solution.c

run: build
	@echo "Usage: ./solution <CMD1> <CMD2>"

test: build
	@passed=0; failed=0; \
	for f in tests/*.in; do \
	    n=$$(basename $$f .in); \
	    expected="tests/$$n.out"; \
	    [ -f "$$expected" ] || continue; \
	    read -r CMD1 CMD2 < "tests/$$n.args"; \
	    actual=$$(./solution "$$CMD1" "$$CMD2" < "$$f" 2>/dev/null); \
	    exp=$$(cat "$$expected"); \
	    if [ "$$actual" = "$$exp" ]; then \
	        echo "PASS: test $$n"; passed=$$((passed+1)); \
	    else \
	        echo "FAIL: test $$n  expected=[$$exp]  got=[$$actual]"; failed=$$((failed+1)); \
	    fi; \
	done; \
	echo "Results: $$passed passed, $$failed failed"; \
	[ $$failed -eq 0 ]

clean:
	rm -f solution
