CC     ?= gcc
CFLAGS ?= -pthread -Wall -Wextra -Wnull-dereference -Werror
BINS    = $(basename $(wildcard *.c))

all: $(BINS)

%: %.c
	$(CC) $^ -o $@ $(CFLAGS)

clean:
	rm -f $(BINS)

.PHONY: all clean
