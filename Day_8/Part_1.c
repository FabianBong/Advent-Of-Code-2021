#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#define MAX_STRING_LENGTH 7000


int main()
{
    FILE *fp = fopen("/Users/fabianbong/Documents/Advent_Of_Code/Day_8/input.txt", "r");
    
    char inpString[MAX_STRING_LENGTH];
    
    int sum = 0;
    
    while(fgets(inpString, MAX_STRING_LENGTH, fp))
    {
        char *out;
        out = strtok(inpString, "|");
        out = strtok(NULL, "|");
        
        char *outNum;
        outNum = strtok(out, " ");
    
        if(strlen(outNum) == 7 || strlen(outNum) == 2 || strlen(outNum) == 4 || strlen(outNum) == 3)
            sum++;
        
        outNum = strtok(NULL, " ");
        if(strlen(outNum) == 7 || strlen(outNum) == 2 || strlen(outNum) == 4 || strlen(outNum) == 3)
            sum++;
        
        outNum = strtok(NULL, " ");
        if(strlen(outNum) == 7 || strlen(outNum) == 2 || strlen(outNum) == 4 || strlen(outNum) == 3)
            sum++;
        
        outNum = strtok(NULL, " ");
        outNum[strcspn(outNum, "\n")] = 0;
        if(strlen(outNum) == 7 || strlen(outNum) == 2 || strlen(outNum) == 4 || strlen(outNum) == 3)
            sum++;
        
    }

    printf("%d", sum);

}
