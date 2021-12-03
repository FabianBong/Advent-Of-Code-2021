#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#define MAX_STRING_LENGTH 14

int main()
{
    FILE *fp = fopen("/Users/fabianbong/Documents/Advent_Of_Code/Day_3/input.txt", "r");
    
    char inpString[MAX_STRING_LENGTH];
    
    int n = 1000;
    char binary[n][MAX_STRING_LENGTH];
    int count = 0;

    while(fgets(inpString, MAX_STRING_LENGTH, fp))
    {
      strcpy(binary[count], inpString);
      count++;
    }

    int keep[n];
    for(int i = 0; i < n; i++)
    {
        keep[i] = 1;
    }
    
    int count_1 = 0;
    int total = 0;
    
    for(int i = 0; i < 12; i++)
    {
        for(int j = 0; j < n; j++)
        {
            if(keep[j] == 1)
            {
                if(binary[j][i] == '1')
                {
                    count_1++;
                }
                total++;
            }
        }
        
        if(total == 1)
            break;
        
        
        char mostCommon = '0';
        if(count_1 >= (total-count_1))
            mostCommon = '1';
        
        for(int j = 0; j < n; j++)
        {
            if(binary[j][i] != mostCommon && keep[j] == 1)
                keep[j] = 0;
        }
        count_1 = 0;
        total = 0;
    }
    
    for(int i = 0; i < n; i++)
    {
        if(keep[i] == 1)
            printf("Oxygen: %s \n", binary[i]);
    }
    
    ///
    ///
    ///
    
    for(int i = 0; i < n; i++)
    {
        keep[i] = 1;
    }
    
    count_1 = 0;
    total = 0;
    
    for(int i = 0; i < 12; i++)
    {
        for(int j = 0; j < n; j++)
        {
            if(keep[j] == 1)
            {
                if(binary[j][i] == '1')
                {
                    count_1++;
                }
                total++;
            }
        }
        
        if(total == 1)
            break;
        
        
        char leastCommon = '1';
        if(count_1 >= (total-count_1))
            leastCommon = '0';
        
        for(int j = 0; j < n; j++)
        {
            if(binary[j][i] != leastCommon && keep[j] == 1)
                keep[j] = 0;
        }
        count_1 = 0;
        total = 0;
    }
    
    for(int i = 0; i < n; i++)
    {
        if(keep[i] == 1)
            printf("CO2: %s \n", binary[i]);
    }
}


