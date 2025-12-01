#include <stdio.h>
#include <stdlib.h>
#include <omp.h>

void bubbleSort(int arr[], int n) {
    int i, j;
    #pragma omp parallel for private(j)
    for(i = 0; i < n-1; i++)
        for(j = 0; j < n-i-1; j++)
            if(arr[j] > arr[j+1]) {
                int temp = arr[j]; arr[j] = arr[j+1]; arr[j+1] = temp;
            }
}

int main() {
    int arr[] = {5,2,9,1,5,6};
    int n = sizeof(arr)/sizeof(arr[0]);

    bubbleSort(arr, n);

    printf("Sorted array: ");
    for(int i=0;i<n;i++) printf("%d ", arr[i]);
    printf("\n");

    return 0;
}
