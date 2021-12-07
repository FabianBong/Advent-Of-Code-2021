#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#define MAX_STRING_LENGTH 7000


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

    int sum = 0;
    
    for(int i = 0; i < crabCount; i++)
    {
        sum += crabs[i];
    }
    
    double mean = (double) sum/ (double) crabCount;
    
    // DIdn't have enough time to think about it myself but this 'paper' is giving some insight
    // https://raw.githubusercontent.com/alexandru-dinu/advent-of-code/main/2021/day-07/notes/solution.pdf
    // This means, the opitmum is either ceil or floor of the mean
    
    double meanCeil = ceil(mean);
    double meanFloor = floorf(mean);
    
    int floor = 0;
    int ceil = 0;
    for(int i = 0; i < crabCount; i++)
    {
        int n = fabs(meanFloor - crabs[i]);
        floor += (n*(n+1))/2;
        n = fabs(meanCeil - crabs[i]);
        ceil += (n*(n+1))/2;
    }
    
    
    printf("The sum of the distances is: %d\n", ceil < floor ? ceil : floor);

}


