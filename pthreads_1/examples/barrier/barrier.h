#ifndef __BARRIER_H_
#define __BARRIER_H_

#include "atomic.h"

struct barrier;

struct barrier *barrier_make(int limit);
int             barrier_get(struct barrier *b);
void            barrier_add(struct barrier *b, int value);
int             barrier_wait(struct barrier *b);
void            barrier_free(struct barrier *b);

#endif
