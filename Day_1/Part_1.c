#include <stdio.h>
#include <stdlib.h>

int main()
{
  FILE *fp = fopen("/Users/fabianbong/Documents/Advent_Of_Code/Day_1/input.txt", "r");

  char inpString[100];

  int n = 2000;
  int depth[n];

  int count = 0;
  while(fgets(inpString, 100,fp))
  {
    depth[count] = atoi(inpString);
    count++;
  }

  int larger = 0;

  for(int i = 1; i < n; i++)
  {
    if(depth[i] > depth[i-1])
    {
      larger++;
    }
  }

  printf("%d", larger);
}
