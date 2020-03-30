#include<iostream>
using namespace std;

//对区间[left,right]进行划分
int Partition(int A[],int left,int right) {
    int temp = A[left];
    while(left < right) {
        while(left < right && A[right] > temp)
            right--;
        A[left] = A[right];
        while(left < right && A[left] <= temp)
            left++;
        A[right] = A[left];
    }
    A[left] = temp;
    return left;
}

void quickSort(int A[],int left,int right) {
    if(left < right) {
        int pos = Partition(A, left, right);
        quickSort(A, left, pos - 1);
        quickSort(A, pos + 1, right);
    }
}

int main() {

    return 0;
}