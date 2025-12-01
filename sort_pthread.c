#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>

#define NUM_THREADS 2

typedef struct {
    int *arr;
    int start;
    int end;
} ThreadData;

void swap(int *a, int *b) { int temp = *a; *a = *b; *b = temp; }

void bubbleSort(int arr[], int start, int end) {
    for(int i = start; i < end; i++)
        for(int j = start; j < end-(i-start)-1; j++)
            if(arr[j] > arr[j+1])
                swap(&arr[j], &arr[j+1]);
}

void* threadSort(void* arg) {
    ThreadData *data = (ThreadData*) arg;
    bubbleSort(data->arr, data->start, data->end);
    pthread_exit(NULL);
}

int main() {
    int arr[] = {5,2,9,1,5,6};
    int n = sizeof(arr)/sizeof(arr[0]);
    pthread_t threads[NUM_THREADS];
    ThreadData tdata[NUM_THREADS];

    int chunk = n/NUM_THREADS;

    // Create threads
    for(int i=0;i<NUM_THREADS;i++) {
        tdata[i].arr = arr;
        tdata[i].start = i*chunk;
        tdata[i].end = (i==NUM_THREADS-1)? n : (i+1)*chunk;
        pthread_create(&threads[i], NULL, threadSort, &tdata[i]);
    }

    // Wait for threads
    for(int i=0;i<NUM_THREADS;i++)
        pthread_join(threads[i], NULL);

    // Merge or simple sequential pass to finalize
    bubbleSort(arr, 0, n);

    printf("Sorted array: ");
    for(int i=0;i<n;i++) printf("%d ", arr[i]);
    printf("\n");

    return 0;
}
