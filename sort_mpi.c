#include <stdio.h>
#include <stdlib.h>
#include <mpi.h>

void bubbleSort(int arr[], int n) {
    for(int i=0;i<n-1;i++)
        for(int j=0;j<n-i-1;j++)
            if(arr[j]>arr[j+1]){
                int temp=arr[j]; arr[j]=arr[j+1]; arr[j+1]=temp;
            }
}

int main(int argc, char **argv) {
    MPI_Init(&argc, &argv);

    int rank, size;
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);

    int n = 6;
    int arr[6] = {5,2,9,1,5,6};
    int chunk = n/size;
    int *sub = malloc(chunk * sizeof(int));

    MPI_Scatter(arr, chunk, MPI_INT, sub, chunk, MPI_INT, 0, MPI_COMM_WORLD);

    bubbleSort(sub, chunk);

    MPI_Gather(sub, chunk, MPI_INT, arr, chunk, MPI_INT

