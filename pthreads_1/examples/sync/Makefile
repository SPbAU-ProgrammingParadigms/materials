CC      ?= gcc
CFLAGS  += -Wall -Wextra -Wnull-dereference -Werror
BIN      = producer_consumer
SRC      = $(wildcard *.c)
OBJ      = $(SRC:.c=.o)

all: $(BIN)

$(BIN): $(OBJ)
	$(CC) $(OBJ) -pthread -o $@

%.o: %.c
	$(CC) -c $(CFLAGS) $< -o $@

clean:
	rm *.o -f $(BIN)

.PHONY: clean
