#include <stdio.h>
#include <stdlib.h>

int main()
{
  FILE *fp = fopen("/Users/fabianbong/Documents/Advent_Of_Code/Day_1/input.txt", "r");
  char inpString[100];

  int depth[2000];
  int n = 0;

  while(fgets(inpString, 100,fp))
  {
    depth[n] = atoi(inpString);
    n++;
  }

  int larger = 0;
  printf("%d", depth[0]);

  for(int i = 1; i < n; i++)
  {
    if(depth[i] > depth[i-1])
    {
      printf("%d (increase)\n", depth[i]); 
      larger++;
    }
    else
    {
      printf("%d \n", depth[i]);
    }
  }


  printf("%d", larger);
}
