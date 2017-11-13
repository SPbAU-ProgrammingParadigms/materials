CC      ?= gcc
CFLAGS  ?= -Wall -Wextra -Werror -ansi -pedantic
LDFLAGS ?= -lpthread

all: volatile nonvolatile

volatile_asm: volatile
	objdump -S -M intel ./volatile

nonvolatile_asm: nonvolatile
	objdump -S -M intel ./nonvolatile

volatile: volatile.c
	$(CC) volatile.c -O3 $(CFLAGS) $(LDFLAGS) -o volatile

nonvolatile: nonvolatile.c
	$(CC) nonvolatile.c -O3 $(CFLAGS) $(LDFALGS) -o nonvolatile

clean:
	rm volatile nonvolatile

.PHONY: clean volatile_asm nonvolatile_asm
