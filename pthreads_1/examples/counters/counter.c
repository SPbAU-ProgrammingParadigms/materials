#include <assert.h>
#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>

const int N = 500000000;
const int M = 1000;

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
    int rc;
    rc = pthread_create(&id, NULL, worker, NULL);
    assert(!rc);

    for (int i = 0; i < M; i++) {
        printf("data is %d (in progress)\n", data);
    }

    rc = pthread_join(id, NULL);
    assert(!rc);

    printf("data is %d\n", data);
    return 0;
}
