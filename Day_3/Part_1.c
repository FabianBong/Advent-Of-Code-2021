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

    int gamma_rate = 0;
    int epsilon_rate = 0;

    int count_1 = 0;
    for(int i = 0; i < 12; i++)
    {
      for(int j = 0; j < n; j++)
      {
        if(binary[j][i] == '1')
          count_1++;
      }
      if(count_1 > n/2)
      {
        gamma_rate += 1 * pow(2,11-i);
      }
      else
      {
        epsilon_rate += 1*pow(2,11-i);
      }
    count_1 = 0;
    }


    printf("Epsilon: %d \n", epsilon_rate);
    printf("Gamma: %d \n", gamma_rate);
    printf("Power: %d", gamma_rate*epsilon_rate);
}

