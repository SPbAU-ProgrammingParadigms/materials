#include "barrier.h"

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>
#include <time.h>

int nanosleep(const struct timespec *req, struct timespec *rem);

#define LIMIT 1024
#define NTHREADS 4
#define STEP   128

const struct timespec c_to_sleep = {0, 100000000L}; /* 0 sec + 10^8 ns = 100 ms */

void * walk(void *args) {
	struct barrier *b = (struct barrier *) args;
    // thread local state of rng
    unsigned short state[3];
    unsigned int seed = time(NULL) + (unsigned int) pthread_self();
    memcpy(state, &seed, sizeof(seed));

	for (;;) { /* silly */
		barrier_add(b, nrand48(state) % STEP);

		printf("%d\n", barrier_get(b));

		nanosleep(&c_to_sleep, NULL);
	}
}

int main(void)
{
	int i, rc;
	pthread_t walkers[NTHREADS];
	struct barrier *b = barrier_make(LIMIT);

	srand(time(NULL));


	for (i = 0; i < NTHREADS; ++i) {
		rc = pthread_create(walkers + i, NULL, walk, b);
		assert(!rc);
	}

	printf("Value after wait: %d\n", barrier_wait(b));

	for (i = 0; i < NTHREADS; ++i) {
		rc = pthread_cancel(walkers[i]);
		assert(!rc);
		pthread_join(walkers[i], NULL);
	}

	barrier_free(b);

  return 0;
}
