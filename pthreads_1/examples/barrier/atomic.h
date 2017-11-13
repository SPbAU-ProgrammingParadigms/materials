#ifndef __ATOMIC_H_
#define __ATOMIC_H_

#include <pthread.h>

struct atomicint {
    int value;
    pthread_mutex_t value_mutex;
};

void atomicint_init(struct atomicint *atomic_int, int init_value);
int atomicint_get(struct atomicint *atomic_int);
void atomicint_add(struct atomicint *atomic_int, int value);
void atomicint_destroy(struct atomicint *atomic_int);

#endif
