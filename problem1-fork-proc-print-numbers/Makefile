CC     = gcc
CFLAGS = -Wall -Wextra

.PHONY: all build run test clean

all: build

build: solution
solution: solution.c
	$(CC) $(CFLAGS) -o solution solution.c

run: build
	@echo "Usage: ./solution <N>"

test: build
	@passed=0; failed=0; \
	for f in tests/*.args; do \
	    n=$$(basename $$f .args); \
	    expected="tests/$$n.out"; \
	    [ -f "$$expected" ] || continue; \
	    actual=$$(./solution $$(cat "$$f") 2>/dev/null); \
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
