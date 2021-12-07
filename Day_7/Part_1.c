#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#define MAX_STRING_LENGTH 7000

int compareInt (const void * a, const void * b) {
   return ( *(int*)a - *(int*)b );
}


int main()
{
    FILE *fp = fopen("/Users/fabianbong/Documents/Advent_Of_Code/Day_7/input.txt", "r");
    
    char inpString[MAX_STRING_LENGTH];
    
    fgets(inpString, MAX_STRING_LENGTH, fp);

    int crabCount = 0;
    
    int crabs[1000];
    for(int i =0 ; i< 1000;i++)
    {
        crabs[i] = 0;
    }

    char * pos;
    pos = strtok(inpString, ",");
    
    while(pos != NULL)
    {
        crabs[crabCount] = atoi(pos);
        pos = strtok(NULL, ",");
        crabCount++;
    }
    
    printf("In total we have: %d crabs \n", crabCount);
    
    qsort(crabs, crabCount, sizeof(int), compareInt);
    
    int median = 0;
    
    median = (crabs[(crabCount-1)/2] + crabs[(crabCount+1)/2])/2;
    
    printf("The median is: %d\n", median);
    
    int sum = 0;
    
    for(int i = 0; i < crabCount; i++)
    {
        sum += abs(median-crabs[i]);
    }
    printf("Sum of all distances: %d\n", sum);
}


