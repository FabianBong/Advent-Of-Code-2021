#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#define MAX_STRING_LENGTH 15



int main()
{
    FILE *fp = fopen("/Users/fabianbong/Documents/Advent_Of_Code/Day_4/input.txt", "r");
    
    char inpString[MAX_STRING_LENGTH];
    
    char numberString[1000];

    //Get bingo number string and discard '\n' line
    fgets(numberString,1000,fp);
    fgets(inpString,MAX_STRING_LENGTH, fp);
    
    //Create array with numbers pulled for bingo 
    int numbersPulled[200];
    char *num;
    num = strtok(numberString,",");
    int countNum = 0;
    while(num != NULL)
    {
        numbersPulled[countNum] = atoi(num);
        num = strtok(NULL,",");
        countNum++;
    }

    //create bingo cards 
    int bingo[1000][5][5];
    int count = 0;
    int row = 0;
   
    //fill bingo cards
    while(fgets(inpString, MAX_STRING_LENGTH, fp))
    {
        if(strcmp(inpString,"\n") == 0)
        {
            row = 0;
            count++;
            continue;
        }
        int col = 0;
        char *numbers;
        numbers = strtok(inpString," ");
        while(numbers != NULL)
        {
            bingo[count][row][col] = atoi(numbers);
            col++;
            numbers = strtok(NULL, " ");
        }
        fgets(inpString, MAX_STRING_LENGTH,fp);
        row++;
    }
    count++;
   
    //keep track of itreation and winning bingo and number
    int iter = 0;
    int winNum = 0;
    int winBingo = 0;

    //iterate through list of numbers pulled 
    while(iter < countNum)
    {
        int numPulled = numbersPulled[iter];

        //cross of number on card (-1)
        for(int i = 0; i < count; i++)
        {
            for(int j = 0; j < 5; j++)
            {
                for(int k = 0; k < 5; k++)
                {
                    if(numPulled == bingo[i][j][k])
                        bingo[i][j][k] = -1;
                }
            }
                            
        }
        
        //Check if one row is completely crossed
        for(int i =0; i < count; i++)
        {
            for(int j = 0; j < 5; j++)
            {
                for(int k = 0; k < 5; k++)
                {
                    if(bingo[i][j][k] != -1)
                        break;
                    else if(k == 4)
                    {
                        //if one row, end loop
                        winNum = numPulled;
                        winBingo = i;
                        goto end;
                    }
                }
            }
            

            //check if one column is completely crossed
            for(int j = 0; j < 5; j++)
            {
                for(int k = 0; k < 5; k++)
                {
                    if(bingo[i][k][j] != -1)
                        break;
                    else if(k == 4)
                    {
                        //if one column, end loop
                        winNum = numPulled;
                        winBingo = i;
                        goto end;
                    }
                }
            }
        }
        
        iter++;
    }


end:

    //print winning number and calculate answer

    printf("%d \n", winNum);
    
    
    int sum = 0;
    for(int i = 0; i < 5; i++)
    {
        for(int k = 0; k < 5; k++)
        {
            if(bingo[winBingo][i][k] != -1)
                sum += bingo[winBingo][i][k];
        }
    }
    
    printf("%d", sum*winNum);
    

}

