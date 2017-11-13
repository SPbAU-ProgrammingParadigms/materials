CFLAGS=-pthread -fsanitize=thread -g
CC=clang

all: example

example: example.c
	$(CC) example.c $(CFLAGS) -o example

clean:
	rm example

.PHONY: clean
