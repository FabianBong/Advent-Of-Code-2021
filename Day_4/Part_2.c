#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#define MAX_STRING_LENGTH 15



int main()
{
    FILE *fp = fopen("/Users/fabianbong/Documents/Advent_Of_Code/Day_4/input.txt", "r");
    
    char inpString[MAX_STRING_LENGTH];
    
    //Load number string and discard '\n' line
    char numberString[1000];
    fgets(numberString,1000,fp);
    fgets(inpString,MAX_STRING_LENGTH, fp);
    
    
    // put pulled numbers into array
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
    
    //keep tracks of boards won
    int boardsWon[1000];
    for(int i = 0; i < 1000; i++)
    {
        boardsWon[i] = 0;
    }

    //create and fill bingo cards 
    int bingo[1000][5][5];
    int count = 0;
    int row = 0;
    
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

    //keep track of won boards and what bingo wins last with what number
    int iter = 0;
    int winNum = 0;
    int winBingo = 0; 
    int boardsWonCount = 0;
    
    while(iter < countNum)
    {
        int numPulled = numbersPulled[iter];
        
        //Cross of number on bingo cards
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
        
        for(int i =0; i < count; i++)
        {
            //Check only if card is not won yet, if board wins
            if(boardsWon[i] != 1)
            {
                for(int j = 0; j < 5; j++)
                {
                    for(int k = 0; k < 5; k++)
                    {
                        if(bingo[i][j][k] != -1)
                            break;
                        else if(k == 4)
                        {
                            //if card wins either move to end of loop or exit loop
                            winNum = numPulled;
                            winBingo = i;
                            boardsWon[i] = 1;
                            boardsWonCount++;
                            if(boardsWonCount == count)
                                goto end;
                            else
                                goto cont;
                        }
                    }
                }
                
                //check if boards wins 
                for(int j = 0; j < 5; j++)
                {
                    for(int k = 0; k < 5; k++)
                    {
                        if(bingo[i][k][j] != -1)
                            break;
                        else if(k == 4)
                        {
                            //if card wins move to end of loop or exit loop
                            winNum = numPulled;
                            winBingo = i;
                            boardsWon[i] = 1;
                            boardsWonCount++;
                            if(boardsWonCount == count)
                                goto end;
                            else
                                goto cont;
                        }
                    }
                }
            }
        cont:
            ;
        }
        
        iter++;
    }
    
end:
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


