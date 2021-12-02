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
  int depthSum[n-2];

  for(int i = 0; i < n -2 ; i++)
  {
   depthSum[i] = depth[i] + depth[i+1] + depth[i+2];
  }

  for(int i = 0; i < n-3; i++)
  {
    if(depthSum[i+1] > depthSum[i])
    {
      larger++;
    }
  }


  printf("%d", larger);
}
