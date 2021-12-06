#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#define MAX_STRING_LENGTH 2000

int main()
{
    FILE *fp = fopen("/Users/fabianbong/Documents/Advent_Of_Code/Day_6/input.txt", "r");
    
    char inpString[MAX_STRING_LENGTH];
    
    fgets(inpString, MAX_STRING_LENGTH, fp);
    
    int fish[1000000];
    int fishCount = 0;
    
    char * days;
    days = strtok(inpString, ",");
    
    while(days != NULL)
    {
        fish[fishCount] = atoi(days);
        days = strtok(NULL, ",");
        fishCount++;
    }
    
    printf("%d\n", fishCount);
    
    for(int days = 0; days < 80; days++)
    {
        int curFishCount = fishCount;
        for(int i = 0; i < curFishCount; i++)
        {
            if(fish[i] == 0)
            {
                fish[i] = 6;
                fish[fishCount] = 8;
                fishCount++;
            }
            else
            {
                fish[i]--;
            }
        }
    }
    
    printf("%d", fishCount);
    
  
}


