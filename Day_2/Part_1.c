#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_STRING_LENGTH 100

int main()
{
    FILE *fp = fopen("/Users/fabianbong/Documents/Advent_Of_Code/Day_2/input.txt", "r");
    
    char inpString[MAX_STRING_LENGTH];
    
    int n = 1000;
    char navigation[n][MAX_STRING_LENGTH];
    int count = 0;
   
    while(fgets(inpString, MAX_STRING_LENGTH,fp))
    {
      strcpy(navigation[count], inpString);
      count++;
    }  

    int horizontal = 0;
    int depth = 0;

    for(int i = 0; i < n; i++)
    {
      char *nav;
      nav = strtok(navigation[i], " ");
      
      int change = 0;

      if(strcmp(nav, "down") == 0)
      {
        nav = strtok(NULL, " ");
        change = atoi(nav);
        depth += change;
      }
      else if (strcmp(nav, "forward") == 0)
      {
        nav = strtok(NULL, " ");
        change = atoi(nav);
        horizontal += change;
      }
      else if(strcmp(nav, "up") == 0)
      {
        nav = strtok(NULL, " ");
        change = atoi(nav);
        depth -= change;
      }

    }
    
    printf("Horizontal: %d \n", horizontal);
    printf("Depth: %d", depth);


}
