#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#define MAX_STRING_LENGTH 20


int min(int a, int b)
{
    return (a > b) ? b :a;
}

int max(int a, int b)
{
    return (a > b) ? a :b;
}

int main()
{
    FILE *fp = fopen("/Users/fabianbong/Documents/Advent_Of_Code/Day_5/input.txt", "r");
    
    char inpString[MAX_STRING_LENGTH];
    
    int n = 1000;
    
    int map[n][n];
    for(int i = 0; i < n; i++)
    {
        for(int j = 0; j < n; j++)
        {
            map[i][j] = 0;
        }
    }

    while(fgets(inpString, MAX_STRING_LENGTH, fp))
    {
        if(strcmp(inpString, "\n") == 0)
            continue;
        char *coordinate1;
        char *coordinate2;
        coordinate1 = strtok(inpString, "->");
        coordinate2 = strtok(NULL, "->");
        
        int x1,x2,y1,y2;
        
        char *value;
        value = strtok(coordinate1, ",");
        
        x1 = atoi(value);
        
        value = strtok(NULL, ",");
        y1 = atoi(value);
        
        value = strtok(coordinate2, ",");
        x2 = atoi(value);
        
        value = strtok(NULL, ",");
        y2 = atoi(value);
        
        
        if(x1 == x2)
        {
            for(int i = min(y1,y2); i <= max(y1,y2); i++)
            {
                map[i][x1]++;
            }
        }else if(y1 == y2)
        {
            for(int i = min(x1,x2); i <= max(x1,x2); i++)
            {
                map[y1][i]++;
            }
        }
        else
        {
            int newX,newY, subtractX, subtractY;
            if(x1 > x2)
                subtractX = -1;
            else
                subtractX = 1;
            
            if(y1>  y2)
                subtractY = -1;
            else
                subtractY = 1;
            
            newX = x1;
            newY = y1;
            while(newY != y2 && newX != x2)
            {
                map[newY][newX]++;
                newY += subtractY*1;
                newX += subtractX*1;
            }
            map[newY][newX]++;
        }
 
            
    }
    int sum = 0;
    for(int i = 0; i < n; i++)
    {
        for(int j = 0; j<n; j++)
        {
            if(map[i][j] > 1)
                sum++;
        }
    }
    
    printf("%d", sum);
  
}


