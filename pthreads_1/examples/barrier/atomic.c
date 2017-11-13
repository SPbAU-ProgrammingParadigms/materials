#include "atomic.h"

#include <assert.h>


void atomicint_init(struct atomicint *atomic_int,int init_value) {
  assert(atomic_int);

  atomic_int->value = init_value;
  pthread_mutex_init(&atomic_int->value_mutex, NULL);
}

int atomicint_get(struct atomicint *atomic_int) {
  assert(atomic_int);

  return atomic_int->value;
}

void atomicint_add(struct atomicint *atomic_int, int value) {
  assert(atomic_int);

  pthread_mutex_lock(&atomic_int->value_mutex);
  atomic_int->value += value;
  pthread_mutex_unlock(&atomic_int->value_mutex);
}

void atomicint_destroy(struct atomicint *atomic_int) {
  assert(atomic_int);

  pthread_mutex_destroy(&atomic_int->value_mutex);
}
