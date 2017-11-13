#include <assert.h>
#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>

const int N = 500000000;
const int M = 10000;

int data;
void* worker(void* arg) {
    (void) arg;
    for (int i = 0; i < N; i++) {
        data++;
    }
    return NULL;
}

int main() {
    pthread_t id;
    int rc = pthread_create(&id, NULL, worker, NULL);
    assert(!rc);
    for (int i = 0; i < M; i++) {
        int copy = data;
        if (copy % 2 == 0) {
            printf("copy is %d (in progress)\n", copy);
            assert(copy % 2 == 0);
        }
    }
    rc = pthread_join(id, NULL);
    assert(!rc);
    printf("data is %d\n", data);
    return 0;
}
